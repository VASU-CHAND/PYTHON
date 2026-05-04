with open("numbers.txt", "r") as f:
    nums = list(map(int, f.read().split()))

print("Max number:", max(nums))
print("Average:", sum(nums)/len(nums))
print("Count >100:", len([x for x in nums if x > 100]))