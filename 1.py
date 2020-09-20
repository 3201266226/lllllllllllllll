import random
operator = {0:'+', 1:'-', 2:'*', 3:'/'}

while(True):
    list = []
    sz = random.randint(1,100)
    list.append(str(sz))
    for i in range(random.randint(1, 10)):
        sz = random.randint(0,100)
        op = random.randint(0, 3)
        if op  == 3 and sz == 0:
            sz = random.randint(1, 100)
        list.append(operator[op])
        list.append(str(sz))
        string = ''.join(list)
    if(eval(string) <= 0):
        continue
    print(string)
    print(eval(string))
    break
