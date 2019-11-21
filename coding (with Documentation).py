#Creating Node class for doubly linked list
class DNode():
    def __init__(self, data, west=None, east=None):
        self.data = data
        self.west = west   
        self.east = east  

class TrainRoute:
    def __init__(self):
        self.head = None
        self.tail = None
        #Record all the station names on this route
        self.stations = []


    #Method adds stations to the queue
    def add(self,station):
        if self.head == None: 
            self.head = station
            self.tail = station
            self.head.west = self.tail
            self.tail.east = self.head
        else:
            self.tail.west = station
            station.east = self.tail
            self.tail = station
        self.stations.append(station.data)


    #Method lists all stations available for user to take
    def printRoute(self):
        print('------------------------------------------------')
        print('---'.join(self.stations))
        print('------------------------------------------------')


    #Method prompts user to input their current location
    def currentStation(self): 
        currStation = input("Which station are you in now? (Enter 'help' to view all the stations, or Enter 'X' to quit the program): \n")

        #print(currStation)
        if currStation == 'help':
            self.printRoute()
            self.currentStation()

        #Statement allows user to end program at current location input
        if currStation == 'X' or currStation == 'x':
            return -1
        if currStation == '':
            self.currentStation()
        i = 1  
        flag = False   
        current = self.head

        #Method checks if the queue is empty
        if(self.head == None):    
            print("The route is empty!")    
            return    
                
        while(current != None):    
            if(current.data == currStation):    
                flag = True    
                break    
            current = current.west    
            i = i + 1 


        #This 'If' statement checks if the input is a existing starting location
        if(flag):    
            #print("\nYou're currently at station No. " + str(i));
            return i;
        else:    
            print("\nThe station is not in the train route. Please enter a valid station name: ");
            #Prompt the user for a valid station name
            self.currentStation()

            
    #Method prompts user to input their destination
    def desStation(self):   
        desStation = input("Which station do you want to go? (Enter 'help' to view all the stations, or Enter 'X' to quit the program): \n")

        #print(desStation)
        if desStation == 'help':
            self.printRoute()
            self.desStation()

        #Statement allows user to end program at destination input
        if desStation == 'X' or desStation == 'x':
            return -1
            
        if desStation == '':
            self.desStation()
        j = 1    
        flag = False   
        current = self.head

        #Method checks if the queue is empty
        if(self.head == None):    
            print("The route is empty")    
            return    
                
        while(current != None):    
            if current.data == desStation:    
                flag = True    
                break    
            current = current.west    
            j = j + 1    


        #This 'If' statement checks if the input is a existing destination within the route
        if flag:    
            #print("\nYou're going to station No. " + str(j)) 
            return j 
        else:    
            print("\nThe station is not in the train route. Please enter a valid station name: ")
            #Prompt the user for a valid station name
            self.desStation()    
        

    #Method tells user which train to take and
    #how many stations they will skip before arriving at their destination
    #If user is already at location, then program will notify user
    #they have are already at their destination
    def routeSuggestion(self, fromStation, toStation):
        if fromStation > toStation:
            print('\nGo by West Bound Train, skip {} stations and get off at Station {}.'.format(fromStation - toStation - 1, fromStation - toStation))
        elif fromStation < toStation:
            print('\nGo by East Bound Train, skip {} stations and get off at Station {}.'.format(toStation - fromStation - 1, toStation - fromStation))
        else:
            print('\nYou are already at your destination.')


#Allows code to run as a standalone program
#instead of through application
if __name__ == "__main__":
    
    #Initialize a train route
    route = TrainRoute()

    
    #Add all the stations along the route 
    route.add(DNode('Ealing Broadway'))
    route.add(DNode('West Acton'))
    route.add(DNode('North Acton'))
    route.add(DNode('East Acton'))
    route.add(DNode('White City'))
    route.add(DNode('Shepherds Bush'))
    route.add(DNode('Holland Park'))
    route.add(DNode('Notting Hill Gate'))
    route.add(DNode('Queensway'))
    route.add(DNode('Lancaster'))
    route.add(DNode('Marble Arch'))
    route.add(DNode('Bond Street'))
    route.add(DNode('Oxford Circus'))
    route.add(DNode('Tottenham Court Road'))
    route.add(DNode('Holborn'))
    route.add(DNode('Chancery Lane'))
    route.add(DNode('St Pauls'))
    route.add(DNode('Bank'))
    route.add(DNode('Liverpool Street'))
    route.add(DNode('Bethnal Green'))
    route.add(DNode('Mile End'))


    #Prompt a user for the current station and the destination
    #The program allows a user to make multiple inquiries
    #Method allows user to end program by entering 'X'
    while True:
        fromStation = route.currentStation()
        if fromStation == -1:
            break;
        toStation = route.desStation()
        if toStation == -1:
            break;
        #The route suggestion will be printed to the console
        if fromStation != None and toStation != None:
            route.routeSuggestion(fromStation, toStation)

