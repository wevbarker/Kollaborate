'''
Dear Colleague, this file has been generated automatically by my Maple program. It contains an expression in the python syntax.
Description of quantity: This is a function in r (perhaps better called x, since it can be negative?), and z, which encodes the density profile (perhaps in units derived from solar mass and kpc, with many powers of ten to make up the difference?). For some reason I can't seem to find the file name of the figure near this part in the script (or anywhere else), this will become a problem if the figures have historically been created by *clicking on things*, since it would suggest trawling the script and making comparisons manually. (An update: this came to pass. However, after some experimenting I'm reasonably confident that the plots have been reconstructed apart from an image that appears at the top of Fig. 5 in the current commit hash.)
'''
def provided_function(r,z):
	return .7161972438e-1*(.373*r**2+(.373+3*(z**2+.9e-1)**(1/2))*(.373+(z**2+.9e-1)**(1/2))**2)/(r**2+(.373+(z**2+.9e-1)**(1/2))**2)**(5/2)/(z**2+.9e-1)**(3/2)
