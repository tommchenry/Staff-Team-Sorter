import random
def sortTeams(allStaff):
	'''
	Takes a list of all staff members and returns a list of staff
	sorted into randomized two-person teams.
	'''
	newTeams=[]
	staffCopy=allStaff
	for i in range(len(allStaff)):
	    selectedStaff=random.randrange(0, len(staffCopy))
	    newTeams.append(staffCopy[selectedStaff])
	    staffCopy.remove(staffCopy[selectedStaff])
	print newTeams 	

allStaff=['The Guy','The Girl','Paisley','Boo Radley']
sortTeams(allStaff)