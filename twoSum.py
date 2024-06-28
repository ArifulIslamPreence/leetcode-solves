a = [2,7,4,2,8]
target = 9

hashMap = {}

for i, n in enumerate(a):
    diff = target - n
    if diff in hashMap:
        return [hashMap[diff], i]
    hashMap[diff] = i

return
