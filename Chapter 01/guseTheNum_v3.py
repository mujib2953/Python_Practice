# game new version with looping

print( '--- Welcome papi ---' );

guess = 0;

while guess != 5:
    guess = int( input( 'Guess the number >>> ' ) )
    if guess == 5:
        print( 'Hola! You won it.--' )
    else:
        if guess > 5:
            print( 'Papi you have gussed bigger number.' )
        else:
            print( 'Papi you have gussed smaller number.' )

print( '--- This is the end of game. ---' );
