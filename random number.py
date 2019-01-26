winning_number = 43
user_input = int(input('guess your number between 1 t0 100'))
if user_input==43:
    print('you win')
else:
    if user_input>=winning_number:
        print('to high')
    else:
       # if user_input<=winning_number:
            print('to low')
