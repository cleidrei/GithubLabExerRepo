def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if len(numbers) == 0:
        return 0
    sorted_nums = sorted(numbers)
    mid = len(sorted_nums) // 2
    if len(sorted_nums) % 2 == 1:
        return sorted_nums[mid]
    return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

def mode(numbers):
    if len(numbers) == 0:
        return 0

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())
    for num in counts:
        if counts[num] == max_count:
            return num


def main():
    data = [1,2,3,4,5,6,7,8,9]
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
