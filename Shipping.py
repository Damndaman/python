#******************************************************************************#
#                                                                              #
#                                                                              #
#               ██╗████████╗██████╗        ██╗ ██████╗  ██████╗                #
#               ██║╚══██╔══╝██╔══██╗      ███║██╔═████╗██╔═████╗               #
#               ██║   ██║   ██████╔╝█████╗╚██║██║██╔██║██║██╔██║               #
#               ██║   ██║   ██╔═══╝ ╚════╝ ██║████╔╝██║████╔╝██║               #
#               ██║   ██║   ██║            ██║╚██████╔╝╚██████╔╝               #
#               ╚═╝   ╚═╝   ╚═╝            ╚═╝ ╚═════╝  ╚═════╝                #
#******************************************************************************# 
#	ITP 100 - HW Assignment 3
#	Title: Shipping.py
#
#	Description: This program will determine the shipping costs based \
#	on a user supplied weight and show the shipping cost.
#

#	Varibles that hold price of shipping, changes to shipping costs should be\
#	updated here.
#	Cost per pound for each shipping category
FEATHERWEIGHT_COST   = float(1.50)
LIGHTWEIGHT_COST     = float(3.00)
MIDDLEWEIGHT_COST    = float(4.00)
HEAVYWEIGHT_COST     = float(4.75)
#	Maximum weight limit per shipping category
FEATHERWEIGHT       = int(2)
LIGHTWEIGHT         = int(6)
MIDDLEWEIGHT        = int(10)

# Ask user to input weight of package to be shipped
weight   = float(input('How much does the package weight?'))

# Determine the Costs of shipping based on wieth and category
if weight <= FEATHERWEIGHT:
	shippingCost = float(weight * FEATHERWEIGHT_COST)
elif weight <=LIGHTWEIGHT:
	shippingCost = float(weight * LIGHTWEIGHT_COST)
elif weight <=MIDDLEWEIGHT:
	shippingCost = float(weight * MIDDLEWEIGHT_COST)
else:
	shippingCost = float(weight * HEAVYWEIGHT_COST)
# Print the final cost to ship a package.
print ('Shipping for your package will be  $'+ format(shippingCost, '.2f'))
