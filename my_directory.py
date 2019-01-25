import os

my_folder = ''
Pr = 1

class dir_location():

    def __init__(self):
        self.me = my_folder
        self.pr = Pr

    def search(self):
        a = str(os.getcwd())
        a = a.split('\\')
        #print(a)
        b = len(a)
        c = str(a[0]) + str('\\')
        for x in range(1,b):
            c = c + str(a[x]) + str('\\')
        self.me = c
        if self.pr == 1:
            print(self.me)
            
    def go_to_folder(self,Where):
        a = self.me + str(Where) + str('\\')
        self.me = a
        if self.pr == 1:
            print(self.me)
            
    def go_to_file(self,Where):
        a = self.me + str(Where)
        self.me = a
        if self.pr == 1:
            print(self.me)
            
    def back(self,Nb=1):
        a = self.me.split('\\')
        #print(a)
        b = len(a)
        #print(b)
        b -= Nb
        #print(b)
        #print(Nb)
        c = str(a[0]) + str('\\')
        for x in range(1,(b-1)):
            c = c + str(a[x]) + str('\\')
        self.me = c
        if self.pr == 1:
            print(self.me)
            
    def log(self,W=0):
        self.pr = W
