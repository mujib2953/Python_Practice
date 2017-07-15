# -*- coding: utf-8 -*-
# @Author: Mujib
# @Date:   2017-07-15 15:05:13
# @Last Modified by:   Mujib
# @Last Modified time: 2017-07-15 15:20:03

actualString = 'Monster truck rally. 4pm. Monday'

print( 'This is upperCase >>> ' + actualString.upper() )
print( '---------------------------------------------' )

print( 'This is lowerCase >>> ' + actualString.lower() )
print( '---------------------------------------------' )

print( 'Is string ends with ".jpg" >>> ' )
print( actualString.endswith( '.jpg' ) )
print( '---------------------------------------------' )

print( 'Is string starts with "Monster" >>> ' )
print( actualString.startswith( 'Monster' ) )
print( '---------------------------------------------' )

print( 'This will strip the given string.' )
print( actualString.strip() )
print( '---------------------------------------------' )

print( 'This will find the given text and return index. i.e. "python"' )
print( actualString.find( 'python' ) )
print( '---------------------------------------------' )

print( 'This will implement replace the words or letter in a given string.' )
print( actualString.replace( 'Monday', 'Friday' ) )

print( '---------------------------------------------' )