import random
operator = {0:'+', 1:'-', 2:'*', 3:'/'}

while(True):
    list = []
    sz = random.randint(1,100)
    list.append(str(sz))
    for i in range(random.randint(1, 3)):
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
    answer0 = float(input("输入你的答案："))
    if(answer0 == eval(string)):
        print("答案正确")
    else:
        print("答案错误，正确答案：")
        print(eval(string))
    break
