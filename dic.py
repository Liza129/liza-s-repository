f = open("C:\\Users\\lizab\\Downloads\\book.txt","r")
dic = {}
for i in f:
    words = i.strip().split()
    for x in words:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
def get_count(item):
    return item[1]
dic = sorted(dic.items(), key = get_count)
for i,x in dic[-1:-11:-1]:
    print(f"'{i}' appears {x} times\n")