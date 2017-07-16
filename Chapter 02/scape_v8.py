# -*- coding: utf-8 -*-
# @Author: Mujib
# @Date:   2017-07-15 17:24:42
# @Last Modified by:   Mujib
# @Last Modified time: 2017-07-16 13:57:17

# Implmenting Twitter messaging
import urllib.request
import time

normalCustomer = 'http://beans-r-us.appspot.com/prices.html'
loyalCustomer = 'http://www.beans-r-us.appspot.com/prices-loyalty.html'

# http://forums.oreilly.com/topic/20756-sending-messages-to-twitter/

def getPrice():
	page = urllib.request.urlopen( normalCustomer )

	text = page.read().decode( 'utf8' )

	# Here + 2 is added since we have to eliminate the character >$
	priceIndex = text.find( '>$' ) + 2; 

	# Here + 4 is since the total 4 character 
	price = float( text[ priceIndex:( priceIndex + 4 ) ] )

	return ( price )

def sendTwitterMessage():
	msg = "I am a message that will be sent to Twitter"
	
	password_manager = urllib.request.HTTPPasswordMgr()
	
	password_manager.add_password("Twitter API",
	"http://twitter.com/statuses", "pk7770007@gmail.com", "")
	
	http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
	page_opener = urllib.request.build_opener(http_handler)
	
	urllib.request.install_opener(page_opener)
	
	params = urllib.parse.urlencode( {'status': msg} )
	
	resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
	resp.read()

	
price_now = input( 'Do you want to see price now (Y/N)?' )

if price_now == 'Y':
	print( getPrice() )
	sendTwitterMessage()
else:
	price = 99.99;
	while price > 4.74:

		# Sleep of 15 minute.
		time.sleep( 10 )
		price = getPrice()
		print( "The price for the coffee is : " + str( price ) )

	print( 'Price is low you can buy.' )