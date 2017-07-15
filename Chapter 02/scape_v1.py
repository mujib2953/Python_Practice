import urllib.request
# http://beans-r-us.appspot.com/prices.html
# http://www.beans-r-us.biz/prices.html

baseUrl = 'http://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS'

page = urllib.request.urlopen( baseUrl )

text = page.read().decode( 'utf8' )

print( text )
