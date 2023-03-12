import time

def sum(i):
    start = time.time()
    res = 0
    if 0 < i < 10 ** 25:
        for n in range(0, i + 1):
            res += n
        print(res)
        end = (time.time() - start)
        if end < 0.1:
            print("Task completed")
        else:
            print("Fail")
    else:
        print("Num is out of range")

exit = False
while exit == False:
    num = input("Enter the num")
    if num == '':
        exit = True
        print("Finishing the program")
    else:
        sum(int(num))