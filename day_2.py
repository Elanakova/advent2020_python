#Part 1. Check if passwords are valid. For example: 1-3 a: abcde - you need to check if password contains 'a' at least 1
#time and at most 3 times. Result - number of valid passwords in list given in file day_2_file

#Part 2. Check if passwords are valid. For example: 1-3 a: abcde
# 1 and 3 are positions in password string. Password is valid if only one position contains 'a'.
#Result - number of valid passwords in list given in file day_2_file

def check_pass_part1():
    count = 0
    sym_count = 0
    f = open("day_2_file")
    for line in f:
        rule = line.split(": ")[0]
        password = line.split(": ")[1]
        sym = rule.split(' ')[1]
        min_count = int(rule.split(' ')[0].split('-')[0])
        max_count = int(rule.split(' ')[0].split('-')[1])
        for i in range(len(password)):
            if password[i] == sym:
                sym_count = sym_count + 1
                print(sym_count)
        print('----')
        if sym_count >= min_count and sym_count <= max_count:
            count = count + 1
        sym_count = 0
        print(count)
    f.close()

def check_pass_part2():
    count = 0
    sym_count = 0
    f = open("day_2_file")
    for line in f:
        rule = line.split(": ")[0]
        password = line.split(": ")[1]
        sym = rule.split(' ')[1]
        pos_1 = int(rule.split(' ')[0].split('-')[0])
        pos_2 = int(rule.split(' ')[0].split('-')[1])

        if password[pos_1 - 1 ] == sym and password[pos_2 - 1] != sym or password[pos_1 - 1] != sym and password[pos_2 - 1] == sym:
            count += 1
    print(count)

def main():
    check_pass_part1()
    check_pass_part2()

if __name__ == '__main__':
    main()