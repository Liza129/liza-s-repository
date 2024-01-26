import functions_binary_and_dicimals

user_ans = int(input("if you want to convert a binary number to a decimal, enter 1. \nDecimal to a binary, enter 2. \nAdd two binary numbers, enter 3. \nHexadecimals to decimals, enter 4. \n Decimals to hexadecimals, enter 5. \nHexadecimals to binary, enter 6. \nBinary to hexadecimals, enter 7.\n And if you want to finish, enter 8. \n "))
while user_ans != 8:
    if user_ans == 1:
        b_0 = input("Enter a binary number: ")
        sum_n = functions_binary_and_dicimals.biToDecimal(b_0)
        print("The decimal number will be: ", sum_n)
    elif user_ans == 2:
        d_0 = int(input("Enter a decimal number: "))
        remaind = functions_binary_and_dicimals.decimalToBi(d_0)
        print("The binary number will be: ", remaind)
    elif user_ans == 3:
        b1 = input("Enter a binary number: ")
        b2 = input("Enter second binary number: ")
        sum_bi = functions_binary_and_dicimals.addToBi(b1,b2)
        print("The sum of binary numbers will be: ", sum_bi)
    elif user_ans == 4:
        h = input("Enter a hexadecimal number: ")
        dec_h_n = functions_binary_and_dicimals.hexToDec(h)
        print("The decimal number will be: ", dec_h_n)
    user_ans = int(input("if you want to convert a binary number to a decimal, enter 1. \nDecimal to a binary, enter 2. \nAdd two binary numbers, enter 3. \nHexadecimals to decimals, enter 4. \n Decimals to hexadecimals, enter 5. \nHexadecimals to binary, enter 6. \nBinary to hexadecimals, enter 7.\n And if you want to finish, enter 8. \n "))
print("Good bye!")
    
    
     
    
    
    
    
