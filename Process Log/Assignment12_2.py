import psutil
import os
import sys

def Process(proc_name):
    for proc in psutil.process_iter(['pid','name','username']):
        if proc.info['name'] == proc_name:
            return proc.info
    pass

def main():
    if len(sys.argv) != 2:
        print("usage : Application_name  proc_name")
        sys.exit(1)

    proc_name = sys.argv[1]
    proc_info = Process(proc_name)

    if proc_info:
        print("Process Name : ",proc_info['name'])
        print("PID : ",proc_info['pid'])
    else:
        print("Process Is Not Running",proc_name)

if __name__ == "__main__":
    main()