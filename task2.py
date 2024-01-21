from typing import List, Tuple


def calculate_statistics(m: List[set]) -> Tuple[int, int, float, tuple]:
    total_numbers = 0
    total_sum = 0
    for num in m:
        total_numbers += len(num)
        total_sum += sum(num)

    average_value = total_sum / total_numbers if total_numbers > 0 else 0

    all_sets = tuple(number for numbers in m for number in numbers)

    return total_numbers, total_sum, average_value, all_sets


def main():
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
    total_numbers, total_sum, average_value, all_sets = calculate_statistics(m)
    print("1. Общее количество чисел:", total_numbers)
    print("2. Общая сумма чисел:", total_sum)
    print("3. Среднее значение:", average_value)
    print("4. Собрать все множества в один кортеж:", all_sets)


if __name__ == '__main__':
    main()