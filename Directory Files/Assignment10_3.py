import os
import shutil
import sys

def copy(first_dir, second_dir):

    if not os.path.exists(second_dir):
        os.makedirs(second_dir)
        print(f"Created directory: {second_dir}")
    files = os.listdir(first_dir)

    for file in files:
        first_path = os.path.join(first_dir, file)
        dest_path = os.path.join(second_dir, file)
        shutil.copy2(first_path, dest_path)
        print(f"Copied {file} to {second_dir}")

def main():
    if len(sys.argv) != 3:
        print("This Script is executed by command line argument")
        sys.exit(1)

    first_dir = sys.argv[1]
    second_dir = sys.argv[2]

    copy(first_dir, second_dir)

if __name__ == "__main__":
    main()