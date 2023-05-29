import time

def inputIntList():
    """拓展-获取输入并形成列表，并转换为int类型列表"""
    Shuru = input().split()  # 获取输入并形成列表
    for i in range(len(Shuru)):
        Shuru[i] = int(Shuru[i])
    return Shuru



def ChaRuPaiXu(Shuru):
    """插入排序"""

    string = str(Shuru) + '\n'
    for M_I in range(1,len(Shuru)):
        key = Shuru[M_I]
        L_I = M_I - 1

        while L_I >= 0 and Shuru[L_I] > key:
            Shuru[L_I + 1] = Shuru[L_I]
            L_I = L_I - 1

        Shuru[L_I + 1] = key
        time.sleep(1)

        string += str(Shuru) + '\n'
    print(string)


    return Shuru



if __name__ == '__main__':
    Shuru = ChaRuPaiXu([5, 2, 4, 6, 1, 3])
