# This script requires the dependency psutil
# to install use 'pip install psutil'
import psutil

def main():
    menuItems = {
        1: "Network Addresses",
        2: "CPU Usage",
        3: "Memory Usage",
        4: "Quit"
    }
    print("Welcome to the Python System Utilities Administrator. Please select an option: ")
    menuBreak = False
    while (menuBreak == False):
        for item in menuItems:
            print(item, ": ", menuItems[item])
        choice = input()
        if (int(choice) == 1):
            addrs = psutil.net_if_addrs().items()
            for i in addrs:
                print(i[0])
                print(i[1][1])
        elif (int(choice) == 2):
            print(psutil.cpu_percent(percpu=True), "(percent per core)")
        elif (int(choice) == 3):
            print(psutil.virtual_memory())
        else:
            menuBreak = True
        
        
           

if __name__ == "__main__":
    main()