def rule_one(num):
    num = str(num)
    passing = 0
    if len(num) == 6:
        passing = 1
    return passing

def rule_two(num):
    num = str(num)
    doubles = []
    last = num[:1]
    passing = 1
    for i in range(2, 7):
        if num[i-1:i] == last:
            doubles.append(last)
        last = num[i-1:i]

    if len(doubles) == 0:
        return 0
    
    for i in range(0, len(doubles)):
        check = doubles.copy()
        check.remove(check[i])
        if doubles[i] in check:
            passing = 0
        elif doubles[i] not in check:
            passing = 1
            break
        
    return passing

def rule_three(num):
    num = str(num)
    last = num[:1]
    passing = 1
    for i in range(2, 7):
        if num[i-1:i] < last:
            passing = 0
            quit
        last = num[i-1:i]
    return passing

nums = [112233, 123444, 111122, 112222]
solutions = 0

for num in range(245318, 765748):
    final = (rule_one(num) and rule_two(num) and rule_three(num))
    solutions += final

print(solutions)
