import os
import glob
import ast

os.chdir("C:/Users/User/Desktop/FIRE/Result/Result")
all_file_name = (glob.glob("*.txt"))

os.chdir("C:/Users/User/Desktop/FIRE/Result")
fopen_res = open("Result.txt", "w")


for k in range(len(all_file_name)):
    print (k)
    flag = 0
    
    os.chdir("C:/Users/User/Desktop/FIRE/Result/Result")
    fopen = open(all_file_name[k], "r")

    data = ""
    data = data + "FIRE_2017_SR_4" + "||"
    data = data + all_file_name[k] + "||"
    
    while 1:
        phrase = fopen.readline()
        if not phrase:
            break
        phrase = ast.literal_eval(phrase)
        #phrase = phrase[:len(phrase) - 1]
        data = data + str(phrase[1]) + ":" + str(phrase[0]) + ","
        flag = 1

    if flag == 1:
        data = data[:len(data) - 1]

    fopen_res.write(data + "\n")

    

    
