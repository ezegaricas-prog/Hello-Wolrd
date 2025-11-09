def mean(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def median(numbers):
    if len(numbers) == 0:
        return 0
    sorted_nums = sorted(numbers)
    mid = len(sorted_nums) // 2
    if len(sorted_nums) % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    if len(numbers) == 0:
        return 0
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    highest = max(counts.values())
    for key in counts:
        if counts[key] == highest:
            return key

def main():
    data = [4, 6, 2, 9, 4, 7, 4, 2]
    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))

if __name__ == "__main__":
    main()
