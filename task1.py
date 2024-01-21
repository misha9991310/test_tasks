import csv


def main() -> None:
    unique_records = dict()

    with open('f.csv', 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter='|')
        for row in csv_reader:
            record_id = row['id'].strip()
            record = (
                row['lastname'].strip(),
                row['name'].strip(),
                row['patronymic'].strip(),
                row['date_of_birth'].strip(),
            )
            if record_id not in unique_records:
                unique_records.update({record_id: record})
            else:
                print(f"id - {record_id} дублируется, \nс данными - {record}")


if __name__ == '__main__':
    main()



