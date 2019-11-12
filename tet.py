def fun(a,b,c,*d,**e):
    print(a,b,c,d)
    print(e['ho'])

ls = [1,2,3,4,5,4,46,8,3,31,5,51,46]
fun(*ls,ho = 45)