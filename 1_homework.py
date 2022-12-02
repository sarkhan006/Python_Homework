""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 
#Пример: - 6 -> да - 7 -> да - 1 -> нет  """

#def InputNumbers(inputText):
#    is_OK = False
#    while not is_OK:
#        try:
#            number = int(input(f"{inputText}"))
#            is_OK = True
#        except ValueError:
#            print("Это не число!")
#    return number
#def checkNumber(num):
#    if 6 <= num <= 7:
#        print("Yes")
#    elif 0 < num < 6:
#       print("No")
#    else:
#        print("число вне пределов 7 дней")


#num = InputNumbers("Введите число: ")
#checkNumber(num)



#""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """


#def inputNumbers(x):
#    xyz = ["X", "Y", "Z"]
#    a = []
#    for i in range(x):
#        a.append(input(f"Введите значение {xyz[i]}: "))
#    return a


#def checkPredicate(x):
#    left = not (x[0] or x[1] or x[2])
#    right = not x[0] and not x[1] and not x[2]
#    result = left == right
#    return result


#statement = inputNumbers(3)

#if checkPredicate(statement) == True:
#    print(f"Утверждение истинно")
#else:
#    print(f"Утверждение ложно")
