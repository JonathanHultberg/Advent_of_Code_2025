def build_largest_number(bank, num_size):
    n = len(bank)
    k = num_size
    number = ""
    start = 0

    for pos in range(k):
        end = n - (k - pos)

        best_index = start
        for curr in range(start, end + 1):
            if int(bank[curr]) > int(bank[best_index]):
                best_index = curr
        
        number += bank[best_index]
        start += best_index + 1

    return int(number)

p1 = p2 = 0
with open('input.txt', 'r') as file:
    battery_banks = file.read().split('\n')

    for bank in battery_banks:
        p1 += build_largest_number(bank, 2)
        p2 += build_largest_number(bank, 12)


    print(p1, p2)
   