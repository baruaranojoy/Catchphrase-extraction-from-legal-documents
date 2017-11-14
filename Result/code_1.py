import ast
import glob, os

os.chdir("C:/Users/User/Desktop/FIRE/Fire_2/Phrases")
all_file_name_phrases = (glob.glob("*.txt"))

os.chdir("C:/Users/User/Desktop/FIRE/Fire_2/Combine_Features_Result/3")
all_file_name_result = (glob.glob("*.txt"))


for k in range(len(all_file_name_phrases)):
    print (k)

    os.chdir("C:/Users/User/Desktop/FIRE/Fire_2/Phrases")
    fopen = open(all_file_name_phrases[k], "r")

    os.chdir("C:/Users/User/Desktop/FIRE/Fire_2/Combine_Features_Result/3")
    fopen2 = open(all_file_name_result[k], "r")

    os.chdir("C:/Users/User/Desktop/FIRE/Result/Result_3")
    fopen3 = open(all_file_name_phrases[k], "w")
    
    while 1:
        phrase = fopen.readline()
        if not phrase:
            break

        res = fopen2.readline()
        if not res:
            break
        
        res = ast.literal_eval(res)

        #if res == [0, 1]:
        if res[1] > res[0]:
            po = ''
            gama = phrase.split(' ')
            for q in range(len(gama)):
                po = po + gama[q]
            po = po[:len(po) - 1]
            #if po.isalpha():
            fopen3.write(str([res[1], phrase[:len(phrase) - 1]]) + "\n")

        
