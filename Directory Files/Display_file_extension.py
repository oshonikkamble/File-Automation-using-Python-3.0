import os
import sys

def display(directory, ext):   
    files = os.listdir(directory)
        
    files_with_extension = [file for file in files if file.endswith(ext)]
    
    if files_with_extension:
        print(f"Files with extension '{ext}' in directory '{directory}':")
        for file in files_with_extension:
            print(file)
    else:
        print(f"No files with extension '{ext}' found in directory '{directory}'.")

def main():
        
    if len(sys.argv) != 3:
        print("This Scrpit Use Three Arguments, directory  extention ")
        sys.exit(1)
    
    directory = sys.argv[1]
    ext = sys.argv[2]
        
    display(directory, ext)

if __name__ == "__main__":
    main()
