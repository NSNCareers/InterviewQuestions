import random

def PrintTicket(ticket): 
    lotteryNumbers = []
    rn = random.randint(0,100) 
    lotteryNumbers.append(rn)  
    while len(lotteryNumbers) < ticket:   
        for i in lotteryNumbers:
            if rn != i:
                lotteryNumbers.append(rn)
                if len(lotteryNumbers) == ticket:
                    print(lotteryNumbers)
                    break
            else:
                rn = random.randint(0,100) 
            

def PrintTicket1(num):
    lotto = []

    while num >= len(lotto):
        rn = random.randint(0,20)
        if rn not in lotto:
            lotto.append(rn)
    print(lotto)
             
PrintTicket1(5)


