print(list(range(3, 6)))            # normal call with separate arguments

args = [3, 6]
print(list(range(*args)))