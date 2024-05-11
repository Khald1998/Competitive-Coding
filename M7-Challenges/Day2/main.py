def distribute_data_oddly(dataNumber, peopleNumber):
    if dataNumber >= peopleNumber:
        share = [1] * peopleNumber
        dataRemaining = dataNumber - peopleNumber 
        
    
        index = 0
        while dataRemaining > 1:
            share[index] += 2
            dataRemaining -= 2
            index = (index + 1) % peopleNumber 
        share.append(dataRemaining)
    
        return share
    else:
        share = [0] * peopleNumber  
        for i in range(dataNumber):
            share[i] = 1  
        share.append(0)
        return share


print(distribute_data_oddly(3, 4))
