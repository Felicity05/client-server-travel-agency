'''
Server program for the Travel Agency Happy Travel
@author: Arelys Alvarez
'''

from socket import * #to be able tu use sockets
from _thread import * #to be able to handle task in separate threads
import threading
import sys #to e able to use system commands
import traceback #to be able to print the errors
from tabulate import tabulate #to print output in table format
from random import *
import string

'''
Clients will be able to do the following in the server

# LIST (will list all flight) 

SEARCHD DEST (it will search destination such as SEARCH MIA), this will search the destination *-MIA

SEARCHALL DEST (it will search information about round-trip for example, 
SEARCHALL ORL will display ORL-MIA 40 seats left at 400 each and MIA-ORL 38 seats left at 400 each). 

SEARCHS DEPARTURE (for example, SEARCHDEPARTURE ORL will search any departure that starts with ORL) 

BUY_TICKET [where] [seats] (For example BUY_TICKET MIA-ORL 40)

BUYRT_TICKET [where] [seats) (Here buys round trip)

RETURN_TICKET [where] [seats]

RETURNRT_TICKET [where] [seats] 
'''

print_lock = threading.Lock()

# REMENBER TO BLOCK THE THREADS FIRST
# thread the client to process each request in a different thread
def threaded_client(conn, buff_size=4096):  # size in bits of the response

    # all the data that we receive we have to decode and all the data that we send we have to encode
    while True:
        data_from_client = conn.recv(buff_size).decode('utf-8').lower()

        # exits the loop if no data
        if not data_from_client:
            break

        #if client wants to disconnect
        if data_from_client == "disconnect":
            print("Client disconnected from server")

        # if data is received, process it and save the output to server_answer
        server_answer = client_input_processing(data_from_client)

        # send the resulting response to the client
        try:
            conn.sendall(server_answer.encode())  # encoding = 'utf-8'
        except:
            traceback.print_exc()

    conn.close()  # close connection


#create and start the server
def start_server():

    # server info
    host = ''
    port = 10000
    activeConn = 1

    sock = socket(AF_INET, SOCK_STREAM) #socket created
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #for easy start/kill the app

    #binding process
    try:
        sock.bind((gethostbyname(host), port))  #socket bounded
    except error as e:
        print("Binding failed." + str(e)) #print error and exit the app
        sys.exit()

    #start listening on socket
    sock.listen(activeConn) #number of active connections

    #socket is ready
    print("\nServer ip: "+ gethostbyname(host)+" listening on port: " + str(port))

    #infinite loop to not reset the server for every client
    while True:
        conn, addr = sock.accept() #stablishing connection
        ipAddr, cPort = str(addr[0]), str(addr[1])
        print("\nClient connected from " + ipAddr + ": " + cPort)

        try:
            my_thread = threading.Thread(target=threaded_client, args=(conn,))  # creates a thread
            my_thread.start()  # starts the thread


            print(threading.active_count())
            print(threading.enumerate())
            print(threading.current_thread())
            print(my_thread.is_alive())

        except:
            traceback.print_exc()

# reads from the file and return a list containing each line of the file
def read_file(fname):
    with open(fname) as f:  # handles opening, reading and closing the file
        text = f.readlines()  # read file line by line

    return text

list_from_file = read_file("Flights.txt")  # list of each line of the file to use in the list_with_format_for_table function


#returns a list of a list to be able to use the tabulate method to format the output as a table
#also returns a dictionary where the key is a unique value(1...) and the value is the par [[oneway], [returntrip]]
def list_with_format_for_table():

    new_text = []  # list to store each line of text
    round_trips = []  # list to store a list of round trips
    round_trip = {}

    for i in range(len(list_from_file)):
        new_text.insert(i, list_from_file[i].replace("\t", ","))  # in each line of text replace space by comma
        flightInfo = new_text[i].split(",")  # split each sentence with comma, return a list of items in each sentence

        dep  = flightInfo[0].split("-")[0]
        arrv = flightInfo[0].split("-")[1]
        seats = flightInfo[1]
        price = flightInfo[2]

        one_way = flightInfo
        return_trip = [arrv+"-"+dep] + [seats] + [price]

        # list to save the round trips
        round_trips += [one_way] + [return_trip]

        round_trip[i+1] = [one_way] + [return_trip]

    # print(round_trip)

    return round_trips, round_trip

new_list = list_with_format_for_table()[0] #list

pair_tickets = list_with_format_for_table()[1] #dictionary


#handles all processing of the input received from the client
def client_input_processing(input_str):
    print_lock.acquire() #locks the current thread until it finishes doing what it's doing

    try:

        #displays useful commands
        if input_str == "help":
            output_str = help()

        #display all of the flights to the client
        elif input_str == 'list':
            output_str = list()

        elif input_str == "pair_tickets":
            output_str = str(pair_tickets)

        #handles search options
        elif input_str.startswith('search'):

            output_str = search(input_str)


        #handles buy ticket option
        elif input_str.startswith('buy'):

            info_flight_entered = input_str.split()

            output_str = buy_ticket(info_flight_entered)


        #handles return tickets
        elif input_str.startswith("return"):

            # ticket_to_return = input_str.split()

            global flights_sold

            # output_str = "we don't have these flights any more: " + str(flights_sold_out)

            output_str = return_ticket(input_str)

        # #displays a list of the flights that the user has bought
        elif input_str == "show_my_tickets":

            output_str = my_tickets()

        # any other input
        else:
            output_str = " Invalid request\n"

    finally:
        print_lock.release() #relase the lock so the other thread can be executed

    return output_str


#shows a list of the available options
def help():
    server_message = "List --> list of all the flights\n" \
                     "SearchS <dep> --> search information about departure <dep>\n" \
                     "SearchD <dest> --> search information about destination <dest>\n" \
                     "Search_all <dest> --> search information about round-trip containing <dest>\n" \
                     "Buy_ticket <where> <seat> --> buy one way ticket\n" \
                     "BuyRT_ticket <where> <seat> --> buy round trip ticket\n" \
                     "Show_my_tickets --> displays the tickets bought\n" \
                     "Return_ticket <where> <seat> --> return one way ticket bought\n" \
                     "Returnrt_ticket <where> <seat> --> return round trip ticket bought\n" \

    return server_message

#shows a list of all the flights
def list():
     # list where each element is a list containing each flight info
    server_message = " These are all the flights that we have: \n" + tabulate(new_list,
              headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') + "\n"

    return server_message

#validates input for correct format and valid number of seats
def input_validation(command):

    server_message = ""

    if len(command) < 3:
        server_message = " Incorrect format for " + command[0] + ". Enter all the information in the format: " \
                         "\n\n\t <dep-dest> <seats>\n"
        if len(command) == 2:
            server_message = " You need to enter how many seats you want to return. " \
                             "Enter all the information and try again!\n"
    else:
        flight = command[1].upper()  # flight dep-arr

        if flight.find("-") == -1:  # if the separator character is incorrect
            server_message = " Incorrect flight format! Enter all the information in the format: " \
                             "\n\n\t <dep-dest> <seats> use Airport code for departure and destination\n"

        else:
            dep = flight.split("-")[0]
            arrv = flight.split("-")[1]

            if len(dep) != 3 or len(arrv) != 3:
                server_message = " Use 3 characters Airport code for departure and destination.\n"

            elif not (command[2].isdigit()):
                server_message = " Invalid number of seats.\n"

            elif int(command[2]) <= 0:
                server_message = " Sorry you need to " + command[0].split("_")[0] + " at least 1 seat.\n"

            elif command[2].startswith("0"):
                server_message = " Invalid number of seats.\n"


    return server_message

# search all the round trip containing dest
def is_dest_in_list(dest):

    list_with_dest = [] #list to hold all the dep-dest/dest-dep flights info

    # goes trough the list to find all the [dest]
    for i in range(len(new_list)):

        if dest in new_list[i][0]:
            list_with_dest += [new_list[i]]  # saves a list containing all the flights with the destination <dest>

    return list_with_dest

# search all the flights with destination dest
def search_dest(desti, list_dest):

    dest_only = [] #list to hold all the -dest flights info

    for i in range(len(list_dest)):  # goes for each value of the list with the specified -dest

        if "-" + desti in list_dest[i][0]:
            dest_only += [list_dest[i]]  # save all the info of the destinations

    return dest_only

# search all the flights with departure dep
def search_dep(destination, all_destinations):

    dep_only = [] #list to hold all the dep flights info

    for i in range(len(all_destinations)):  # goes for each value of the list with the specified dest

        if all_destinations[i][0].startswith(destination):
            dep_only += [all_destinations[i]]  # save all the info of the destinations


    return dep_only

#handles all the search options
def search(input_str):

    server_message = ""

    search_dest = input_str.split()

    # if the client only enters search
    if len(search_dest) == 1:
        server_message = " You need to enter destination or departure. \n\n Popular destinations are: MIA, LAS, ATL, DEN, LGW...\n"

    elif len(search_dest) > 2:
        server_message = " You can only enter destination or departure but not both.\n"

    else:

        # get the destination from the user input and convert it to uppercase
        dest = search_dest[1].upper()

        # handling ignore case input
        search_criteria = search_dest[0].lower()
        search_all = "search_all".lower()  # search roundtrip
        search_f = "searchD".lower()  # search destination
        search_s = "searchS".lower()  # search departure

        if search_criteria == search_all or search_criteria == search_f or search_criteria == search_s:

            # check for invalid destination
            if len(dest) != 3:
                server_message = " That's not a valid destination. Enter the Airport code and try again!\n"
            else:

                list_all_dest = is_dest_in_list(dest)

                #if the dest or dep looking for is not in the list
                if not list_all_dest:
                    server_message = " Sorry we don't have that destination/departure. Try another one!" \
                                    "\n\n Type \"List\" to get a list of all the flights that we have.\n"

                else:
                    # search all the round trip containing dest
                    if search_criteria == search_all:

                        server_message = "These are the round trip flights for your search: " + dest + "\n" \
                                     + tabulate(list_all_dest, headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') + "\n"


                    # search all the flights with destination dest
                    elif search_criteria == search_f:

                        dest_only = []  # list to hold all the -dest flights info

                        for i in range(len(list_all_dest)):  # goes for each value of the list with the specified -dest

                            if "-" + dest in list_all_dest[i][0]:
                                dest_only += [list_all_dest[i]]  # save all the info of the destinations

                        # print all the -<dest> in table format showing the number of seats and the price
                        server_message = " These are the flights for the destination: " + dest + "\n" \
                                             + tabulate(dest_only, headers=['Flight', 'Seats', 'Price'],
                                                        tablefmt='orgtbl') + "\n"

                    # search all the flight with departures dep
                    elif search_criteria == search_s:

                        dep_only = []  # list to hold all the dep flights info

                        for i in range(len(list_all_dest)):  # goes for each value of the list with the specified dest

                            if list_all_dest[i][0].startswith(dest):
                                dep_only += [list_all_dest[i]]  # save all the info of the destinations


                        # print all the <dept> in table format showing the number of seats and the price
                        server_message = " These are the flights for the departure: " + dest + "\n" \
                                             + tabulate(dep_only, headers=['Flight', 'Seats', 'Price'],
                                                        tablefmt='orgtbl') + "\n"

        else:  # checks for incorrect format of search
            server_message = " Invalid format for searching.\n\n Try searchD <dest>, search_all <dest>, " \
                         "searchS <dep>\n"


    return server_message

#global variable that keeps track of the flights sold
one_way_flights_sold = []

round_trip_flights_sold = []

def buy_one_way_ticket(flight, seats):

    server_message = ""

    for i in range(len(new_list)):
    # search for the flight entered
        if flight in new_list[i]:
            flight_selected = new_list[i]  # saves all the information of the flight selected
            # print(flight_selected)

            total_seats = flight_selected[1] #original number of seats

            if int(seats) <= int(total_seats) and int(seats) > 0:
                temp = total_seats  # temp variable to hold the original total seats to replace them for the seats left
                total_seats = int(total_seats) - int(seats)  # seats left of the flight selected

                # updates the number of seats available for that flight
                new_list[i][1] = new_list[i][1].replace(temp, str(total_seats))

                flight_bought = [flight_selected[0]] + [seats] + [flight_selected[2]]

                # global one_way_flights_sold  # list to hold the flights that have been sold

                # add the flight bought to a list
                if not one_way_flights_sold:  # list is empty
                    one_way_flights_sold.append(flight_bought)
                    # print("added to list")
                    # print(one_way_flights_sold)
                else:
                    for j in range(len(one_way_flights_sold)):
                        if flight_bought[0] in one_way_flights_sold[j]:
                            # print(one_way_flights_sold[j])
                            # print("inside loop")
                            new = int(one_way_flights_sold[j][1]) + int(seats)
                            one_way_flights_sold[j][1] = new
                        break

                server_message = " Congratulations you just bought a ticket for: \n\n" \
                     + tabulate([flight_bought], headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') \
                     + "\n\n Price is per person per seats. We have left now " + str(total_seats) \
                     + " seats for each of that flights.\n\n Your confirmation number is: " \
                     + ''.join(choices(string.ascii_uppercase + string.digits, k=7)) + "\n"
                break
            else:
                if int(seats) <= 0:
                    server_message = " You need to at least buy 1 ticket.\n"
                    break
                else:
                    if int(total_seats) == 0:
                        server_message = " Sorry we don't have more seats for that flight.\n "
                        break
                    else:
                        server_message = " Sorry you cannot buy more seats than the ones we have available.\n\n " \
                                         "\t\t The amount of seats that we have available is: " + str(total_seats) + "\n"
                        break
        else:
            server_message = " Sorry we don't have that flight. Try another one!\n"

    return server_message

def buy_round_trip_ticket(flight, seats):

    server_message = ""

    for i in range(len(new_list)):
    # search for the flight entered
        if flight in new_list[i]:
            flight_selected = new_list[i]  # saves all the information of the flight selected
            return_f = new_list[i+1]
            # print(flight_selected)

            total_seats = flight_selected[1] #original number of seats
            retrun_total_seats = return_f[1]

            if int(seats) <= int(total_seats) and int(seats) > 0:
                temp = total_seats  # temp variable to hold the original total seats to replace them for the seats left
                temp1 = retrun_total_seats
                total_seats = int(total_seats) - int(seats)  # seats left of the flight selected
                retrun_total_seats = int(retrun_total_seats) - int(seats)

                # print(i)
                # updates the number of seats available for that flight
                new_list[i][1] = new_list[i][1].replace(temp, str(total_seats))
                new_list[i+1][1] = new_list[i+1][1].replace(temp1, str(retrun_total_seats))

                one_way = [flight_selected[0]] + [seats] + [flight_selected[2]]
                return_flight = [return_f[0]] + [seats] + [return_f[2]]

                flight_bought = [one_way] + [return_flight]
                # print(flight_bought)

                # global flights_sold  # list to hold the flights that have been sold

                # add the flight bought to a list
                round_trip_flights_sold.append(flight_bought)

                # print(flights_sold)

                server_message = " Congratulations you just bought a round trip ticket for: \n\n" \
                     + tabulate(flight_bought, headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') \
                     + "\n\n Price is per person per seats. We have left now " + str(total_seats) \
                     + " seats for each of that flights.\n\n Your confirmation number is: " \
                     + ''.join(choices(string.ascii_uppercase + string.digits, k=7)) + "\n"
                break
            else:
                if int(seats) <= 0:
                    server_message = " You need to at least buy 1 ticket.\n"
                    break
                else:
                    if int(total_seats) == 0:
                        server_message = " Sorry we don't have more seats for that flight.\n "
                        break
                    else:
                        server_message = " Sorry you cannot buy more seats than the ones we have available. " \
                                         "\n\n The amount of seats that we have available is: " + str(total_seats) + "\n"
                        break
        else:
            server_message = " Sorry we don't have that flight. Try another one!\n"

    return server_message

#handles buying ticket options
def buy_ticket(info_flight_entered):

    if info_flight_entered[0] == "buyrt_ticket" or info_flight_entered[0] == "buy_ticket":

        if len(info_flight_entered) < 3:
            server_message = " Which ticket you would like to buy? Enter all the information in the format: " \
                         "\n\n\t <dep-dest> <seats>\n"
            if len(info_flight_entered) == 2:
                server_message = " You need to enter how many seats you would like to buy. " \
                             "Enter all the information and try again!\n"

        else:  # if the info for the flight entered is correct

            # input entered by the user
            flight = info_flight_entered[1].upper()
            seats = info_flight_entered[2]

            if flight.find("-") == -1:  # if the separator character is incorrect
                server_message = " Incorrect flight format! Enter all the information in the format: " \
                             "\n\n\t <dep-dest> <seats> use Airport code for departure and destination\n"
            else:
                dep = flight.split("-")[0]
                arrv = flight.split("-")[1]

                if len(dep) != 3 or len(arrv) != 3:
                    server_message = " Use 3 characters Airport code for departure and destination.\n"
                else:  # flight format correct

                    if info_flight_entered[0] == "buy_ticket":

                        server_message = buy_one_way_ticket(flight, seats)

                    else: #buyRT_ticket

                        server_message = buy_round_trip_ticket(flight, seats)



    else:
        server_message = " Invalid format for buying a ticket.\n\n Try buy_ticket <dep-dest> <seats> or " \
                     "buyRT_ticket <dep-dest> <seats> \n"

    return server_message


def update_list_of_flights(desired_flight_to_return, seats_to_return):
    # updates the flight information in the list of flights

        for j in range(len(new_list)):
            if desired_flight_to_return in new_list[j]:
                # seats that the user is returning
                updated_seats_returned = int(new_list[j][1]) + int(seats_to_return)
                new_list[j][1] = new_list[j][1].replace(new_list[j][1], str(updated_seats_returned))

                break


#checks if the flight to return is in the list of flights sold
# def find_flight_in_flights_sold(flight, return_flight):
#     global flights_sold
#
#     for i in range(len(one_way_flights_sold)):
#
#         if flight in one_way_flights_sold[i][0] or return_flight in one_way_flights_sold[i][0]:
#
#             return one_way_flights_sold[i]
#             break
#
#     return False

#check for the validity of the number of seats
def valid_seats_to_return(seats_to_return, seats_that_can_be_returned, returning_flight):

    if int(seats_to_return) <= int(seats_that_can_be_returned):

        # updates seats left to return in flights sold
        seats_that_can_be_returned = int(seats_that_can_be_returned) - int(seats_to_return)

        # if there isn't more seats to return remove the flight from the list of flights sold
        if seats_that_can_be_returned == 0:
            one_way_flights_sold.remove(returning_flight)

        return seats_to_return, seats_that_can_be_returned

    return False

#returns one way ticket
#flight to return = entire flight = dep-dest seats price
def return_one_way_ticket(flight_to_return, seats_to_return):

    if not one_way_flights_sold:
        server_message = "You cannot return a ticket that hasn't been sold"
    else:
        print("no")
        for i in range(len(one_way_flights_sold)):
            if flight_to_return in one_way_flights_sold[i]:
                flight_found = one_way_flights_sold[i]
                # print(one_way_flights_sold[i])
                available_seats_to_return = flight_found[1]

                if int(seats_to_return) <= int(available_seats_to_return) and int(seats_to_return) > 0:

                    one_way_flights_sold[i][1] = int(one_way_flights_sold[i][1]) - int(seats_to_return)
                    # print(one_way_flights_sold[i])
                    # print("inside loop")

                    # once the returning tickets has been processed update the number of seats in the list of flights
                    update_list_of_flights(flight_to_return, seats_to_return)

                    server_message = " What a shame to see you go... \n\n" \
                                 " Congratulations you successfully return the ticket(s): \n\n" \
                                 + tabulate([[flight_found[0]] + [str(seats_to_return)] + [flight_found[2]]],
                                            headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') \
                                 + "\n\n Allow 5 business days to receive the money back to your card.\n" \
                    # + str(available_seats_to_return) +" "+ str(flights_sold) +" "+ str(desired_flight_to_return)\
                    break
                else:
                    if int(seats_to_return) <= 0:
                        server_message = " You need to at least buy 1 ticket.\n"
                        break
                    else:
                        if int(seats_to_return) == 0:
                            server_message = " Sorry you cannot return more seats for that flight.\n "
                            break
                        else:
                            server_message = " Sorry you cannot return more seats than the ones we have available.\n\n " \
                                         "\t\t The amount of seats that we have available is: " \
                                             + str(available_seats_to_return) + "\n"
                            break
            else:
                server_message = " Sorry we don't have the flight you are trying to return.\n"
                break



    return server_message

#flight to return = entire flight = dep-dest seats price
def return_round_trip_ticket(flight_to_return, seats_to_return):

    server_message = ""

    if not round_trip_flights_sold :
        server_message = "You cannot return a ticket that hasn't been sold"
    else:
        print("no")
        for i in range(len(round_trip_flights_sold)):
            if flight_to_return in round_trip_flights_sold[i][0] or flight_to_return in round_trip_flights_sold[i][1] :
                flight_found = round_trip_flights_sold[i][0]
                return_flight_found = round_trip_flights_sold[i][1]
                # print(flight_found + return_flight_found)
                available_seats_to_return = flight_found[1]
                # print(available_seats_to_return)
                # print("------")

                if int(seats_to_return) <= int(available_seats_to_return) and int(seats_to_return) > 0:

                    #updating number of seats
                    round_trip_flights_sold[i][0][1] = int(round_trip_flights_sold[i][0][1]) - int(seats_to_return)
                    round_trip_flights_sold[i][1][1] = int(round_trip_flights_sold[i][1][1]) - int(seats_to_return)

                    # print(round_trip_flights_sold[i][0][1])
                    # print(round_trip_flights_sold[i][1][1])

                    # once the returning tickets has been processed update the number of seats in the list of flights
                    for j in range(len(new_list)):
                        if flight_to_return in new_list[j]:
                            if flight_to_return == flight_found[0]:
                                # seats that the user is returning
                                updated_seats_returned = int(new_list[j][1]) + int(seats_to_return)
                                new_list[j][1] = new_list[j][1].replace(new_list[j][1], str(updated_seats_returned))
                                new_list[j+1][1] = new_list[j+1][1].replace(new_list[j+1][1], str(updated_seats_returned))
                                break
                            elif flight_to_return == return_flight_found[0]:
                                updated_seats_returned = int(new_list[j][1]) + int(seats_to_return)
                                new_list[j][1] = new_list[j][1].replace(new_list[j][1], str(updated_seats_returned))
                                new_list[j - 1][1] = new_list[j - 1][1].replace(new_list[j - 1][1], str(updated_seats_returned))
                                break

                    one_ticket = [flight_found[0]] + [str(seats_to_return)] + [flight_found[2]]
                    ret_ticket = [return_flight_found[0]] + [str(seats_to_return)] + [return_flight_found[2]]

                    server_message = " What a shame to see you go... \n\n" \
                                 " Congratulations you successfully return the ticket(s): \n\n" \
                                 + tabulate([one_ticket] + [ret_ticket], headers=['Flight', 'Seats', 'Price'],
                                            tablefmt='orgtbl') \
                                 + "\n\n Allow 5 business days to receive the money back to your card.\n" \
                    # + str(available_seats_to_return) +" "+ str(flights_sold) +" "+ str(desired_flight_to_return)\
                    break
                else:
                    if int(seats_to_return) <= 0:
                        server_message = " You need to at least buy 1 ticket.\n"
                        break
                    else:
                        if int(seats_to_return) == 0:
                            server_message = " Sorry you cannot return more seats for that flight.\n "
                            break
                        else:
                            server_message = " Sorry you cannot return more seats than the ones we have available.\n\n " \
                                         "\t\t The amount of seats that we have available is: " \
                                             + str(available_seats_to_return) + "\n"
                            break
            else:
                server_message = " Sorry we don't have the flight you are trying to return.\n"
                break



    return server_message

        # new = int(one_way_flights_sold[i][1]) - int(seats_to_return[1])
        # one_way_flights_sold[i][1] = str(new)


    # server_message = str(one_way_flights_sold[j][1]) + " What a shame to see you go... \n\n" \
    #                  " Congratulations you successfully return the ticket(s): \n\n" \
    #                  + tabulate([[one_way_flights_sold[j][0]] + [str(seats_to_return[0])] + [flight_to_return[2]]],
    #                             headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') \
    #                  + "\n\n Allow 5 business days to receive the money back to your card.\n" \
        # + str(available_seats_to_return) +" "+ str(flights_sold) +" "+ str(desired_flight_to_return)\

    # return server_message

#handles returning a ticket
def return_ticket(input_str):

    command = input_str.split() #split the user input to get the command, flight and seats

    if command[0] == "returnrt_ticket" or command[0] == "return_ticket":

        server_message = input_validation(command) #validate the input to let pass only the correct format

        if not server_message: # flight format correct

            flight_to_return = command[1].upper()
            seats_to_return = command[2]

            # process return_ticket
            if command[0] == "return_ticket":

                server_message = return_one_way_ticket(flight_to_return, seats_to_return)

            # process returnRT_ticket
            else:
                server_message = return_round_trip_ticket(flight_to_return, seats_to_return)

    else:
        server_message = command[0] + " Invalid format for returning a ticket.\n\n " \
                         "Try return_ticket <dep-dest> <seats> or returnRT_ticket <dep-dest> <seats> \n"

    return server_message

#displays all the flights that have been bought
def my_tickets():

    server_message = ""

    if not round_trip_flights_sold and not one_way_flights_sold:
        server_message = " There's no tickets to show yet.\n"
    else:

        server_message = " These are the tickets that you have bought:\n\n\t" + str(one_way_flights_sold)  \
                            + str(round_trip_flights_sold) + "\n\n\t\t" + "Price is per person per seat.\n"

    return server_message






def main():
    start_server()




#allows to run the Python files either as reusable modules or standalone programs
if __name__ == "__main__":
    main()
