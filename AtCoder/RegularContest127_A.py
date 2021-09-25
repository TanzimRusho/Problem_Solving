num = input()

if num[0] != '1': # for values > 10^9, this won't work.
    for i in range(1, len(num)+1):
        print(i, end="")

else: # need a better algorithm to count the leading 1's
    n = int(num)
    
    count = 0
    
    for i in range(1, n+1):
        num_str = str(i)
        
        j = 0
            
        while j < len(num_str) and num_str[j] == '1':
            count += 1 
            j += 1 
    
    print(count)
