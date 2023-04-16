#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Faulty calculator$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# #

dictionary = {"45*3" : "555" , "56 + 9" : "77" , "56 / 6" : "4"}
i = 0
while i < 1:
    
    print("                              HII.. 'SARANSH GUPTA' WELCOMES YOU IN EXAMINATION CALCULATOR. ")

    
    a = input("(1) +   For Addition \n(2) -   For Substration\n(3) *  For Multiplication\n(4) /   For Division\n(5) **  For Powering\nChoose your operation symbol:- ")
    if a != "+" and a != "-" and a != "*" and a != "/" and a != "**":
        print("OOPS! you entered invalid key \n Try Again!!")
        break
    l = input("enter your first no. :- ")
    
    if l.isnumeric():
        l = int(l)
    
        j = input("enter your second no. :- ")

        if j.isnumeric():
            j = int(j)   

            if a == "+":
                if l == 56 and j == 9:
                    print(dictionary["56 + 9"])
                else:
                    print(l+j)

            elif a == "-":
                print(l-j)

            elif a == "*":
                if l == 45 and j == 3:
                    print(dictionary["45*3"])
                else:
                    print(l*j)
            
            elif a == "**":
                print(l**j)

            else:
                if l == 56 and j == 6:
                    print(dictionary["56 / 6"])
                else:
                    print(l/j)

    
            print("so you want to calculate again ")
            k = input("If yes type \"y\" else type \"n\" :-  ")
            if k == "y":
                continue 
            else:
                break































