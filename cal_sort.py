with open('input.txt', 'r') as c:
    lines = c.readlines()
c.close()

highest_cal = 0
second_cal = 0
third_cal = 0
i = 0
elf_calories = 0
while i < len(lines):
    
    if lines[i] != '\n':
        elf_calories += int(lines[i].replace('\n',''))
    else:
        if highest_cal < elf_calories:
            third_cal, second_cal, highest_cal = second_cal, highest_cal, elf_calories
        elif second_cal < elf_calories:
            third_cal, second_cal = second_cal, elf_calories
        elif third_cal < elf_calories:
            third_cal = elf_calories
        elf_calories = 0
    i += 1

print(highest_cal)
print(second_cal)
print(third_cal)
print(highest_cal + second_cal + third_cal)

    
    