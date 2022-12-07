def infinite_add(x):
    operand_list = []
    print("INPUT NUMBERS \n")

    for i in range(x):
        print("Enter operand number ", i+1)
        element = float(input())
        operand_list.append(element)

    sum = 0
    for element in operand_list:
        sum = sum + element

    return [sum, operand_list]


if __name__ == '__main__':
    x = int(input("Enter how many numbers you want to add: "))
    result = infinite_add(x)
    print("\n\n\n\n")
    
    print(float(result[1][0]), end="")
    
    for i in range(1, len(result[1])):
        print(" + ", result[1][i], end="")
        
    print(" = ", result[0])
