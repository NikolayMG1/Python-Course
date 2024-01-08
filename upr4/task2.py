# ---Internal state, do not touch---
counters = {
    'pass_instantly': 0,
    'pass_after_third_try': 0,
    'pass_after_fifth_try': 0,
    'never_pass': 0,
}
def retry(func):
    def wrapper(depth = 3):
            if depth == 0:
                 return False
            if func() == True:
                return True
            else : 
                return wrapper(depth-1)
    return wrapper

# Tests
@retry
def pass_instantly():
    counters['pass_instantly'] += 1
    return True

@retry
def pass_after_third_try():
    counters['pass_after_third_try'] += 1
    return counters['pass_after_third_try'] == 3

@retry
def pass_after_fifth_try():
    counters['pass_after_fifth_try'] += 1
    return counters['pass_after_fifth_try'] == 5

@retry
def never_pass():
    counters['never_pass'] += 1
    return False


assert pass_instantly() == True
assert counters['pass_instantly'] == 1
assert pass_after_third_try() == True
assert counters['pass_after_third_try'] == 3
assert pass_after_fifth_try() == False
assert counters['pass_after_fifth_try'] == 3
assert never_pass() == False
assert counters['never_pass'] == 3