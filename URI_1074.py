# URI: 1074
T = input()
T = int(T)

nums = []
for i in range(T):
    x = input()
    nums.append(int(x))

for num in nums:
    if num % 2 == 0 and num != 0:
        print("EVEN", end="")
    elif num == 0:
        print("NULL")
    else:
        print("ODD", end="")
    
    if num > 0:
        print(" POSITIVE")
    elif num < 0:
        print(" NEGATIVE")
