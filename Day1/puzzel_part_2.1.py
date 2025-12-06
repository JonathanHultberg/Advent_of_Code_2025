dail = list(range(0, 100))
dail_position = 50
count_zero = 0

with open('input_file.txt', 'r') as file:
    for line in file:
        instruction = line.strip()
        direction = instruction[0]
        clicks = int(instruction[1:])

        if direction == 'R':
            while clicks > 0:
                if dail_position == 0:
                    count_zero += 1
                dail_position += 1
                clicks -= 1
                if dail_position > 99:
                    dail_position = 0

        else:
            while clicks > 0:
                if dail_position == 0:
                    count_zero += 1
                dail_position -= 1
                clicks -= 1
                if dail_position < 0:
                    dail_position = 99

print(count_zero)
