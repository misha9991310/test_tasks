import os
import datetime


def check_and_delete(folder: str, N: int) -> None:
    for (root, dirs, files) in os.walk(folder, topdown=True):
        print((root, dirs, files))
        for f in files:
            print(f)
            file_path = os.path.join(root, f)
            timestamp_of_file_modified = os.path.getmtime(file_path)
            modification_date = datetime.datetime.fromtimestamp(timestamp_of_file_modified)
            number_of_days = (datetime.datetime.now() - modification_date).days

            if number_of_days > N:
                os.remove(file_path)
                print(f" Delete : {f}")


def main() -> None:
    folder = "name_folder"
    N = 4

    check_and_delete(folder, N)


if __name__ == '__main__':
    main()