import psutil

def DisplayProcess():
    print("List of Running process are : ")
    print("_______________________________")
    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)

    print("_________________________________")

def main():
    DisplayProcess()

if __name__ == "__main__":
    main()
