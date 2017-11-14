import ast
import glob, os

os.chdir("C:/Users/User/Desktop/FIRE/Result/Result_3")
result_3 = (glob.glob("*.txt"))

os.chdir("C:/Users/User/Desktop/FIRE/Result/Result_4")
result_4 = (glob.glob("*.txt"))

for k in range(len(result_3)):
    print (k)
    
    os.chdir("C:/Users/User/Desktop/FIRE/Result/Result_3")
    fopen_1 = open(result_3[k], "r")

    os.chdir("C:/Users/User/Desktop/FIRE/Result/Result_4")
    fopen_2 = open(result_4[k], "r")

    os.chdir("C:/Users/User/Desktop/FIRE/Result/Result")
    fopen_3 = open(result_3[k], "w")

    data = []

    while 1:
        phrase = fopen_1.readline()
        if not phrase:
            break
        phrase = ast.literal_eval(phrase)
        data.append(phrase)

    while 1:
        phrase = fopen_2.readline()
        if not phrase:
            break
        phrase = ast.literal_eval(phrase)
        data.append(phrase)

    #data = list(set(data))
    data.sort(reverse=True)

    data_1 = []
    flag = 0
    for p in range(len(data)):
        we = data[p]
        flag = 0
        for q in range(len(data_1)):
            polo = data_1[q]
            if we == data_1[q] or we[0] == polo[0]:
            #if we == data_1[q]:
                flag = 1
        if flag == 0:
            data_1.append(data[p])
    
    for m in range(len(data_1)):
        fopen_3.write(str(data_1[m]) + "\n")

    fopen_3.close()
    fopen_2.close()
    fopen_1.close()
