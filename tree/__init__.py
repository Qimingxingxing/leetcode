arr = []

# pass by reference
def recur(temp):
    temp.append(1)

recur(arr)
print(arr)


num = 1

def recur(cur):
    cur += 1
    return cur

recur(num)
print(num) # 2

