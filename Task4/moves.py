with open("/Users/aleksey/Documents/file.txt", "r", encoding="utf-8") as file:
    nums = []
    for line in file:
        nums.append(int(line))
cnt = 0  # Счетчик ходов
mediana = sorted(nums)[len(nums) // 2] #  Медиана списка
for i in sorted(nums):
    cnt += abs(mediana - i)
print(cnt)
