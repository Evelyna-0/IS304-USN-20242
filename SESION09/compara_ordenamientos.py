import random
import time

# Función Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Función Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Función Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Función Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Generar una lista aleatoria
list_size = 1000  # Tamaño de la lista
random_list = [random.randint(1, 10000) for _ in range(list_size)]

# Medir el tiempo de Bubble Sort
start_time = time.time()
bubble_sort(random_list.copy())
bubble_sort_time = time.time() - start_time

# Medir el tiempo de Selection Sort
start_time = time.time()
selection_sort(random_list.copy())
selection_sort_time = time.time() - start_time

# Medir el tiempo de Insertion Sort
start_time = time.time()
insertion_sort(random_list.copy())
insertion_sort_time = time.time() - start_time

# Medir el tiempo de Merge Sort
start_time = time.time()
merge_sort(random_list.copy())
merge_sort_time = time.time() - start_time

# Crear una lista de tiempos
sort_times = [
    ('Bubble Sort', bubble_sort_time),
    ('Selection Sort', selection_sort_time),
    ('Insertion Sort', insertion_sort_time),
    ('Merge Sort', merge_sort_time)
]

# Ordenar por tiempo
sort_times.sort(key=lambda x: x[1])

# Mostrar los resultados
print("Orden de algoritmos por tiempo (de menor a mayor):")
for algo, tiempo in sort_times:
    print(f"{algo}: {tiempo:.6f} segundos")
