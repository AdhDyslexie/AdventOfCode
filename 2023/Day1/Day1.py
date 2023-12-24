# for i in range(10):
#     print('loop:', i)
#     for x in range(10):
#         print('Second Loop:', x)

import itertools

with open("Text.txt", mode = 'r') as file:
    test = file.readlines()

   
    Tempvalue = []
    for x in itertools.islice(test,5):

        TempList = []
        TempList.append(x)

        for y in TempList:
            print(TempList[0])
            if(y.isnumeric() == True):

                print("Y is: ", y)
                # listlen = len(y) - 1
                # NewString = y[0] + "" + y[listlen]
                # Value = int(NewString)
        
        #print(TempList)
        TempList.pop()
                

    print(Tempvalue)


# Check if the string in the index has any numerical charcters
# if true, get the first & last numerical charcters & put them togather in a string
# Cast string to int
# Repet for every line
# Take all numbers & add them all together
                

    # Removing Anything thats not a number

    # Tempvalue = []
    # for x in itertools.islice(test,5):
    #     for y in x:
    #         if(not y.isnumeric()):
    #             TmpStr = y
    #             test.remove(TmpStr)

    #     Tempvalue.append(y)

    # print(Tempvalue)


    # Adding any numbers to a new list

    # Tempvalue = []
    # for x in itertools.islice(test,5):
    #     print(x)
    #     for y in x:
    #         if(y.isnumeric() == True):
    #             Tempvalue.append(y)
                
    # listlen = len(y) - 1
    # NewString = y[0] + "" + y[listlen]
    # FinalValue = int(NewString)
