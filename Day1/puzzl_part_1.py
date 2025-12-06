dial = list(range(0, 100))
dail_position = 50
count_zero = 0

with open('input_file.txt', 'r') as file:
    for line in file:
        instruction = line.strip()
        direction = instruction[0]
        clicks = int(instruction[1:])

        if direction == 'R':
            dail_position = (dail_position + clicks) % 100
        else:
            dail_position = (dail_position - clicks) % 100

        if dial[dail_position] == 0:
            count_zero += 1

print(count_zero)
