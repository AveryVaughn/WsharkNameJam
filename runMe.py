# cheap and dirty script to generate that endlessly long wireshark filter
# make sure you get the basic concept of what the filters are looking for 
# or this is easy mode
# keep circulating the tapes
def dumpOutString(s):
    sUsed1 = f"{s[0]}".strip()
    thisCounter = 1
    thisUpperLimit = len(s) 
    while thisCounter <= thisUpperLimit - 1 :
        sUsed1 += s[thisCounter].strip() + " "
        thisCounter += 1
        
    return sUsed1


fileToUse = open("ip_ranges.txt", 'r')
theseIps = fileToUse.readlines()
firstipString = f"ip.src == {theseIps[0]} "
ipList = []
ipList.insert(0, firstipString)
counter = 1
upperLimit = len(theseIps) 
while counter < upperLimit:
    toAdd = f"or ip.src == {theseIps[counter]}"
    ipList.append(toAdd)
    counter += 1


bigTime = dumpOutString(ipList)
print(bigTime)



