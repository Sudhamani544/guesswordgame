import random

li = ['amsterdam','europe','netherlands','australia','canada','germany','india','spain','switzerland','china','nepal']
guessword = random.choice(li)
li1 = [str('-') for i in range(len(guessword))]
print(f'please guess a word of length {len(guessword)}')
print(f'you are given \'length of word + 5\' chances: {len(guessword) + 5}')
guessstring=''

def convert_list_to_string(org_list):
    return guessstring.join(org_list)

def read_guesschars():
    i=0
    while i<len(guessword)+6:
        userguesschar = input('enter a single char: ')
        guesschar = userguesschar.lower()
        #condition to check if guesschar is not valid
        if len(guesschar) == 0 or len(guesschar) >= 2 or guesschar <= '9':
            print('enter a valid char, not a number or more than one character')
            read_guesschars()
        if guesschar in guessword:
            print('correct guess')
            #matching indices for all guesschar
            index_pos_list = [ i for i in range(len(guessword)) if guessword[i] == guesschar ]
            #read into a output list li1
            for j in index_pos_list:
                li1[j] = guesschar
            # Convert list of chars to string
            full_str = convert_list_to_string(li1)
            print(full_str)
            if guessword == full_str:
                print(f'your guess is correct: {full_str}')
                break
        elif guesschar not in guessword:
            print('wrong guess, please guess it again')
            print()
        i += 1
read_guesschars()
