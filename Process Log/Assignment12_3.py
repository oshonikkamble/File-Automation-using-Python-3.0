import psutil
import sys
import os

def process_info():
    processes_info = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        processes_info.append(proc.info)
    return processes_info

def logfile(directory, processes_info):
    filepath = os.path.join(directory, 'ProcessLog.log')
    log_file = open(filepath, "w") 
    log_file.write("Process Information:\n")
    for info in processes_info:
        log_file.write(f"Name: {info['name']}, PID: {info['pid']}, Username: {info['username']}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: Application Name  Directory_name")
        sys.exit(1)

    directory_name = sys.argv[1]
    if not os.path.isdir(directory_name):
        print("Invalid directory path.")
        sys.exit(1)

    processes_info = process_info()
    if processes_info:
        logfile(directory_name, processes_info)
        print("Process information is Created in ProcessLog.log File in the directory.")
    else:
        print("No running processes found.")

if __name__ == "__main__":
    main()