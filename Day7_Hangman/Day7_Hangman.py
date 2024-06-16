#Hangman

#import libraries
import random
import Hangman_art
import Hangman_wordlist

print(Hangman_art.logo)

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(Hangman_wordlist.word_list)
#print(chosen_word)

#Print the blanks for the chosen word equivalend to given number of letters
display = []
for i in range(0, len(chosen_word)):
    display.append("_")

print("\n")
print(f"{' '.join(display)}")

word_length = len(chosen_word)

end_of_game = False

lives = 6

while not end_of_game:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("\nGuess a letter\n").lower()
    
    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                if display[position] == "_":
                    display[position] = letter
                else:
                    print("\nYou have already chosen that letter, try another one.")
            
    else:
        lives -= 1
        print(Hangman_art.stages[lives])
        print("Sorry that's incorrect")
        if lives == 0:
            print("You lose!")
            print(f"\nThe word was {chosen_word}")
            break
            
    print(f"\n{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win!")