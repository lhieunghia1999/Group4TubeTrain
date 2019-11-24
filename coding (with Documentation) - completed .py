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
    
    def inquire(self):
        # Ask a user for the fromStation and toStation 
        # The program allows a user to make multiple inquiries
        fromStation = self.currentStation()
        toStation = self.desStation()

        # The route suggestion will be printed to the console
        route.routeSuggestion(fromStation, toStation)
        
        # Ask user if he/she wishes to make another inquiry    
        toContinue = input("Do you want to continue[y/n]? ")
        # letter 'y' is case-insensitive here
        if toContinue == 'y' or toContinue == 'Y' :
            self.inquire()            
            
    #Method prompts user to input their current location    
    def currentStation(self): 
        currStation = input("Which station are you in now? (Enter 'help' to view all the stations) \n")

        #print(currStation)
        if currStation == 'help':
            self.printRoute()
            return self.currentStation()
        if currStation == '':
            return self.currentStation()
        i = 1  
        current = self.head
                        
        if(self.head == None):    
            print("The route is empty!")    
            return    
                
        while(current != None):    
            if(current.data == currStation):    
                return i    
            current = current.west    
            i = i + 1 
        
        #Keeping prompting the user until a valid station name is entered
        print("\nThe station is not in the train route, please enter a valid station name:");
        return self.currentStation()

            
    #Method prompts user to input their destination         
    def desStation(self):   
        desStation = input("Which station do you want to go? (Enter 'help' to view all the stations, or Enter 'X' to quit the program): \n")

        #print(desStation)
        if desStation == 'help':
            self.printRoute()
            return self.desStation()
            
        if desStation == '':
            return self.desStation()
        j = 1    
        current = self.head
                        
        if(self.head == None):    
            print("The route is empty")    
            return    
                
        while(current != None):    
            if current.data == desStation:    
                return j   
            current = current.west    
            j = j + 1    
        
        #Keeping prompting the user until a valid station name is entered
        print("\nThe station is not in the train route, please enter a valid station name:")
        return self.desStation()    
        
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
            print('\nYou\'re already at your destination.')

#Allows code to run as a standalone program
#instead of through application            
if __name__ == "__main__":
    # Initialize a train route
    route = TrainRoute()

    # Add all the stations along the route 
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
    
    route.inquire()




