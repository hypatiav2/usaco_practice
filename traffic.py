# Problem: Traffic
n = int(input())
traffic = (0,0)
sections = []
consecutive = False
for m in range(n):
    sections.append(input().split())
for s in sections[n::-1]:
    ma = max(int(s[1]),int(s[2]))
    mi = min(int(s[1]),int(s[2]))
    if "off" in s:
        traffic = (traffic[0]+mi,traffic[1]+ma)
    elif "on" in s:
        traffic = (traffic[0]-ma,traffic[1]-mi)
    elif "none" in s:
        if consecutive == True:
            traffic = (max(int(s[1]),traffic[0]),min(int(s[2]),traffic[1]))
        else: traffic = (int(s[1]),int(s[2]))
        consecutive = True
if traffic[0] < 0:
    traffic = (0,traffic[1])
if traffic[1] < 0:
    traffic = (traffic[0],0)
print(str(traffic[0]) + " " + str(traffic[1]))

consecutive = False
traffic = (0,0)
temp =(0,0)
for s in sections:
    ma = max(int(s[1]),int(s[2]))
    mi = min(int(s[1]),int(s[2]))
    if "off" in s:
        traffic = (traffic[0]-ma,traffic[1]-mi)
    elif "on" in s:
        traffic = (traffic[0]+mi,traffic[1]+ma)
    elif "none" in s:
        if consecutive == True:
            traffic = (max(int(s[1]),traffic[0]),min(int(s[2]),traffic[1]))
        else: traffic = (int(s[1]),int(s[2]))
        consecutive = True
if traffic[0] < 0:
    traffic = (0,traffic[1])
if traffic[1] < 0:
    traffic = (traffic[0],0)
print(str(traffic[0]) + " " + str(traffic[1]))

    

