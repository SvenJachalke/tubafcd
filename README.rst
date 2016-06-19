# -----------------------------------------------------
# --- tubafcd -- MANUAL -------------------------------
# -----------------------------------------------------

Author:		Sven Jachalke
Mail:		sven.jachalke@physik.tu-freiberg.de

# Installation

- fire up terminal
- navigate to tubafcd folder
- type: python setup.py install
- wait until installation finished

# TUBAFcolors:

- colors functions

	TUBAFred() = tubafred() ... red TUBAF color
	TUBAFblue() = tubafblue() ... blue TUBAF color
	TUBAFgree() = tubafgree() ... green TUBAF color
	TUBAForange() = tubaforange() ... orange TUBAF color
	TUBAFcyan() = tubafcyan() ... cyan TUBAF color
  --> returns RGB tuple
 
- color map
	TUBAFcmap(direction='regular')
	direction:	'regular','inverse'
	
				'regular' ... from blue to red
				'inverse' ... from red to blue
	
	call of TUBAFcmap() gives 'regular'!
  --> return colormap object for e.g. imshow, etc.
  
- importing module:
	
	from tubafcd import *
	--> just use TUBAFrot() -- returning color tuple
	
	import tubafcd
	--> tubafcd.TUBAFrot() 