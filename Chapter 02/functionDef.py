# -*- coding: utf-8 -*-
# @Author: Mujib
# @Date:   2017-07-15 16:07:35
# @Last Modified by:   Mujib
# @Last Modified time: 2017-07-15 16:19:07

# To implement the basic function

def make_smoothie():
	juice = input( 'What juice you would like? >>>' )
	fruit = input( 'Ok - and how about fruit. >>>' )

	print( 'Thanks, Let`s go.' )
	print( 'Crushing the ice.' )
	print( 'Blending the ' + fruit  )
	print( 'Now , adding some ' + juice + ' juice.' )
	print( 'Finished! There`s your ' + fruit + ' and ' + juice + ' smoothie.' )



print( 'Welcome to Smoothie..' )
order = 'Y'

while order == 'Y':
	make_smoothie();
	order = input( 'Do you want to order more( Y/N )?' )
	pass
