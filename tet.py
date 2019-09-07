s = input()
n = int(s[0])
m = int(s[2])
q = int(s[4])
l = []
for i in range(n):
    l = l + [input()]
for j in range(q):
    a = input()
    if int(a[0])==2:
        ret = 0
      #  print(l)
        for i in l:
            ret = ret + i.count("1")
        print(ret)
    else:
        x = 0
        y = 0
        if a[2] == '-':
            x = -int(a[3])
            if a[5] == '-':
                y == -int(a[6])
            else:
                y == int(a[5])
        else:
           # print("h1")
            x = int(a[2])
            if a[4] == '-':
               # print("h2")
                y = -int(a[5])
               # print("h3",y)
               # print("h4",int(a[5]))
            else:
                y == int(a[4])
                
        print(x,y);
        if x>0:
            for i in range(n):
                l[i] = (l[i]+("0"*x))[-m:]
        if x<0:
            x = -x
            for i in range(n):
                l[i] = (("0"*x)+l[i])[:m]
        if y>0:
            l = (l+(["0000"]*y))[-n:]
        if y<0:
            y = -y
            l = ((["0000"]*y)+l)[:n]
