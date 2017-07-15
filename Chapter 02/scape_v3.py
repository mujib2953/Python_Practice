# -*- coding: utf-8 -*-
# @Author: Mujib Ansari
# @Date:   2017-07-15 14:59:26
# @Last Modified by:   Mujib
# @Last Modified time: 2017-07-15 15:32:39

# For Loyal customer
import urllib.request

normalCustomer = 'http://beans-r-us.appspot.com/prices.html'
loyalCustomer = 'http://www.beans-r-us.appspot.com/prices-loyalty.html'

page = urllib.request.urlopen( loyalCustomer )

text = page.read().decode( 'utf8' )

# Here + 2 is added since we have to eliminate the character >$
priceIndex = text.find( '>$' ) + 2; 

# Here + 4 is since the total 4 character 
price = text[ priceIndex:( priceIndex + 4 ) ]
print( priceIndex )

print( "The price fro the coffee is : " + price )
