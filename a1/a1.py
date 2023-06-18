"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *
import sys


# Fill these in with your details
__author__ = "{Erik Flink} ({s46267445})"
__email__ = "e.flin@uqconnect.edu.au"
__date__ = "19/08/20"



# Write your code here (i.e. functions)


def select_word_at_random(word_select):
    """
    Selects random word depedning on difficulty selected

    Parameters:
        word_select (str): the variable to determine which letter word will be
        selected

    Returns:
        A randomly selected word with either 6,7,8 or 9 letters
    """
    if word_select =='FIXED':
        words=load_words('FIXED')
        word=random.choice(words)
    elif word_select == 'ARBITRARY':
        words=load_words('ARBITRARY')
        word=random.choice(words)
    else:
        word=None
    return word


def guess_index(word):
    """
    Selects the number and order of guesses from the a1_support

    Parameters:
        word(str): The word selected to be guessed

    Returns:
        The number of guesses and the characters to be guessed in each one
    
    """
    word_length = len(word)
    if word_length == 6:
        guess_slice=GUESS_INDEX_TUPLE[0]
    elif word_length == 7:
        guess_slice=GUESS_INDEX_TUPLE[1]
    elif word_length == 8:
        guess_slice=GUESS_INDEX_TUPLE[2]
    elif word_length == 9:
        guess_slice=GUESS_INDEX_TUPLE[3]
    return guess_slice


def display_guess_matrix(guess_no, word_length, scores):
    """
    prints the progress of the game

    Parameters:
        guess_no(int): The number of guesses
        word_length(int): the amount of letters in the word to be guessed
        score(Integer tuple): Points acquired for each guess
        
    returns:
        Displays rows guessed and to be guessed detailing scores for each row,
        and marked letters that were guessed.
    """
    if word_length == 6:
        print('       | {} | {} | {} '
              '| {} | {} | {} |'.format(1,2,3,4,5,6))
        print('-'*(4*word_length+9))
        
        count=0
        while count < guess_no-1:
    
            guess_index=((0,1),(2,4),(2,4),(3,5),(2,5),(0,5))
            letter_guess=guess_index[count]
            asterisk=()
            y=list(range(letter_guess[0],letter_guess[1]+1))
            z=list(range(0,word_length+1))            
            for c in z:
                if c in y:
                    asterisk+=('| * ',)
                else:
                    asterisk+=('| - ',)
                
            print('Guess '+str(count+1)+'{}{}{}{}{}{}'
                  '|'.format(*asterisk)+'   '+str(scores[count])+' Points')
            print('-'*(4*word_length+9))

            count+=1
        if count == guess_no-1:
            
            guess_index=((0,1),(2,4),(2,4),(3,5),(2,5),(0,5))
            letter_guess=guess_index[count]
            asterisk=()
            y=list(range(letter_guess[0],letter_guess[1]+1))
            z=list(range(0,word_length+1))
            count+=1
            for c in z:
                if c in y:
                    asterisk+=('| * ',)
                else:
                    asterisk+=('| - ',)
            print('Guess '+str(count)+'{}{}{}{}{}{}'
                  '|'.format(*asterisk))
            print('-'*(4*word_length+9))
   
    if word_length == 7:
        print('       | {} | {} | {} '
              '| {} | {} | {} | {} |'.format(1,2,3,4,5,6,7))
        print('-'*(4*word_length+9))
        
        count=0
        while count < guess_no-1:
    
            guess_index=((0,1),(1,2),(4,6),(2,5),(3,6),(2,6),(0,6))
            letter_guess=guess_index[count]
            asterisk=()
            y=list(range(letter_guess[0],letter_guess[1]+1))
            z=list(range(0,word_length+1))            
            for c in z:
                if c in y:
                    asterisk+=('| * ',)
                else:
                    asterisk+=('| - ',)
                
            print('Guess '+str(count+1)+'{}{}{}{}{}{}{}'
                  '|'.format(*asterisk)+'   '+str(scores[count])+' Points')
            print('-'*(4*word_length+9))

            count+=1
        if count == guess_no-1:
            
            guess_index=((0,1),(1,2),(4,6),(2,5),(3,6),(2,6),(0,6))
            letter_guess=guess_index[count]
            asterisk=()
            y=list(range(letter_guess[0],letter_guess[1]+1))
            z=list(range(0,word_length+1))
            count+=1
            for c in z:
                if c in y:
                    asterisk+=('| * ',)
                else:
                    asterisk+=('| - ',)
            print('Guess '+str(count)+'{}{}{}{}{}{}{}'
                  '|'.format(*asterisk))
            print('-'*(4*word_length+9))
 
    if word_length == 8:
        print('       | {} | {} | {} '
              '| {} | {} | {} | {} | {} |'.format(1,2,3,4,5,6,7,8))
        print('-'*(4*word_length+9))
        
        count=0
        while count < guess_no-1:
    
            guess_index=((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(2,7),(0,7))
            letter_guess=guess_index[count]
            asterisk=()
            y=list(range(letter_guess[0],letter_guess[1]+1))
            z=list(range(0,word_length+1))            
            for c in z:
                if c in y:
                    asterisk+=('| * ',)
                else:
                    asterisk+=('| - ',)
                
            print('Guess '+str(count+1)+'{}{}{}{}{}{}{}{}'
                  '|'.format(*asterisk)+'   '+str(scores[count])+' Points')
            print('-'*(4*word_length+9))

            count+=1
        if count == guess_no-1:
            
            guess_index=((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(2,7),(0,7))
            letter_guess=guess_index[count]
            asterisk=()
            y=list(range(letter_guess[0],letter_guess[1]+1))
            z=list(range(0,word_length+1))
            count+=1
            for c in z:
                if c in y:
                    asterisk+=('| * ',)
                else:
                    asterisk+=('| - ',)
            print('Guess '+str(count)+'{}{}{}{}{}{}{}{}'
                  '|'.format(*asterisk))
            print('-'*(4*word_length+9))

    if word_length == 9:
        print('       | {} | {} | {} '
              '| {} | {} | {} | {} | {} | {} |'.format(1,2,3,4,5,6,7,8,9))
        print('-'*(4*word_length+9))
        
        count=0
        while count < guess_no-1:
    
            guess_index=((0,1),(1,3),(4,7),(3,5),(3,6),
                         (5,7),(3,7),(2,8),(0,8))
            letter_guess=guess_index[count]
            asterisk=()
            y=list(range(letter_guess[0],letter_guess[1]+1))
            z=list(range(0,word_length+1))            
            for c in z:
                if c in y:
                    asterisk+=('| * ',)
                else:
                    asterisk+=('| - ',)
                
            print('Guess '+str(count+1)+'{}{}{}{}{}{}{}{}{}'
                  '|'.format(*asterisk)+'   '+str(scores[count])+' Points')
            print('-'*(4*word_length+9))

            count+=1
        if count == guess_no-1:
            
            guess_index=((0,1),(1,3),(4,7),(3,5),(3,6),
                         (5,7),(3,7),(2,8),(0,8))
            letter_guess=guess_index[count]
            asterisk=()
            y=list(range(letter_guess[0],letter_guess[1]+1))
            z=list(range(0,word_length+1))
            count+=1
            for c in z:
                if c in y:
                    asterisk+=('| * ',)
                else:
                    asterisk+=('| - ',)
            print('Guess '+str(count)+'{}{}{}{}{}{}{}{}{}'
                  '|'.format(*asterisk))
            print('-'*(4*word_length+9))


def create_guess_line(guess_no, word_length):
    """
    Returns string corresponding to the guess_no


    Parameters:
        guess_no(int): The number of guesses
        word_length(int): the amount of letters in the word to be guessed
        
    Returns:
        This functions creates the latest guess line depending on guess_no
        and word length with the letters to be guessed marked with an asterisk
    """
    if word_length == 6:
        
        guess_index=((0,1),(2,4),(2,4),(3,5),(2,5),(0,5))
        letter_guess=guess_index[guess_no-1]
        asterisk=()
        y=list(range(letter_guess[0],letter_guess[1]+1))
        z=list(range(0,word_length+1))
        for c in z:
            if c in y:
                asterisk+=('| * ',)
            else:
                asterisk+=('| - ',)
        guess_line='Guess '+str(guess_no)+'{}{}{}{}{}{}|'.format(*asterisk)

    if word_length == 7:
        
        guess_index=((0,1),(1,2),(4,6),(2,5),(3,6),(2,6),(0,6))
        letter_guess=guess_index[guess_no-1]
        asterisk=()
        y=list(range(letter_guess[0],letter_guess[1]+1))
        z=list(range(0,word_length+1))
        for c in z:
            if c in y:
                asterisk+=('| * ',)
            else:
                asterisk+=('| - ',)
        guess_line='Guess '+str(guess_no)+'{}{}{}{}{}{}{}|'.format(*asterisk)

    if word_length == 8:
        
        guess_index=((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(2,7),(0,7))
        letter_guess=guess_index[guess_no-1]
        asterisk=()
        y=list(range(letter_guess[0],letter_guess[1]+1))
        z=list(range(0,word_length+1))
        for c in z:
            if c in y:
                asterisk+=('| * ',)
            else:
                asterisk+=('| - ',)
        guess_line='Guess '+str(guess_no)+'{}{}{}{}{}{}{}{}|'.format(*asterisk)

    if word_length == 9:
        
        guess_index=((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(3,7),(2,8),(0,8))
        letter_guess=guess_index[guess_no-1]
        asterisk=()
        y=list(range(letter_guess[0],letter_guess[1]+1))
        z=list(range(0,word_length+1))
        for c in z:
            if c in y:
                asterisk+=('| * ',)
            else:
                asterisk+=('| - ',)
        guess_line='Guess '+str(guess_no)+'{}{}{}{}{}{}{}{}{}|'.format(*asterisk)
    return guess_line
    
def compute_value_for_guess(word, start_index,end_index, guess):
    """
    compares the guessed string to the substring to see how many points are
    achieved

    Parameters:
        word(str): The word to be guessed
        start_index(int): The starting position of the substring in the word
        end_index(int): The ending position of the substring int he word
        guess(str): the guessed inputed by the player

    Return:
        the number of points for the guess
        
    """
    sub = word[start_index:end_index+1]
    points=0
    if len(guess) == len(sub):
        for i,c in enumerate(guess):
            if c in sub:
                if i == sub.find(c):
                    if c in VOWELS:
                        points += 14
                    if c in CONSONANTS:
                        points += 12
                else:
                    points += 5
        
    return points

    

def main():
    """
    start of game
    """
    print(WELCOME)

    start = True
    while start:
        input_com=input(INPUT_ACTION)
        if input_com == 's':
            start=False
        elif input_com == 'h':
            print(HELP)
            start=False
        elif input_com == 'q':
            return
        else:
            print(INVALID)
    word_select = (input("Do you want a 'FIXED' or 'ARBITRARY' length "
                           "word?: "))
    
    word = select_word_at_random(word_select)
    word_length = len(word)
    guess_slice = guess_index(word)
    guess_no=1
    scores=()
    
    print('Now try and guess the word, step by step!!')
      

    
    while guess_no < word_length:

        letter_guess=guess_slice[guess_no-1]


        start_index = letter_guess[0]
        end_index = letter_guess[1]
        points = 0

        sub = word[start_index:end_index+1]

        display_guess_matrix(guess_no, word_length, scores)
        create_guess_line(guess_no, word_length)
        guess=input('Now enter Guess '+str(guess_no)+': ')
        while len(guess) !=  len(sub):
            guess=input('Now enter Guess '+str(guess_no)+': ')

        points=compute_value_for_guess(word, start_index,end_index, guess)
 
        guess_no+=1 
        scores+=(points,)


        if guess_no == word_length:
            display_guess_matrix(guess_no, word_length, scores)
            create_guess_line(guess_no, word_length)
            guess = input('Now enter your final guess. i.e. guess the whole'
                          ' word: ')
            if guess == word:
                print('You have guessed the word correctly. Congratulations.')
            else:
                print('Your guess was wrong. The correct word was "'+word+'"')
            


if __name__ == "__main__":
    main()
