from module1 import t91days
from module2 import t182days
from module3 import t365days

CONTROL = '2'
while CONTROL == '2':
    T = (input("Please select tenor \n \
                    1) 91 days \n \
                    2) 182 days \n \
                    3) 365 days \n \
                    4) Exit Application \n "))
    if T == '1':
        t91days()
        CONTROL = '1'
    elif T == '2':
        t182days()
        CONTROL = '1'
    elif T == '3':
        t365days() 
        CONTROL = '1'
    elif T == '4':
        break    
    else:
        print("Invalid Entry")       

    print("\n************************************** \n")
    
    CONTROL = (input('Exit Application? \n \
                        1) Yes \
                        2) No \n'))
    
    print("\n************************************** \n")
