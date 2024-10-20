import os
import shutil
import sys

def copy_extension(first_dir, second_dir, ext):

    if not os.path.exists(second_dir):
        os.makedirs(second_dir)
        print(f"Created directory: {second_dir}")

    files = os.listdir(first_dir)
   
    for file in files:
        if file.endswith(ext):
            first_path = os.path.join(first_dir, file)
            second_path = os.path.join(second_dir, file)
            shutil.copy2(first_path, second_path)
            print(f"Copied {file} to {second_dir}")

def main():
    
    if len(sys.argv) != 4:
        print("Usage: python script.py <source_directory> <destination_directory> <extension>")
        sys.exit(1)

    first_dir = sys.argv[1]
    second_dir = sys.argv[2]
    ext = sys.argv[3]

    copy_extension(first_dir, second_dir, ext)

if __name__ == "__main__":
    main()