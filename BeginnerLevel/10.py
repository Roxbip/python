import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
print(a)
print(b)
result_overlaps = [i for i in set(a) if i in b]
print(result_overlaps)
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]
print(result)