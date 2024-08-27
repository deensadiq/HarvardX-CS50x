from collections import Counter

counts = Counter('aabcbbddacbd')

print(counts)

# sort counter
print("====Sorted====")
print(sorted(counts))

# most common
print("====most common====")
print(counts.most_common(2))

# print counts after sorting
print("====after sorting====")
print(counts)

counts.update('dgaced')

# after adding new values
print("====after adding new entries====")
print(counts)

print(counts['a'])