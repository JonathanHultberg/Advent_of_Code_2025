def sum_solutions(data):
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


with open('test.txt', 'r') as file:
    content = file.readlines()
    part_1 = [line.strip().split() for line in content]
    part_2 = content
    print(part_2)
    print(sum_solutions(part_1))