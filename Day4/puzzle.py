def find_valid_roll(diagram, not_remove):
    total_valid_rolls = 0
    while True:
        valid_rolls = 0
        can_be_removed = []
        for row in range(len(diagram)):
            for col in range(len(diagram[row])):
                adjecent_rolls = 0
                if diagram[row][col] != '@':
                    continue
                adjecent_rolls += check_neigbor(diagram, row, col, True)
                if row - 1 >= 0:
                    adjecent_rolls += check_neigbor(diagram, row - 1, col, False)
                if row + 1 < len(diagram):
                    adjecent_rolls += check_neigbor(diagram, row + 1, col, False)

                if adjecent_rolls < 4:
                    valid_rolls += 1
                    can_be_removed.append((row, col))
        
        total_valid_rolls += valid_rolls
        for row, col in can_be_removed:
            diagram[row] = diagram[row][:col] + 'X' + diagram[row][col + 1:]
        
        
        if valid_rolls == 0 or not_remove:
            break
    return total_valid_rolls

def check_neigbor(diagram, row, col, is_curr_row):
    rolls = 0
    if is_curr_row:
        if col - 1 >= 0 and diagram[row][col - 1] == '@':
            rolls += 1
        if col + 1 < len(diagram[row]) and diagram[row][col + 1] == '@':
            rolls += 1
    else:
        if col - 1 >= 0 and diagram[row][col - 1] == '@':
            rolls += 1
        if diagram[row][col] == '@':
            rolls += 1
        if col + 1 < len(diagram[row]) and diagram[row][col + 1] == '@':
            rolls += 1

    return rolls

with open('input.txt', 'r') as file:
    diagram = file.read().split("\n")

    #Comment out one of the following lines to get the desired output
    print(find_valid_roll(diagram, True))
    print(find_valid_roll(diagram, False))

    