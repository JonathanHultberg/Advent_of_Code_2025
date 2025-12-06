
def part_one(min, max):
    total = 0
    for x in range(min, max + 1):
        num_str = str(x)
        if len(num_str) % 2 == 0 and num_str[:len(num_str) // 2] == num_str[len(num_str) // 2:]:
            total += x
    return total

def part_two(min, max):
    total = 0
    for x in range(min, max + 1):
        num_str = str(x)
        for n in range(1, len(num_str) // 2 + 1):
            if len(num_str) % n == 0 and parts_equal(num_str, n):
                    total += x
                    break

    return total


def parts_equal(num_str, n):
    sequence = num_str[:n]
    for i in range(0, len(num_str), n):
        if num_str[i:i + n] != sequence:
            return False
    return True


with open('test.txt', 'r') as f:
    p1 = p2 = 0
    content = f.read()
    id_ranges = content.split(',')

    for id_range in id_ranges:
        id_max_min = id_range.split('-')
        p1 += part_one(int(id_max_min[0]), int(id_max_min[1]))
        p2 += part_two(int(id_max_min[0]), int(id_max_min[1]))


    print(p1, p2)