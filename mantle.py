from collections import Counter
import re
from os import path


def reportLog(file):
    
    # Check if file exists
    if path.exists(file) == False:
        print("Please enter valid path to file on line 52")
        exit()
    
    # Setup Counter objects
    ipcnt = Counter()
    urlcnt = Counter()
    
    # Setup regex statements
    ipre = re.compile(r'^(?P<ip>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) - ')
    urlre = re.compile(r"(?P<url>(?<=GET\s)(.*?)(?=\sHTTP))")

    # Loop through each line in log file
    with open(file) as infile:
        
        # Check each line
        for line in infile:

            # Check for matching ip and url on each line
            m = ipre.match(line)
            n = urlre.search(line)
            
            # Iterate Counter objects
            if m is not None and n is not None:
                ip = m.groupdict()['ip']
                ipcnt[ip] += 1
                url = n.groupdict()['url']
                urlcnt[url] += 1
    
    # Print Report
    print("\n Number of Unique IPs: ", len(ipcnt), "\n",
          "\n",
          "Top 3 most active IPs:",
          "\n IP:",'\n IP: '.join(['  Count: '.join([str(cell) for cell in row]) for row in ipcnt.most_common(3)]), "\n"
          "\n",
          "Top 3 most visited URLs:",
          "\n URL:",'\n URL: '.join(['  Count: '.join([str(cell) for cell in row]) for row in urlcnt.most_common(3)]), "\n")


if __name__ == "__main__":
    
    # Please change the folder path below
    folder = r"C:\Users\Ruhaab Sheikh\Desktop\Mantle Group"
    
    # Uncomment any test case you would like to run below
    
    # Original log file
    # file = folder + "\programming-task-example-data.log"
    
    # Test Case 1: Log file with less than 3 logs
    # file = folder + "\Test Case 1.log"
    
    # Test Case 2: Log file with 1000 logs
    file = folder + "\Test Case 2.log"
    
    reportLog(file)
    
