dail = list(range(0, 100))
dail_position = 50
count_zero = 0

with open('input_file.txt', 'r') as file:
    for line in file:
        instruction = line.strip()
        direction = instruction[0]
        clicks = int(instruction[1:])

        if direction == 'R':
            count_zero += (dail_position + clicks) //100
            dail_position = (dail_position + clicks) % 100

        else:
            if dail_position == 0:
                count_zero += clicks // 100
            else:
                if clicks < dail_position:
                    count_zero += 0
                else:
                    count_zero += 1 + (clicks - dail_position) // 100

            dail_position = (dail_position - clicks) % 100

print(count_zero)
