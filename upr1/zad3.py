def is_valid_UCN(ucn, should_bypass_checksum=False):
    pass  # write your code here

    ucn = str(ucn)
    if len(ucn) != 10:
        return False
    
    year = int(ucn[0:2])
    month = int(ucn[2:4])
    day = int(ucn[4:6])
    days31 = [1, 3, 5, 7, 8, 10, 12]

    if 0 < month < 12:

        if 0 < day <= 31 and month in days31:
            return True
        
        elif 0 < day <= 28 and month == 2: 
            return True
        elif 0 < day <= 30:
            return True

            
    if not should_bypass_checksum:
        weights = [2, 4, 8, 5, 10, 9, 7, 3, 6]
        checksum = sum(int(ucn[i]) * weights[i] for i in range(9)) % 11
        if checksum != int(ucn[9]):
            return False
    
    return True

print(is_valid_UCN("6101057509") == True)
print(is_valid_UCN("6101057500", should_bypass_checksum=True) == True)
print(is_valid_UCN("6101057500") == False)
print(is_valid_UCN("6913136669") == False)