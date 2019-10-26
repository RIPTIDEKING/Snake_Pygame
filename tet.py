class t:
    def __init__(self, ls):
        self.ls = ls
        self.ls[1] = 5

ls = [0,1]
tt = t(ls)
print(ls)