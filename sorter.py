import random
def sortTeams(allStaff):
    '''
    Takes a list of all staff members and returns a list of staff
    sorted into randomized two-person teams.
    '''
    newTeams=[]
    staffCopy=list(allStaff)
    for i in range(len(allStaff)):
	selectedStaff=random.randrange(0, len(staffCopy))
	newTeams.append(staffCopy[selectedStaff])
	staffCopy.remove(staffCopy[selectedStaff])
    allStaff=newTeams
    displayList(allStaff)
	      
def displayList(sortedList):
    print 'Happy Halloween 2014!\nHere are this year\'s terrifying teamups:\n'
    for i in range(len(sortedList)):
        if (i+1)%2==0:
	   print 'Team', i/2+1, ':', sortedList[i-1], 'and', sortedList[i]
    if len(sortedList)%2!=0:
        print 'Team', len(sortedList)/2+1, ':', sortedList[-1]
    print '---------\n' 
	      	      
def createList():
    '''
    Takes user input to produce a list that can be passed to sortTeams()
    '''
    allStaff = []
    running = True 
    print 'Pumpkin Carving Team Creator 0.1'
    while running == True:
        if len(allStaff) > 0:
            print 'Current Roster:'
            for member in allStaff:
                print member
        command=raw_input('Enter a name to add them to the staff roster.\n(S to sort, R to reroll, X to exit): ')
        print command
        if command == 'X' or command == 'x':
            print 'Exiting.'
            running = False
        elif command == 'S' or command == 's':
            sortTeams(allStaff)
        elif command == 'R' or command == 'r':
            sortTeams(allStaff)    
        else:
            allStaff.append(command)
            print '---------\n'  
	    	
allStaff=['The Guy','The Girl','Paisley','Boo Radley','Tanjo', 'Tony', 'Alicia', 'A Dog']
createList()