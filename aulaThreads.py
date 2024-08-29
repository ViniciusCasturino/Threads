import threading
def partial_sum(numbers, start, end, result, index):
    result[index] = sum(numbers[start:end])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_threads = 2
chunk_size = len(numbers) // num_threads
results = [0] * num_threads
threads = []
for i in range(num_threads):
    start = i * chunk_size
    end = start + chunk_size
    thread = threading.Thread(target=partial_sum, args=(numbers, start, end, results, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

total_sum = sum(results)

print(f"A soma total é: {total_sum}")
