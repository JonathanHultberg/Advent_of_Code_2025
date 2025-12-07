def sum_part_1(data):
    row = len(data) - 1
    colum = len(data[0])
    total = 0

    for i in range(colum):
        if data[-1][i] == '+':
            total += sum(int(data[j][i]) for j in range(row))
        elif data[-1][i] == '*':
            product = 1
            for j in range(row):
                product *= int(data[j][i])
            total += product
    return total

def sun_part_2(numbers, operators):
    total = 0
    for i in range(len(operators)):
        if operators[i] == '+':
            total += sum(elm for elm in numbers[i])
        if operators[i] == '*':
            product = 1
            for elm in numbers[i]:
                product *= elm
            total += product
    return total

        

def parser(data):
    operators = []
    numbers = []
    woring_list = []

    for colum in zip(*data):
        num = ''
        found_digit = False
        for ch in colum:
            if ch.isdigit():
                num += ch
                found_digit = True
            elif ch in ('+', '*'):
                operators.append(ch)  

        if found_digit:
            woring_list.append(int(num))
        else:
            if woring_list:
                numbers.append(woring_list)
                woring_list = []
    if woring_list:
        numbers.append(woring_list)
    
    return numbers, operators

with open('input.txt', 'r') as file:
    content = file.readlines()
    part_1 = [line.strip().split() for line in content]
    part_2 = [[elm for elm in line if elm !='\n'] for line in content]

    print(sum_part_1(part_1))

    numbers, operators = parser(part_2)
    print(sun_part_2(numbers, operators))
