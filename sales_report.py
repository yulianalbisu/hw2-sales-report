"""Generate sales report showing total melons each salesperson sold."""

#we need to store a list when looking for salespeople
salespeople = []
#the melons that have been sold 
melons_sold = []

#opening the file
f = open('sales-report.txt')

#iterating line to find out the f value
for line in f:
    line = line.rstrip() #remove space on the right
    entries = line.split('|') #separate each item in the line

    salesperson = entries[0] # creating a new item to store the first value
    melons = int(entries[2]) # creating melons to restore the second value of line
                             # its a number so it will be a integrer

    if salesperson in salespeople: #if the salesperson is in salespeople, store the value in:
        position = salespeople.index(salesperson) #from the salespeople we are taking the salesperson
                                   #store it in position

#how do we know this position index has to be in the position?

        melons_sold[position] += melons #looking for the position of the person who has sold the 
                                        #the melons 

    else: #if we dont find what we are looking for
        salespeople.append(salesperson) #if salesperson doesnt exist, add it to the salespeople
        melons_sold.append(melons) #add melons to melons sold?


for i in range(len(salespeople)): #please explain again
    
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
