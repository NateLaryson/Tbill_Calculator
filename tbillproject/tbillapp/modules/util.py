# ******* 91 Days Tenor Function *****

def t91days(principal, rate_pa, terms, years):

    YIELD = principal
    R = (rate_pa / 100 ) / 4
    RESULT = 0
    
    if years == 0:
        counter = 1
    else:
        counter = years * 4
 
    if terms == 'PO':
        for x in range(0, counter):
            RESULT = (R * principal) + YIELD
            YIELD = RESULT
            
        return YIELD
            
    else:
        for x in range(0, counter):
            RESULT = (R * YIELD) + YIELD
            YIELD = RESULT
            
        return YIELD


# ******* 182 Days Tenor Function *****

def t182days(principal, rate_pa, terms, years):

    YIELD = principal
    R = (rate_pa / 100 ) / 2
    RESULT = 0
    
    if years == 0:
        counter = 1
    else:
        counter = years * 2
 
    if terms == 'PO':
        for x in range(0, counter):
            RESULT = (R * principal) + YIELD
            YIELD = RESULT
            
        return YIELD
            
    else:
        for x in range(0, counter):
            RESULT = (R * YIELD) + YIELD
            YIELD = RESULT
            
        return YIELD


# ******* 365 Days Tenor Function *****

def t365days(principal, rate_pa, terms, years):

    YIELD = principal
    R = rate_pa / 100
    RESULT = 0
    
    if years == 0:
        counter = 1
    else:
        counter = years
 
    if terms == 'PO':
        for x in range(0, counter):
            RESULT = (R * principal) + YIELD
            YIELD = RESULT
            
        return YIELD
            
    else:
        for x in range(0, counter):
            RESULT = (R * YIELD) + YIELD
            YIELD = RESULT
            
        return YIELD


