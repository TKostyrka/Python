evs = [2, 4, 6, 8]
ods = [1, 3, 5, 7]
pg = "The quick brown fox jumps over the lazy dog"

print(list(pg))
print(sorted(pg))
print(sorted(list(set(pg.lower()))))

# --------------------------------------------------------------------------------------------

nums = evs + ods
snums = sorted(evs + ods)
print(nums)
print(snums)

# --------------------------------------------------------------------------------------------

del snums[0:2]
print(snums)
del snums[0:2]
print(snums)
