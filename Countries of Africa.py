countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome &Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe" ] 
print("You need to guess all countries of Africa")
print("You have 3 lives")
score = 0
lives = 3
number_of_countries_left = len(countries)
number_of_countries_left = int(number_of_countries_left)
while number_of_countries_left > 0:
    print("Number of countries to guess: ", number_of_countries_left)
    country = input("Enter the name of a country: ")
    if country in countries:
        print("Good guess")
        score += 1
        countries.remove(country)
        number_of_countries_left -= 1
        print("Your current score is: ", score)
    else:
        print("Invalid guess")
        score -= 1
        lives -= 1
        print("Your current score is: ", score)
        print(lives, "lives left")
    if lives == 0:
        print("Game over")
        break
    if lives > 0 and number_of_countries_left == 0:
        print("All countries are guessed ")
        break

    