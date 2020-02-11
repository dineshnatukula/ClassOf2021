import sys
hrs = mns = sec = spd = res = 0
eTime = sTime = tmpSpd = 0
for line in sys.stdin:
    l = line.split(":")
    hrs = int(l[0])
    mns = int(l[1])
    l2 = l[2].split(" ")
    spd = 0
    if len(l2) == 2:
        sec = int(l2[0])
        spd = int(l2[1])
    else:
        sec = int(l[2])
    # print (mns, mns/60)
    # print (hrs , " ::: " , mns%60 , " ::: " , sec%60)
    etime = hrs + (mns/60) + (sec/3600)
    print (spd)
    if spd == 0:
        res = res + (eTime - sTime) * tmpSpd
        print (line, res,  " km")
    else:
        res = res + (eTime - sTime) * tmpSpd
        print("here...", tmpSpd, res)
    sTime = eTime
    if len(l2) == 2:
        tmpSpd = spd