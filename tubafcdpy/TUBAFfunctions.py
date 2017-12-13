from tubafcdpy.TUBAFcolors import *

def TUBAFblue():
	"""
	Tuple for TUBAF CD blue color 
	"""
	return colorblue

def tubafblue():
	return TUBAFblue()

def TUBAFred():
	"""
	Tuple for TUBAF CD red color 
	"""
	return colorred

def tubafred():
	return TUBAFred()
	
def TUBAFgreen():
	"""
	Tuple for TUBAF CD green color 
	"""
	return colorgreen
	
def tubafgreen():
	return TUBAFgreen()
	
def TUBAForange():
	"""
	Tuple for TUBAF CD orange color 
	"""
	return colororange

def tubaforange():
	return TUBAForange()
	
def TUBAFcyan():
	"""
	Tuple for TUBAF CD cyan color 
	"""
	return colorcyan

def tubafcyan():
	return TUBAFcyan()

def TUBAFcmap(direction='regular'):
	"""
	Generates color map, e.g. for imshow
	"""
	import matplotlib as mpl
	from matplotlib.cm import register_cmap
	
	if direction == 'regular':
		TUBAFcmap = mpl.colors.LinearSegmentedColormap.from_list('own',[TUBAFblue(),TUBAFcyan(),TUBAFgreen(),TUBAForange(),TUBAFred()])
	elif direction == 'inverse':
		TUBAFcmap = mpl.colors.LinearSegmentedColormap.from_list('own',[TUBAFred(),TUBAForange(),TUBAFgreen(),TUBAFcyan(),TUBAFblue()])	
	
	mpl.cm.register_cmap(name='TUBAF',cmap=TUBAFcmap)
	return TUBAFcmap

def tubafcmap(direction='regular'):
	return TUBAFcmap()
	
#Version of Colors
TUBAFCDversion='2013'