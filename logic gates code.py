import logic_gates_def
user_ans = int(input("if you want to choose a logic gate, type a number thet represents it:\nNOT gate - 1\nAND gate - 2 \nOR gate - 3\nNAND gate - 4\nNOR gate -5\nXOR gate - 6\nXNOR gate -7\nNothing - 8\n"))

while user_ans != 8:
    user_ans2 = input("Do you want to see the truth table of the gate(enter a) or provide two input(s) and view the output from the logic gate for these inputs(enter b):\n ")
    if user_ans2 == "a":
        if user_ans == 1:
            print("  A  NotA\n  0   1\n  1   0")
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
            if user_ans == 2:
                output = logic_gates_def.AND_gate(first_in,second_in)
                print("The output will be: ", output)
            elif user_ans == 3:
                output = logic_gates_def.OR_gate(first_in,second_in)
                print("The output will be: ", output)
            elif user_ans == 4:
                output = logic_gates_def.NAND_gate(first_in,second_in)
                print("The output will be: ", output)
            elif user_ans == 5:
                output = logic_gates_def.NOR_gate(first_in,second_in)
                print("The output will be: ", output)
            elif user_ans == 6:
                output = logic_gates_def.XOR_gate(first_in,second_in)
                print("The output will be: ", output)
            elif user_ans == 7:
                output = logic_gates_def.XNOR_gate(first_in,second_in)
                print("The output will be: ", output)
        else:
            first_in = input("Enter a number for the first input: ")
            output = logic_gates_def.NOT_gate(first_in)
            print("The output will be: ", output)
    user_ans = int(input("if you want to choose a logic gate, type a number thet represents it:\nNOT gate - 1\nAND gate - 2 \nOR gate - 3\nNAND gate - 4\nNOR gate -5\nXOR gate - 6\nXNOR gate -7\nNothing - 8\n"))
print("Good bye")