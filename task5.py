from typing import Optional, Union, Tuple, List


def find_concatenated_words(word1: str, word2: str) -> Optional[Union[str, Tuple[str, str]]]:
    end_word1 = word1[-2:]
    if end_word1 in word2 and word1 != word2:
        word2_position = word2.find(end_word1) + 2
        chars_collision = word2[:word2_position]

        if word1.endswith(chars_collision):
            word2_intersection = word2[word2_position:]
            new_word = find_concatenated_words(word1, word2_intersection)

            if new_word:
                return word1, new_word
            else:
                return word1, word2_intersection

    return None


def read_word_list_from_file(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        word_list: List[str] = [line.strip() for line in file]
    return word_list


def main():
    file_path = 'text'

    word_list = read_word_list_from_file(file_path)

    if not word_list:
        print("Файл с словами пуст.")
        return

    while True:
        first_word = input("Введите первое слово (или 'exit' для выхода): ").strip().lower()

        if first_word == 'exit':
            break

        for second_word in word_list:
            result = find_concatenated_words(first_word, second_word)

            if result:
                word = ''.join(i for i in result)
                print(word)




if __name__ == "__main__":
    main()