# ******* 182 Days Tenor Function *****

def t182days():
    
    PRINCIPAL = float(input("Principal :: "))
    INTERESTRATE_PA = float(input("Rate (% Per Annum) :: "))
    CONTROL = '1'
    while CONTROL == '1':
        TERMs = (input("Terms(s) to Calculate (Estimate) :: \n \
                            1) 6 Months (182 days) \n \
                            2) 1 Year \n \
                            3) 2 or More Years \n"))
        
        if TERMs == '1':
            COUNTER = 1
            CONTROL =  '2'
            
        elif TERMs == '2':
            COUNTER = 2
            CONTROL =  '2'
            
        elif TERMs == '3':
            YEAR = int(input("Input Number of Years :: "))
            COUNTER = YEAR * 4
            CONTROL =  '2'
        else:
            print("Sorry , Invalid Selection - Enter an integer from 1 to 3 ")
            CONTROL =  '1'
            
    CONTROL2 = '1'
    while CONTROL2 == '1':
        RO_term = (input("Roll Over Terms :: \n \
                            1) Roll over Principal only \n \
                            2) Roll over Principal + Interest \n"))
        if RO_term == '1':
            RO = 1
            CONTROL2 = '2'
            
        elif RO_term =='2':
            RO = 2
            CONTROL2 = '2'
        else:
            print("Sorry , Invalid Selection - Enter an integer from 1 to 2 ")
            CONTROL2 =  '1'
        
    YIELD = PRINCIPAL
    R = (INTERESTRATE_PA / 100 ) / 2 
    RESULT = 0

    print("\n******** 182 Days Tenor *********")
    
    if RO == 1:
        for x in range(0, COUNTER):
            RESULT = (R * PRINCIPAL) + YIELD
            YIELD = RESULT

        print("*** ROLL-OVER PRINCIPAL ONLY *** ")
        print("********************************* \n")
        print(f"Maturity Value :: GHS {str(round(YIELD, 2))}")    
        print(f"Interest :: GHS {str(round(YIELD - PRINCIPAL, 2))}")

    elif RO == 2:
        for x in range(0, COUNTER):
            RESULT = (R * YIELD) + YIELD
            YIELD = RESULT

        print("*** ROLL-OVER PRINCIPAL + INTEREST *** \n")
        print("********************************* \n")
        print(f"Maturity Value :: GHS {str(round(RESULT, 2))}") 
        print(f"Interest :: GHS {str(round(RESULT - PRINCIPAL, 2))}")

    else:
        print("Invalid input")
