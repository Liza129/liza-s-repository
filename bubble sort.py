#bubble sort
l = []
inp = input("Enter a number to a list, when you finish just enter letter 'y':")
while inp != "y":#crate a list of numbers from user
    l.append(int(inp))
    inp = input("Enter a number to a list, when you finish just enter letter 'y'")
pass_n = 1#pass number
len_l = len(l) - 1# how many times the loop will repeat
for n in range(len_l):
    comparisons = 0
    swap = 0
    c = 0#counter
    print("Start of Pass:", pass_n)
    for i in range(len_l):
        swap_n = l[c]#max number to swap
        comparisons += 1
        while swap_n > l[c+1]:#compare 2 numbers and if the first one is greater, swap them
            swap += 1
            a,b = l[c], l[c+1]#swapping numbers
            l[c] = b
            l[c+1] = a
            print(l)
        c += 1
    print("End of Pass", pass_n, "\nThere were", comparisons, "comparisons and", swap, "swaps")
    pass_n += 1
 