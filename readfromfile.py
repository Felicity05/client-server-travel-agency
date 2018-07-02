from tabulate import tabulate
# # import re
# # from texttable import Texttable
# #
# # # def read():
# # #     with open("Flights.txt") as f:
# # #         output_str = ""
# # #
# # #         text = f.readlines()
# # #
# # #         new_text = [] #list to store each line of text
# # #         new_list = [] #list to store a list of each line of text
# # #         list_with_header = [] #to include the header in the list
# # #         list_with_header.insert(0, ['Flight', 'Seats', 'Price']) #add the header to the list
# # #         for i in range(len(text)):
# # #             new_text.insert(i, text[i].replace("\t", ",")) #in each line of text replace space by comma
# # #             sentences = new_text[i].split(",") #split each sentence with comma, return a list of items in each sentence
# # #             # words = sentences[i].split(",")
# # #
# # #             new_list.insert(i,sentences) #store in new_list each sentence list
# # #
# # #             # print(new_text[i])
# # #             # print(sentences)
# # #         # print("++++++++++++++++++++++++++++++++")
# # #
# # #         # print(new_text)
# # #
# # #
# # #             list_with_header.append(sentences) #append all the sentences to the list
# # #
# # #         #for debugging
# # #         print(new_list)
# # #         print(list_with_header)
# # #         print("\n=================================================")
# # #
# # #         #create text table object
# # #         # t = Texttable()
# # #         # t.add_rows(list_with_header) #add the list to be printed in table format
# # #
# # #         output_str = "These are all the flights that we have: \n" \
# # #                      +      tabulate(new_list, headers=['Flight', 'No.', 'Price'], tablefmt='orgtbl')
# # #         # draw the table              draw table with another format
# # #
# # #
# # #     return output_str
# #
# #
# # # print(read())
# # def read_file():
# #     with open("Flights.txt") as f:
# #         sentinel = True
# #
# #         text = f.readlines()  # read file line by line
# #
# #     return text
# #
# # list_from_file = read_file()
# #
# #
# #
# # def format_for_table():
# #
# #         new_text = []  # list to store each line of text
# #         new_list = []  # list to store a list of each line of text
# #
# #         for i in range(len(list_from_file)):
# #             new_text.insert(i, list_from_file[i].replace("\t", ","))  # in each line of text replace space by comma
# #             flightInfo = new_text[i].split(",")  # split each sentence with comma, return a list of items in each sentence
# #
# #
# #             new_list.insert(i, flightInfo)  # store in new_list each sentence list
# #
# #     # print("text: " + str(text))
# #     # print("new list: " + str(new_list))
# #
# #
# #         return new_list
# #     # else:
# #     #     return text
# #
# #
# #
# # print("====================================\n for text\n")
# #
# #
# # # print(list_from_file)
# #
# # # print(format_for_table())
# #
# #
# # # instr = "hi"
# #
# # # list = read_file(instr)
# #
# # # def this():
# # #     finald = []
# # #     info = []
# #
# #     # for i in range(len(list)):
# #     #
# #     #     if 'MIA' in list[i]:
# #     #         finald += [list[i]]
# #
# #     # print(finald)
# #
# #
# #     # for i in range(len(finald)): #goes fro each value of finald
# #     #
# #     #     info += [finald[i].split()] #split each value to get the adecuate format for the table
# #     #
# #     #     # print(info)
# #     #
# #     #     #print all the <-dest> in table format showing the number of seats and the price
# #     #     out = tabulate(info,headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl')
# #     #
# #     # return out
# #     #
# #
# # # print(list)
# #
# # # print(this())
# #
# #
# #
# # # print(output_str)
# # # print(list)
# #
# #
# # # inp = "buy_ticket ctu-dxb 75"
# # #
# # # words = inp.split()
# #
# # # for i in range(len(words)):
# #     # print(words[i])
# #
# # # sec_word = words[1].find("-") #return the index where the char is found -1 if not found
# # #
# # # flight = words[1].upper()
# # # seats = words[2]
# # #
# # # dep = flight.split("-")[0]
# # # arrv = flight.split("-")[1]
# # #
# # # entry = flight+"\t"+seats
# #
# # # print(entry)
# #
# #
# # # for i in range(len(list)):
# # #     if flight in list[i]:
# # #         # print(list[i])
# # #         break
# # #     # else:
# #     #     print(list[i])
# #
# #
# # # print(flight+seats+ "separated destinations: "+ dep + arrv)
# #
# # # while True:
# # #     seats = input("-> ")
# # #
# # #     if int(seats) <= int(total_seats):
# # #
# # #         temp = total_seats #temp variable to hold the total seats to replace them for the seats left
# # #         total_seats = int(total_seats) -  int(seats)  # seats left of the flight selected
# # #
# # #         out = str(seats) +"seats left: "+ str(total_seats)
# # #     else:
# # #         output_str = " Sorry the amount of seats that we have available is: " + str(total_seats)
# #
# # def list_with_format_for_table():
# #     new_text = []  # list to store each line of text
# #     new_list = []  # list to store a list of each line of text
# #
# #     for i in range(len(list_from_file)):
# #         new_text.insert(i, list_from_file[i].replace("\t", ","))  # in each line of text replace space by comma
# #         flightInfo = new_text[i].split(",")  # split each sentence with comma, return a list of items in each sentence
# #
# #         new_list.insert(i, flightInfo)  # store in new_list each sentence list
# #
# #     return new_list
# #
# # def read_file(fname):
# #     with open(fname) as f: #handles opening, reading and closing the file
# #         text = f.readlines()  # read file line by line
# #
# #     return text
# #
# # list_from_file = read_file("Flights.txt") #list of each line of the file
# #
# # flight = "las-jfk".upper()
# # flight1 = "mia-orl".upper()
# #
# # new_list = list_with_format_for_table()
# #
# #
# #
# # def is_flights_in_flights_sold(flight, return_flight):
# #     global flights_sold
# #
# #     centinel = False
# #
# #     for i in range(len(flights_sold)):
# #
# #         # print(flights_sold[i][0])
# #         if flight in flights_sold[i] or return_flight in flights_sold[i]:
# #
# #            return flights_sold[i]
# #
# #     return False
# #
# #
# #     # print(centinel)
# #     # if centinel:
# #     #     return True
# #
# #
# # # result = is_flights_in_flights_sold("LAS-JFK", "JFK-LAS")
# #
# # # if result == False:
# # #     print("ticket not here")
# # # else:
# # #     print(result)
# #
# # # print("LAS-JFK" in flights_sold[0])
# #
# # def valid_seats_to_return(seats_to_return, seats_that_can_be_returned, returning_flight):
# #
# #     server_message = ""
# #
# #     if int(seats_to_return) <= int(seats_that_can_be_returned):
# #
# #         # updates seats left to return in flights sold
# #         seats_that_can_be_returned = int(seats_that_can_be_returned) - int(seats_to_return)
# #
# #         # if there isn't more seats to return remove the flight from the list of flights sold
# #         if seats_that_can_be_returned == 0:
# #             flights_sold.remove(returning_flight)
# #
# #         return seats_to_return, seats_that_can_be_returned
# #
# #     return False
# #
# #     # # if the user try to return more seats tan the available to return or less than 0
# #     # else:
# #     #     server_message = " Sorry you cannot return more seats than the available to return.\n\n " \
# #     #                              "\t\t Seats that can be returned: " + str(available_seats) + "\n"
# #     #
# #     # return server_message
# #
# # #flight to return = entire flight = dep-dest seats price
# # def return_one_way_ticket(flight_to_return, seats_to_return):
# #
# #     for i in range(len(flights_sold)):
# #         if flight_to_return[0] in flights_sold[i]:
# #
# #             flights_sold[i][1] = flights_sold[i][1].replace(flights_sold[i][1], str(seats_to_return[1]))
# #
# #
# #         server_message = " What a shame to see you go... \n\n" \
# #                      " Congratulations you successfully return the ticket(s): \n\n" \
# #                      + tabulate([[flight_to_return[0]] + [str(seats_to_return[0])] + [flight_to_return[2]]],
# #                                 headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') \
# #                      + "\n\n Allow 5 business days to receive the money back to your card.\n" \
# #         # + str(available_seats_to_return) +" "+ str(flights_sold) +" "+ str(desired_flight_to_return)\
# #
# #     return server_message
# #
# # flights_sold = [['LAS-JFK', '40', '336\n'], ['MEX-HND', '40', '336\n']]
# #
# # result = valid_seats_to_return(seats_to_return=6, seats_that_can_be_returned=40, returning_flight="LAS-JFK, 40, 336")
# #
# # if result == False:
# #     server_message = " Sorry you cannot return more seats than the available to return.\n\n " \
# #                          "\t\t Seats that can be returned: " + "40" + "\n"
# # else:
# #     server_message = return_one_way_ticket(flights_sold[0], result)
# #
# #
# # print("original list: "+str(flights_sold))
# #
# # # print(flights_sold[0][1])
# #
# # print(server_message)
# #
# # print("list after returning: " +str(result[0]) + " tickets: "+ str(flights_sold))
# #
# # print("LAS-JFK" in flights_sold[0])
# #
# # # print(new_list)
# # # if str(result).isalpha():
# # #     print("error "+result)
# # # else:
# # #     print(return_one_way_ticket("LAS-JFK", result))
#
#
def read_file(fname):
    with open(fname) as f: #handles opening, reading and closing the file
        text = f.readlines()  # read file line by line

    return text

list_from_file = read_file("Flights.txt") #list of each line of the file to use in the list_with_format_for_table function
#
#returns a list of a list to be able to use the tabulate method to format the output as a table
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

new_list = list_with_format_for_table()[0]
#
# round_trip = list_with_format_for_table()[1]
#
#
# print(new_list)
#
#
# #shows a list of all the flights
# def list():
#      # list where each element is a list containing each flight info
#     server_message = " These are all the flights that we have: \n" + tabulate(new_list,
#               headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') + "\n"
#
#     return server_message
#
# print("CDG" in new_list[1][0])
#
# # print(list())
# print("\n==============================\n")
#
# dest = "SEA"
#
# def is_dest_in_list():
#
#     list_with_dest = []
#
#     # goes trough the list to find all the [dest]
#     for i in range(len(new_list)):
#
#         if dest in new_list[i][0]:
#             # print("hereeeeeeeeeee")
#             list_with_dest += [new_list[i]]  # saves a list containing the destination <dest>
#             # print(list_with_dest)
#
#     return list_with_dest
#
#
#     # return  False
#
# list = is_dest_in_list()
#
# # if not list:
# #     print(" Sorry we don't have that destination/departure. Try another one!" \
# #                "\n\n Type \"List\" to get a list of all the flights that we have.\n")
# # else:  #  if <dest> not in list
# #
# #     print(is_dest_in_list())
#
# #
# # def search_s(dest, all_dest):
# #
# #     dep_only = []
# #
# #     for i in range(len(all_dest)):  # goes for each value of the list with the specified dest
# #
# #         if all_dest[i][0].startswith(dest):
# #             dep_only += [all_dest[i]]  # save all the info of the destinations
# #
# #
# #     return dep_only
#
#
# # print(search_s(dest, list))
#
#
# # def buy_round_trip_ticket(flight, seats):
# #
# #     server_message = ""
# #     flights_sold = []
# #
# #     for i in range(len(new_list)):
# #     # search for the flight entered
# #         if flight in new_list[i]:
# #             flight_selected = new_list[i]  # saves all the information of the flight selected
# #             print(flight_selected)
# #
# #             total_seats = flight_selected[1] #original number of seats
# #
# #             if int(seats) <= int(total_seats) and int(seats) > 0:
# #                 temp = total_seats  # temp variable to hold the original total seats to replace them for the seats left
# #                 total_seats = int(total_seats) - int(seats)  # seats left of the flight selected
# #
# #                 print(i)
# #                 # updates the number of seats available for that flight
# #                 new_list[i][1] = new_list[i][1].replace(temp, str(total_seats))
# #                 new_list[i+1][1] = new_list[i+1][1].replace(temp, str(total_seats))
# #
# #                 flight_bought = [new_list[i]] + [new_list[i+1]]
# #                 print(flight_bought)
# #
# #                 # global flights_sold  # list to hold the flights that have been sold
# #
# #                 # add the flight bought to a list
# #                 flights_sold.append(flight_bought)
# #
# #                 print(flights_sold)
# #
# #                 server_message = " Congratulations you just bought a round trip ticket for: \n\n" \
# #                      + tabulate(flight_bought,
# #                                 headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') \
# #                      + "\n\n Price is per person per seats. We have left now " + str(total_seats) \
# #                      + " seats for each of that flights.\n\n Your confirmation number is: " \
# #                      # + ''.join(choices(string.ascii_uppercase + string.digits, k=7)) + "\n" \
# #                 break
# #             else:
# #                 if int(seats) < 0:
# #                     server_message = "at least buy 1 ticket"
# #                 else:
# #                     server_message = "cannot return more than the available seats to return: " + str(total_seats)
# #
# #
# #         else:
# #             server_message = "flight not in list"
# #
# #     return server_message
# #
# #
# # print(buy_round_trip_ticket("LAS-JFK", 26))
# #
# # print(new_list)
#
#         #
#         #
#         #
#         #     # flight selected with seats selected and price per seat
#         #     flight_bought = [flight] + [seats] + [price]
#         #     return_flight_bought = [return_flight] + [seats] + [price]  # generate return flight
#         #
#         #     # updates the number of seats available for that flight
#         #     new_list[i][1] = new_list[i][1].replace(temp, str(total_seats))
#         #
#         #     global flights_sold  # list to hold the flights that have been sold
#
# seats = 5
#
# flight_bought = ['LAS-JFK', '5', '336\n']
#
# one_way_flights_sold = []
#
# print(flight_bought[0])
#
# if not one_way_flights_sold: #list is empty
#     one_way_flights_sold.append(flight_bought)
#     print("added to list")
#     print(one_way_flights_sold)
#
#
# for j in range(len(one_way_flights_sold)):
#     if flight_bought[0] in one_way_flights_sold[j]:
#         print(one_way_flights_sold[j])
#         print("inside loop")
#         new = int(one_way_flights_sold[j][1]) + int(seats)
#         one_way_flights_sold[j][1] = new
#     break
#
# print(one_way_flights_sold)
#
#
round_trip_flights_sold = [[['LAS-JFK', '10', '336\n'], ['JFK-LAS', '10', '336\n']], [['MEX-HND', '10', '336\n'], ['HND-MEX', '10', '336\n']]]

print("HND-MEX" in round_trip_flights_sold[1][1])

def update_list_of_flights(desired_flight_to_return, seats_to_return):
    # updates the flight information in the list of flights

        for j in range(len(new_list)):
            if desired_flight_to_return in new_list[j]:
                # seats that the user is returning
                updated_seats_returned = int(new_list[j][1]) + int(seats_to_return)
                new_list[j][1] = new_list[j][1].replace(new_list[j][1], str(updated_seats_returned))
                new_list[j][1] = new_list[j][1].replace(new_list[j][1], str(updated_seats_returned))

                break

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

                    print(round_trip_flights_sold[i][0][1])
                    print(round_trip_flights_sold[i][1][1])

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
                                 + tabulate([one_ticket] + [ret_ticket],
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

        # new = int(one_way_flights_sold[i][1]) - int(seats_to_return[1])
        # one_way_flights_sold[i][1] = str(new)


    # server_message = str(one_way_flights_sold[j][1]) + " What a shame to see you go... \n\n" \
    #                  " Congratulations you successfully return the ticket(s): \n\n" \
    #                  + tabulate([[one_way_flights_sold[j][0]] + [str(seats_to_return[0])] + [flight_to_return[2]]],
    #                             headers=['Flight', 'Seats', 'Price'], tablefmt='orgtbl') \
    #                  + "\n\n Allow 5 business days to receive the money back to your card.\n" \
        # + str(available_seats_to_return) +" "+ str(flights_sold) +" "+ str(desired_flight_to_return)\

    # return server_message

print(return_round_trip_ticket('JFK-LAS', "5"))
print(new_list)