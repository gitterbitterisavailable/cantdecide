from random import *
weightdef = ["smoke","biking","swimming","games","drive"]
weights = [25,20,20,20,20]    
def pick():
    r = choices(weightdef,weights=weights,k=1)
    print(r)


for i in range(0,100):
    pick()
    

