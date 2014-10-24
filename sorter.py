import random
def sortTeams(allStaff):
	'''
	Takes a list of all staff members and returns a list of staff
	sorted into randomized two-person teams.
	'''
	newTeams=[]
	staffCopy=allStaff
	print 'Happy Halloween 2014!\nHere are this year\'s terrifying teamups:\n'
	for i in range(len(allStaff)):
	    selectedStaff=random.randrange(0, len(staffCopy))
	    newTeams.append(staffCopy[selectedStaff])
	    staffCopy.remove(staffCopy[selectedStaff])
            if (i+1)%2==0:
	      print 'Team', i/2+1, ':', newTeams[i-1], 'and', newTeams[i]
	    	
allStaff=['The Guy','The Girl','Paisley','Boo Radley']
sortTeams(allStaff)