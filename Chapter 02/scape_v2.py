import urllib.request

normalCustomer = 'http://beans-r-us.appspot.com/prices.html'

page = urllib.request.urlopen( normalCustomer )

text = page.read().decode( 'utf8' )
price = text[ 234:238 ]

print( "The price fro the coffee is : " + price )
