def checkBigRect(rectInfo,rAx,rAy):
    for element in rectInfo:
        if (element[0]+element[2]) > rAx >= element[0]:
            if (element[1]+element[3]) > rAy >= element[1]:
                return True
        print(element[0]+element[2],element[0])
        print(element[1]+element[3],element[1])
    return False

rectInfo = [[0,40,1000,20],[0,60,20,540],[980,60,20,540],[20,580,960,20]]
rAx = 0
rAy = 320
print(checkBigRect(rectInfo,rAx,rAy))