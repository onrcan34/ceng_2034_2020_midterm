import os
import sys
import requests
import threading

url_list = ["https://api.github.com", "http://bilgisayar.mu.edu.tr", "https://www.python.org", "http://akrepnalan.com/ceng2034", "https://github.com/caesarsalad/wow"]


user = input("Which action would you like to take?\n1-Print PID\n2-Print LOADAVG\n3-Print '5 min loadavg' value and cpu core count\n4-Print the links\n5-Check the links valid or not.\n")
print("---------------------------------------------------")
if(user == "1"):
    print("PID is printing...")
    print(os.getpid()) 

elif(user == "2"):
    print("loadavg is printing...")
    print(os.getloadavg())
elif(user == "3"):
    print("'5 min loadavg' value and cpu core count are printing...")
    print(os.getloadavg()[1])

    loadavg = os.getloadavg()[1]
    cpuCount = os.cpu_count()

    if(cpuCount - loadavg < 1):
        print("Exitting...")
        sys.exit()

elif(user == "4"):
    print("The links are printing...")

    def requestSite(url):
        return requests.get(url).status_code

    for url in url_list:
        if(str(requestSite(url))[0] == "2"):
            print("This website 2xx", url)
        elif(str(requestSite(url))[0] == "4" or requestSite(url)[0] == "5"):
            print("This website  4xx or 5xx ", url)

else:
    print("The links are checking...")
    def requestSite(url):
        response = requests.get(url).status_code
        if(str(response)[0] == "2"):
            print("This url is working: ", url)
        elif(str(response)[0] == "4" or str(response)[0] == "5"):
            print("This url is not working ", url)


    for url in url_list:
        thread = threading.Thread(target=requestSite, args=(url,))
        thread.start()
        thread.join()
