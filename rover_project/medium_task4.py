# Read data from file
def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            numbers = line.strip().replace(',', ' ').split()
            for num in numbers:
                data.append(float(num))
    return data

# Muchiko Filter (Moving Average)
def muchiko_filter(data, window_size=3):
    n = len(data)
    k = window_size // 2
    result = []

    for i in range(n):
        window = []
        for j in range(i - k, i + k + 1):
            if 0 <= j < n:
                window.append(data[j])
        avg = sum(window) / len(window)
        result.append(avg)

    return result


# Sanchiko Filter (Median Filter)
def sanchiko_filter(data, window_size=3):
    n = len(data)
    k = window_size // 2
    result = []

    for i in range(n):
        window = []
        for j in range(i - k, i + k + 1):
            if 0 <= j < n:
                window.append(data[j])

        window.sort()
        m = len(window)
        if m % 2 == 1:
            median = window[m // 2]
        else:
            median = (window[m // 2 - 1] + window[m // 2]) / 2

        result.append(median)

    return result


# Hybrid Filter (Median → Moving Average)
def hybrid_filter(data):
    step1 = sanchiko_filter(data, 3)
    step2 = muchiko_filter(step1, 3)
    return step2


# Variance calculation (stability check)
def variance(data):
    mean = sum(data) / len(data)
    total = 0
    for x in data:
        total += (x - mean) ** 2
    return total / len(data)


# Main execution
data = read_data("log.txt")

muchiko = muchiko_filter(data)
sanchiko = sanchiko_filter(data)
hybrid = hybrid_filter(data)

print("Variance Comparison:")
print("Original:", variance(data))
print("Muchiko:", variance(muchiko))
print("Sanchiko:", variance(sanchiko))
print("Hybrid:", variance(hybrid))


# Find best filter
results = [
    ("Muchiko", variance(muchiko)),
    ("Sanchiko", variance(sanchiko)),
    ("Hybrid", variance(hybrid))
]

best = results[0]
for r in results:
    if r[1] < best[1]:
        best = r

print("Best Filter:", best[0])