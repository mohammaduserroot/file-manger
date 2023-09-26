# in the name of ALLAH
import argparse
import os


def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)


def create_directory(directory):
    os.makedirs(directory)
    print("create succsefuly folder !")


def delete_file(file):
    os.remove(file)
    print("delete succsefuly file !")


def delete_directory(directory):
    os.rmdir(directory)
    print(" delete succsefuly folder")


def search_files(directory, file_name):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file_name in file:
                print(os.path.join(root, file))


def main():
    parser = argparse.ArgumentParser(description=' basic file manger')
    parser.add_argument('command', choices=['list', 'create', 'delete_file', 'delete_directory', 'search'],
                        help=' choosie a command')
    parser.add_argument('-d', '--directory', help='path folder')
    parser.add_argument('-f', '--file', help=' path file')
    parser.add_argument('-n', '--name', help='file name ')

    args = parser.parse_args()

    if args.command == "list":
        list_files(args.directory)
    elif args.command == "create":
        create_directory(args.directory)
    elif args.command == "delete_file":
        delete_file(args.file)
    elif args.command == "delete_directory":
        delete_directory(args.directory)
    elif args.command == "search":
        search_files(args.directory, args.name)


if __name__ == '__main__':
    main()