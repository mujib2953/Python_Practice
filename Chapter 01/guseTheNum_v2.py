print( 'Welcome to Guess the Number game' )
inputValue = input( 'Guess the numbrer :: ' )
inputValue = int( inputValue )

if inputValue == 5:
    print( 'Hola! You have won the game...' )
else:
    if inputValue > 5:
        print( 'Too high. You should guess smaller values' )
    else :
        print( 'Too low. You should guess bigger values' )

# print( 'Alas! You have lost. Try luck again.' )

print( '---- Game over papi ----' )
