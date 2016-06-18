#-------------------------------
#TUBAF CD colors
#-------------------------------

def TUBAFblue():
	"""
	Tuple for TUBAF CD blue color 
	"""
	return (0/255.,100/255.,168/255.)
	
def TUBAFred():
	"""
	Tuple for TUBAF CD red color 
	"""
	return (181/255.,18/255.,62/255.)
def TUBAFgreen():
	"""
	Tuple for TUBAF CD green color 
	"""
	return (25/255.,150/255.,43/255.)
def TUBAForange():
	"""
	Tuple for TUBAF CD orange color 
	"""
	return (244/255.,134/255.,3/255.)
def TUBAFcyan():
	"""
	Tuple for TUBAF CD cyan color 
	"""
	return (35/255.,186/255.,226/255.)


def TUBAFcmap(direction='regular'):
	"""
	Generates color map, e.g. for imshow
	"""
	import matplotlib as mpl
	
	if direction == 'regular':
		TUBAFcmap = mpl.colors.LinearSegmentedColormap.from_list('own',[TUBAFblue(),TUBAFcyan(),TUBAFgreen(),TUBAForange(),TUBAFred()])
	elif direction == 'inverse':
		TUBAFcmap = mpl.colors.LinearSegmentedColormap.from_list('own',[TUBAFred(),TUBAForange(),TUBAFgreen(),TUBAFcyan(),TUBAFblue()])	
	
	return TUBAFcmap
	
#Version of Colors
TUBAFCDversion='2013'