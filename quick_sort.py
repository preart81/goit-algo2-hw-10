import random
import time

import matplotlib.pyplot as plt


# Для реалізації рандомізованого алгоритму QuickSort реалізуйте функцію randomized_quick_sort(arr), де опорний елемент (pivot) обирається випадковим чином.
def randomized_quick_sort(arr) -> list:
    """Рандомізований QuickSort.
    Args:
        arr (list): Список для сортування.
    Returns:
        list: Сортований список.
    """
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr) -> list:
    """Детермінований QuickSort.
    Args:
        arr (list): Список для сортування.
    Returns:
        list: Сортований список.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# функція вимірювання часу виконання QuickSort
def measure_time(sort_func, arr, repeats=5):
    times = []
    for _ in range(repeats):
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)


# Створення набору тестових масивів різного розміру: 10_000, 50_000, 100_000 та 500_000 елементів.
sizes = [10_000, 50_000, 100_000, 500_000]
times_randomized = []
times_deterministic = []

# Заповнення масивів випадковими цілими числами і виміряння часу виконання QuickSort
for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]

    times_randomized.append(measure_time(randomized_quick_sort, arr))
    times_deterministic.append(measure_time(deterministic_quick_sort, arr))

# Виведення результатів
for size, randomized_time, deterministic_time in zip(sizes, times_randomized, times_deterministic):
    print(f"Розмір масиву: {size:_}")
    print(f"   Рандомізований QuickSort: {randomized_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд")

# Побудова графіків, з підписами осей та легендою
plt.plot(sizes, times_randomized, label="Рандомізований QuickSort")
plt.plot(sizes, times_deterministic, label="Детермінований QuickSort")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Час виконання (секунди)")
plt.legend()
plt.show()
