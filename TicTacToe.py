print("\tTicTcToeProject\n")


game = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
    }

gamer = 1 
moves = 0 
endCheck = 0
Player1 = input("Enter 1st player name : ").upper()
Player2 = input("Enter 2nd player name : ").upper()

def check():

    if game['1'] == 'X' and game['2'] == 'X' and game['3'] == 'X':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player1 + ' Won!!')
    
        return 1
    if game['4'] == 'X' and game['5'] == 'X' and game['6'] == 'X':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player1 + ' Won!!')
    
        return 1
    if game['7'] == 'X' and game['8'] == 'X' and game['9'] == 'X':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player1 + ' Won!!')
    
        return 1
    
    if game['1'] == 'X' and game['5'] == 'X' and game['9'] == 'X':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player1 + ' Won!!')
    
        return 1
    
    if game['3'] == 'X' and game['5'] == 'X' and game['7'] == 'X':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player1 + ' Won!!')
    
        return 1
    
    if game['1'] == 'X' and game['4'] == 'X' and game['7'] == 'X':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player1 + ' Won!!')
    
        return 1
    if game['2'] == 'X' and game['5'] == 'X' and game['8'] == 'X':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player1 + ' Won!!')
    
        return 1
    if game['3'] == 'X' and game['6'] == 'X' and game['9'] == 'X':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player1 + ' Won!!')
    
        return 1
    
    if game['1'] == 'O' and game['2'] == 'O' and game['3'] == 'O':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player2 + ' Won!!')

        return 1
    
    if game['4'] == 'O' and game['5'] == 'O' and game['6'] == 'O':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player2 + ' Won!!')

        return 1
    if game['7'] == 'O' and game['8'] == 'O' and game['9'] == 'O':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player2 + ' Won!!')

        return 1
    
    if game['1'] == 'O' and game['5'] == 'O' and game['9'] == 'O':
        print('\nCongratulation ..)')
        print('\nPlayer ' + Player2 + ' Won!!')

    if game['3'] == 'O' and game['5'] == 'O' and game['7'] == 'O':
        print('\nCongratulation ..)')
        print('\nPlayer ' + Player2 + ' Won!!')

        return 1
    
    if game['1'] == 'O' and game['4'] == 'O' and game['7'] == 'O':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player2 + ' Won!!')

        return 1
    if game['2'] == 'O' and game['5'] == 'O' and game['8'] == 'O':
        print('\nCongratulation ..)')
        print('\nPlayer ' + Player2 + ' Won!!')

        return 1
    if game['3'] == 'O' and game['6'] == 'O' and game['9'] == 'O':
        print('\nCongratulation ..')
        print('\nPlayer ' + Player2 + ' Won!!')

        return 1
    return 0


print('\nThis is game pattern\n')
print(' |-----------|')
print(' | 1 | 2 | 3 |')
print(' |---|---|---|')
print(' | 4 | 5 | 6 |')
print(' |---|---|---|')
print(' | 7 | 8 | 9 |')
print(' |-----------|')

print("\nLet's Start the game\n")
while True:
    print(' |-----------|')
    print(' | '+game['1'] + ' | ' + game['2'] + ' | ' + game['3']+' |')
    print(' |---|---|---|')
    print(' | '+game['4'] + ' | ' + game['5'] + ' | ' + game['6']+' |')
    print(' |---|---|---|')
    print(' | '+game['7'] + ' | ' + game['8'] + ' | ' + game['9']+' |')
    print(' |-----------|')
    endCheck = check()

    if moves == 9 or endCheck == 1:
        print("\nThe Game Over")
        break

    while True: 

        if gamer == 1:
            print("\nEnter a number from 1 to 9 to give O/X on the board")
            p1_input = input('Player '+Player1 +' turn : ')
            print()

            if p1_input in game and game[p1_input] == ' ':
                game[p1_input] = 'X'
                gamer = 2
                break
            
            else:
                print('Invalid input, please try again')
                continue

        else:
            print("\nEnter a number from 1 to 9 to give O/X on the board ")
            p2_input = input('Player '+Player2+' turn : ')
            print()

            if p2_input in game and game[p2_input] == ' ':
                game[p2_input] = 'O'
                gamer = 1
                break

            else: 
                print('Invalid input, please try again')
                continue

    moves += 1
    
