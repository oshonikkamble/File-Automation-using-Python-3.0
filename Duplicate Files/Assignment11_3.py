import os
import hashlib
import sys

def findduplicates(directory):   
    hash_dict = {}

    duplicate_files = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            f = open(file_path, 'rb') 
            file_hash = hashlib.md5(f.read()).hexdigest()

            f.close()

            if file_hash in hash_dict:
                duplicate_files.append(file_path)
            else:
                hash_dict[file_hash] = file_path

    log_file = open('log.txt', 'w') 
    log_file.write("Duplicate files deleted:\n")
    for file in duplicate_files:
            log_file.write(file + '\n')
            os.remove(file)
            print(f"Deleted: {file}")

    print("Duplicates deleted and logged in log.txt.")

def main():

    if len(sys.argv) != 2:
        print("Usage: Application Name   directory")
        sys.exit(1)

    directory = sys.argv[1]

    findduplicates(directory)

if __name__ == "__main__":
     main()