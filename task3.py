from typing import Dict, List


def transformations(list_value: List[list]) -> Dict:
    max_list = max(len(sublist) for sublist in list_value)
    keys = [f'k{i + 1}' for i in range(max_list)]
    b = [dict(zip(keys, sublist)) for sublist in list_value]
    return b


def main() -> None:
    a = [[1, 2, 3], [4, 5, 6]]
    print(transformations(a))


if __name__ == '__main__':
    main()