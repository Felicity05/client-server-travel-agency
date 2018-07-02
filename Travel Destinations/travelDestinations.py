'''
Program to randomly generate a list fo Flights every time it's run
@author: Arelys Alvarez
'''
from random import *
from collections import Counter

#process the file with the codes of the airports and store them in a dictionary
def process_file(fname):
    lineCode = {} #creates an empty dictionary

    with open(fname) as f: #Handles files operations in this case reading the file
        for line in f:
            if ("#" not in line): #ignore lines that start with '#'
                # print(line)
                words_in_linetext = line.split()  #split the line of text to get independent words

                lineNumber = words_in_linetext[0] #get the first word of line of text
                # print("line number: " + lineNum[0])

                airCode = words_in_linetext[1] #get the second word of the line of text
                # print("airport code: " + lineNum[1])

                lineCode[lineNumber] = airCode  #add the key and values to the dictionary

        return lineCode

dicLineCode = process_file("airportCodes") #dictionary with the codes of the airport

#debugging purposes
# print(lineCode.keys())
# print(lineCode.values())
#print all the values of the dictionary
#for k, v in lineCode.items():
    # print(k +" "+v)

#create 50 different round trips flights
def create_flights():

    flights = []

    for i in range(50):
        #generate a random number between 1 and 50
        deparFrom = randint(1, 50)

        # print(deparFrom)
        # read from file airpot codes and get the code of that line
        if(str(deparFrom) in dicLineCode):
            From = dicLineCode.get(str(deparFrom)) #get the value of that key


        #check if arrvTo is different from deparFrom
        while(True):
            arrvTo = randint(1,50) #generate a random number between 1 and 50
            if(deparFrom != arrvTo):
                break

        # print(arrvTo)
        #get that code form the file airpot codes
        if (str(arrvTo) in dicLineCode):
            To = dicLineCode.get(str(arrvTo))  # get the value of that key

             # print(arrv)


        flight = From + "-" + To
        if flight not in flights:
            flights.append(flight)

        number_of_flights = Counter(flights)

    # print(number_of_flights)

    return flights

def write_flights():
    fileWrite = open('Flights.txt', 'w')  # write to a file

    flights = create_flights()

    for i in range(len(flights)):
        flight = flights[i].split("-")

        From = flight[0]
        To = flight[1]

        # print(From)
        # print(To)

        # get the flight number and the price
        available_seats = randint(20, 75)  # generate random number for the number of seats of the flight
        price = randint(50, 1000)  # generate a random number for the price of the flight

        # print(price)
        # print(available_seats)

        # write to a file the flights info to form the flights
        fileWrite.write(From + "-" + To + "\t" + str(available_seats) + "\t" + str(price) + "\n")
        # fileWrite.write(To + "-" + From + "\t" + str(available_seats) + "\t" + str(price) + "\n")

    fileWrite.close()  # closes the fle after we are done working with it



try:
    write_flights()
    print("correct lenght: " + str(len(create_flights())))
    print("\nFile with flights successfully created.")
except:
    print("Something went wrong when creating the flights.")




