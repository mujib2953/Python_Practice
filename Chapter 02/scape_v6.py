# -*- coding: utf-8 -*-
# @Author: Mujib
# @Date:   2017-07-15 16:47:13
# @Last Modified by:   Mujib
# @Last Modified time: 2017-07-15 16:53:29

# Implmenting function
import urllib.request
import time

normalCustomer = 'http://beans-r-us.appspot.com/prices.html'
loyalCustomer = 'http://www.beans-r-us.appspot.com/prices-loyalty.html'

price = 99.99;

def getPrice():
	page = urllib.request.urlopen( normalCustomer )

	text = page.read().decode( 'utf8' )

	# Here + 2 is added since we have to eliminate the character >$
	priceIndex = text.find( '>$' ) + 2; 

	# Here + 4 is since the total 4 character 
	price = float( text[ priceIndex:( priceIndex + 4 ) ] )

	return ( price )
	

while price > 4.74:

	# Sleep of 15 minute.
	time.sleep( 10 )
	price = getPrice()
	print( "The price for the coffee is : " + str( price ) )

print( 'Price is low you can buy.' )