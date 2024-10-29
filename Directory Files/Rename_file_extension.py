import os
import sys

def renamefiles(directory, ext1, ext2):
    files = os.listdir(directory)    
    
    for filename in files:        
        if filename.endswith(ext1):            
            new_filename = filename[:-len(ext1)] + ext2
            
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

def main():

    if len(sys.argv) != 4 :
        print("This Script is executed by command line argument")
        sys.exit()           

    directory = sys.argv[1]
    ext1 = sys.argv[2]
    ext2 = sys.argv[3]

    renamefiles(directory, ext1, ext2)
if __name__ == "__main__":
    main()
