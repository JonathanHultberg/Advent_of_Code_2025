def amount_in_range(ranges, ingredients):
    total = 0
    for ingredient in ingredients:
        in_range = any(start <= ingredient <= end for start, end in ranges)
        if in_range:
            total += 1
    return total

def total_amout_in_range(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    merged_ranges = []

    for start, end in ranges:
        if not merged_ranges:
            merged_ranges.append([start, end])
        else:
            last_end = merged_ranges[-1][1]
            
            if start <= last_end + 1:
                merged_ranges[-1][1] = max(last_end, end)
            else:
                merged_ranges.append([start, end])
    
    return sum(end - start + 1 for start, end in merged_ranges)
    
with open('input.txt', 'r') as file:
    content = file.read().split('\n\n')
    ingredients = []
    ranges_pair = []
    for str_range in content[0].split('\n'):
        ranges_pair.append([int(str_range.split('-')[0]), int(str_range.split('-')[1])])
 
    for ingredient in content[1].split('\n'):
        ingredients.append(int(ingredient))

    
    print(amount_in_range(ranges_pair, ingredients))
    print(total_amout_in_range(ranges_pair))