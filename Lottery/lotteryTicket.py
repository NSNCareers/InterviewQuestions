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
            
            
             
PrintTicket(5)


