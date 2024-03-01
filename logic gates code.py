user_ans = int(input("if you want to choose a logic gate, \type a number thet represents it:\nNOT gate - 1\nAND gate - 2 \nOR gate - 3\nNAND gate - 4\nNOR gate -5\nXOR gate - 6\nXNOR gate -7\nNothing - 8\n"))
if user_ans != 8:
    user_ans2 = input("Do you want to see the truth table of the gate(enter a) or provide two input(s) and view the output from the logic gate for these inputs(enter b):\n ")
    if user_ans2 == "a":
        if user_ans == 1:
            print("  A  NotA\n  0   1\n  1  0")
        elif user_ans == 2:
            print("  B  A  AB\n  0  0  0\n  0  1  0\n  1  0  0\n  1  1  1")
        elif user_ans == 3:
            print("  B  A  AB\n  0  0  0\n  0  1  1\n  1  0  1\n  1  1  1")
        elif user_ans == 4:
            print("  B  A  AB\n  0  0  1\n  0  1  1\n  1  0  1\n  1  1  0")
        elif user_ans == 5:
            print("  B  A  AB\n  0  0  1\n  0  1  0\n  1  0  0\n  1  1  0")
        elif user_ans == 6:
            print("  B  A  AB\n  0  0  0\n  0  1  1\n  1  0  1\n  1  1  0")
        elif user_ans == 7:
            print("  B  A  AB\n  0  0  1\n  0  1  0\n  1  0  0\n  1  1  1")
    elif user_ans2 == "b":
        if user_ans != 1:
            first_in = input("Enter a number for the first input: ")
            second_in = input("Enter a number for the second input: ")
            
