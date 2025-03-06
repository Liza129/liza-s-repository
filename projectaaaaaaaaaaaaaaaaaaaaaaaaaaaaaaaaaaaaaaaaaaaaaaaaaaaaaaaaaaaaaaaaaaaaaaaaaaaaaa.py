import pandas as pd
import copy
import math
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\21YBratushkin.ACC\\Downloads\\countries-table.csv")
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("project-cb978-firebase-adminsdk-o6ddb-e3a40dcfc5.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://project-cb978-default-rtdb.europe-west1.firebasedatabase.app/'})

#Cleaning 

#drop unused columns
df = df.drop(columns = ["place","pop2030", "pop2050","area", "cca2","cca3","netChange","unMember","worldPercentage","density","densityMi"])
#drop duplicate rows
df.drop_duplicates(subset=['country'], inplace=True)
df = df.drop_duplicates(subset='rank', keep='first')
#drop when all values are missing
df.dropna(how='all', inplace=True)
#remove rows with invalid values
df = df[df != 'invalid_value']
#rename columns
df.rename(columns={'landAreaKm': 'land_area',"growthRate":"growth_rate"}, inplace=True)
#convert column values to specific types
df = df.astype({"pop1980":int, "pop2000":int,"pop2010":int, "pop2023":int, "pop2024":int,"land_area":float, "country":str,"growth_rate":float,"rank":int})
#round coulumns
df = df.round({"pop1980":0, "pop2000":0,"pop2010":0, "pop2023":0, "pop2024":0,"land_area":2})
#reorder columns
df = df[['pop1980', 'pop2000', 'pop2010',"pop2023","pop2024","rank","growth_rate","land_area","country"]]
#detect and count missing values
missing_counts = df.isna().sum()
#print(missing_counts)
#check types
#print(df.dtypes)


obj = {}
"""
All keys:
pop1980
pop2000
pop2010
pop2023
pop2024
rank
growth_rate
land_area
country
"""

#store dataset in the dictionary
for column in df.columns:
    obj[column] = list(df[column])
#create a list with all countries to send to firebase
countries_to_js = obj["country"]

#list with keys in which population is stored
l_col_names = []#['pop1980', 'pop2000', 'pop2010', 'pop2023', 'pop2024']
c = 1
for i in obj:
    if c <= 5:
        l_col_names.append(i)
    c += 1

#create 2 other identical objects to obj, one of which has only EU countries and the other will have only nonEU  
obj_EU = copy.deepcopy(obj)
obj_NotEU = copy.deepcopy(obj)
eu = ["Austria","Belgium","Bulgaria","Croatia","Cyprus","Czech Republic","Denmark","Estonia","Finland","France","Germany","Greece","Hungary","Ireland","Italy","Latvia","Lithuania","Luxembourg","Malta","Netherlands","Poland","Portugal","Romania","Slovakia","Slovenia","Spain","Sweden"]

not_eu = []
for i in obj["country"]:
    if i not in eu:
      not_eu.append(i)  
growth_rate = obj["growth_rate"]
pop2024 = obj["pop2024"]


c = 0
#create dictionaries for EU and non-EU to store population for eu/non_eu countries only
#same layout as in obj, but store only population
EUIndexes = []
NonEUIndexes = []
for i in obj["country"]:
    if i in eu:
        EUIndexes.append(c)
    else:
        NonEUIndexes.append(c)
    c+=1   

for key in obj_NotEU:
    tmp = obj_NotEU[key]
    obj_NotEU[key] = [value for indexPos, value in enumerate(tmp) if indexPos in NonEUIndexes]
           

for key in obj_EU:
    tmp = obj_EU[key]
    obj_EU[key] = [value for indexPos, value in enumerate(tmp) if indexPos in EUIndexes]

    
#print(obj)
#print('EU',obj_EU)
#print('Non-EU',obj_NotEU)

#Density
#Total land area
def tot_land_F(obj):
    sum_land = 0
    for i in obj["land_area"]:#add up each countries land area
        sum_land += i
    return sum_land#130364272.63999997


#Average/mean and total population
def ave_tot_pop_F(obj,i):
    sum_pop = 0
    for x in obj[i]:#go through population in given year and add it up
        sum_pop += x
    ave_pop = sum_pop/obj["rank"][-1]#divide by the number of countries to get mean
    return ave_pop,sum_pop

#function to calculate density using formula
def formula_den_F(year_p,land):
    density = year_p/land
    return density


        
#function to calculate density of each country individually
def density_of_each_country_points(l_col_names,obj):
    density_of_each_c_obj = {}
    c = 0
    
    for x in obj["country"]:
        for i in l_col_names:
            year_p = obj[i][c]#get population of a specific country in a specific year
            land = obj["land_area"][c]#get land area of that country
            density = formula_den_F(year_p,land)#calculate density
            
            #layout of the dictionary
            #density_of_each_c_obj[India] = ["density in year1","density in year2","density in year3","density in year4","density in year5"]
            
            if i in density_of_each_c_obj:#if country is already in density_of_each_c_obj append to the end of the list
                density_of_each_c_obj[i] += [density]
            else:
                density_of_each_c_obj[i] = []#if not, create an empty list and add density to it
                density_of_each_c_obj[i] += [density]
        c += 1
        
    return density_of_each_c_obj

density_of_each_c_obj = density_of_each_country_points(l_col_names,obj)
#print("not sorted",density_of_each_c_obj)






#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



#function which sorts dictionary with all individuall countries, from least density to highest
def sort_each_value_of_density_country_obj(density_of_each_c_obj):
    obj2 = {}#dictionary with from gratest to least densities
    
    for key,value in density_of_each_c_obj.items():
        value.sort()
        obj2[key] = value
    return obj2
sorted_density_of_each_c_obj = sort_each_value_of_density_country_obj(copy.deepcopy(density_of_each_c_obj))
#print("sorted",sorted_density_of_each_c_obj)



#function to create a dictionary with key as a country and value[#,#,#,#,#] which shows density in each year
def country_density_points_F(obj,sorted_density_of_each_c_obj,density_of_each_c_obj):  
    obj_firebase_density_countries = {}
    
    for key,value in sorted_density_of_each_c_obj.items():
        for i in value:
            try:
                indexPosition = density_of_each_c_obj["pop1980"].index(i)
                if obj["country"][indexPosition] not in obj_firebase_density_countries:
                    obj_firebase_density_countries[obj["country"][indexPosition]]=[]
                    for everyYear in l_col_names:
                        
                        obj_firebase_density_countries[obj["country"][indexPosition]]+=[density_of_each_c_obj[everyYear][indexPosition] ]
                
            except:
                print('Unable to find value at position: ',i)
                break
        break
                 
    return obj_firebase_density_countries
obj_firebase_density_countries = country_density_points_F(obj,sorted_density_of_each_c_obj,density_of_each_c_obj)
#print("our obj",obj_firebase_density_countries)


def points_density_F(l_col_names):
    total_pop_l = [] #[4445984509, 6169875598, 7019913954, 8089994739, 8160255134]
    for i in l_col_names:
        n,x = ave_tot_pop_F(obj,i)
        total_pop_l.append(x)
    land = tot_land_F(obj)
    density_l = []#[34.1043172256064, 47.32796396630899, 53.84844951642114, 62.05683946352743, 62.5957938378906]
    for year_p in total_pop_l:
        g = formula_den_F(year_p,land)
        density_l.append(g)
    return density_l, [1980,2000,2010,2023,2024], total_pop_l
y_axis_d, x_axis_d, total_pop_l = points_density_F(l_col_names)#points on the graph[34.1043172256064, 47.32796396630899, 53.84844951642114, 62.05683946352743, 62.5957938378906] [1980, 2000, 2010, 2023, 2024]

#Standard dev

def ave_pop_in_list_F(l_col_names,obj):
    ave_pop_l = []#[18999933.7991453, 26366989.735042736, 29999632.282051284, 34572627.08974359, 34872885.18803419]
    for i in l_col_names:
        n,x = ave_tot_pop_F(obj,i)
        ave_pop_l.append(n)
    return ave_pop_l

def country_pop_min_mean_F(obj,key,c):
    l = []#list of each country in the particular year - mean
    for i in obj[key]:
        l.append(i - ave_pop_in_list_F(l_col_names,obj)[c])
    return l

def points_stn_dev_F(l_col_names,obj):
    #pop-mean
    pop_country_less_ave_d = {}
    for i in l_col_names:
        pop_country_less_ave_d[i] = []
    c = 0
    for key in pop_country_less_ave_d:
        pop_country_less_ave_d[key] = country_pop_min_mean_F(obj,key,c)
        c += 1
    #square each
    c = 0
    for key in pop_country_less_ave_d:
        for i in pop_country_less_ave_d[key]:
            i = i**2
            pop_country_less_ave_d[key][c] = i
            c+=1
        c = 0
    #sum all
    sum_in_each_year = 0
    for key in pop_country_less_ave_d:
        for i in pop_country_less_ave_d[key]:
            sum_in_each_year += i
        #divide ny number of countries
        sum_in_each_year = sum_in_each_year/len(obj["country"])#obj["rank"][-1]
        #square root
        sum_in_each_year = sum_in_each_year**0.5
        #substitude back into dictionary
        pop_country_less_ave_d[key] = sum_in_each_year
        sum_in_each_year = 0
    
    y_axis = []#[81420952.09280767, 111697438.90249301, 124320333.94819558, 137498838.86868116, 138051643.75059503]
    for key in pop_country_less_ave_d:
        y_axis.append(pop_country_less_ave_d[key])
    return y_axis, [1980,2000,2010,2023,2024]

y_axis_stn_d,x_axis_stn_d = points_stn_dev_F(l_col_names,obj)

y_axis_stn_d_eu,x_axis_stn_d_eu = points_stn_dev_F(l_col_names,obj_EU)
y_axis_stn_d_not_eu,x_axis_stn_d_not_eu = points_stn_dev_F(l_col_names,obj_NotEU)
#POINTS111111111!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

y_axis_d_round = []
y_axis_stn_d_round = []
#round all y_axis to 1 decimal place
for i in y_axis_d:
    i = round(i,1)
    y_axis_d_round.append(i)
for x in y_axis_stn_d:
    x = round(x,1)
    y_axis_stn_d_round.append(x)

#Chart 3 predicted population
def predicting_pop_F(obj):
    k, p0 = ave_tot_pop_F(obj,"pop2024")#assuming initial population is in 2024 => P0
    t = [5,10,30,50]#list of the timeframe for which I'm predicting population
    rate,k = ave_tot_pop_F(obj,"growth_rate")#getting average growth rate of the world
    l_predicted_y = []#list of predicted population
    for i in t:
        c = p0*math.exp(rate*i)#formula for prediction
        c = int(c)
        l_predicted_y.append(c)
    l_percentage_x1 = []
    for i in l_predicted_y:
        j = ((i-p0)/p0)*100
        j = int(j)
        j = str(j) + "% increase"
        l_percentage_x1.append(j)
    years = [2030,2025,2055,2075]
    c = 0
    l_percentage_x = []
    for i in l_percentage_x1:
        i = str(i)+" in "+str(years[c])
        l_percentage_x.append(i)
        c +=1
        
    return l_percentage_x,l_predicted_y,years
l_percentage_x,l_predicted_y,years = predicting_pop_F(obj)
#print("predicted", l_percentage_x,l_predicted_y)



#print("Density: \nx-axis: ",x_axis_d,"\ny-axis:",y_axis_d_round,"\nStandard deviation:","\nx-axis:",x_axis_stn_d,"\ny-axis:",y_axis_stn_d_round)



#firebase
fb_dictionary={
    "Graph1_density":{
        "x_axis_density":x_axis_d,
        "y_axis_density":y_axis_d_round
        },
    "Graph2_stn_dev":{
        "x_axis_stn_dev":x_axis_stn_d,
        "y_axis_stn_dev":y_axis_stn_d_round,
        "y_eu":y_axis_stn_d_eu,
        "y_not_eu":y_axis_stn_d_not_eu
        },
    "Graph3_pred":{
        "x_axis_pred":l_percentage_x,
        "y_axis_pred":l_predicted_y
        },
    "Country_list": countries_to_js,
    "Country_density":obj_firebase_density_countries,
    "EU_c":eu,
    "NonEU_c":not_eu,
    "growth_rate":growth_rate,
    "pop2024":pop2024
    }

ref = db.reference('/')

ref.set(fb_dictionary)

#plotting the points on the graph
#plt.plot(x1, y1, label = "line 1")
#line
list_n = ["1980", "2000", "2010", "2023", "2024"]
plt.plot(list_n, y_axis_d_round)
plt.xlabel('Time')
plt.ylabel('density pop/km2')
plt.title('Density of the world over time')
#plt.legend()
plt.show()
#bar
left = [1, 2, 3, 4, 5]

plt.bar(left, y_axis_stn_d_round, tick_label = x_axis_stn_d,
        width = 0.8, color = ['#8e5ea2', '#c45850','#3e95cd','#3cba9f',"#e8c3b9"])
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Variation in population size across the world over time')
plt.show()
#pie
"""
plt.plot(l_percentage_x,l_predicted_y )
plt.xlabel('Cumulative growth percentage')
plt.ylabel('population')
plt.title('Predicted population')
plt.show()
"""
years2 = []
for i in years:
    i = str(i)
    years2.append(i)
    
#print("years2",years2,"l_predicted_y",l_predicted_y,"l_percentage_x",l_percentage_x)
fig, ax = plt.subplots()
ax.pie(l_predicted_y, labels=l_percentage_x)
plt.title('Predicted population')

plt.show()