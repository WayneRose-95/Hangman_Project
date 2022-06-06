# First Define The Rules of Hangman 

'''
Rules: 

Given two parties a guesser and the executioner
The executioner chooses a word
When the guesser guesses a letter
The executioner verifies if it is right or wrong 
The game concludes when the either the word is guessed
or if the guesser runs out of lives. 

'''

# How to implement this in code? 
# Define a class and define its attributes 
# Classes are better than raw code because of reusability. 

import random


class Hangman:

    def __init__(self, number_of_lives):
        self.lives = number_of_lives 
        self.word_list = []
        self.letters_chosen = []
        self.empty_list = []
        self.index = '_'
        self.number_of_letters = len(set(self.word_list))
        
        

    def input_letter(self):

        '''
        Method to ask the user to input a letter 

        '''
        # While the below statement is True
        while True:
            # Input a letter 
            player_choice = input('Please choose a letter:').lower()
            # If the length of the letter input is greater than 1
            if len(player_choice) > 1:
                # A message telling the user to input one letter will come up
                print('Please just input one letter')
            elif player_choice.isalpha() is False: 
                print('Only letters from A-Z, please.')
            # If the player's choice is in the letters chosen then do the following: 
            elif player_choice in self.letters_chosen:
                print('You have already tried this letter')
            # But if it is equal to 1 then the while loop will break. 
            elif len(player_choice) == 1:
                break

       # Player choice is returned to be used inside future methods. 
        return player_choice

    def choose_random_word(self):

        '''
        Method for the program to choose a random word from a text file

        '''

        # Open the text file 
        with open("words.txt", "r") as file:
        # Choose a random word from said text file by iterating through the text file. 
            
                # For each row in the file, read each line, and split each of the lines. 
            word = random.choice(file.read().splitlines())
                # This returns a list of lines
            
            # Return this word to be used inside further methods. 
            return word
        
        # Print that word (for debugging purposes)

    def convert_random_word(self):
        '''
        Method to convert the random word generated within the words.txt file into a list of underscores

        '''
        # Choose a random word 
        random_word = self.choose_random_word()

        # Set the length of that word to the number of characters.
          
        length_of_word = len(random_word)

        # Create an empty list (intialised in the __init__ method as self.word_list = [])

        # For each character in the length of the word
        for character in range(length_of_word):
            self.word_list.append("_")

        print(self.word_list) # prints out === ['_', '_', '_' etc....]
        print('Start Game!')
        print(f'The word has {len(self.word_list)} characters')
        # append empty characters to that list in accordance with the number of characters inside the word. 
        return ''.join(self.word_list), random_word

    # Make a method to check the indexes of the list 

        
    
    def check_letter(self):

        '''
        Method to check the letter that the user has input.
        
        '''
        #TODO: Change the names of the weird variable names 
        # Sets the random_word generated from this method to a variable. 
        random_word = self.convert_random_word()[1]

        # While the number of lives the player has is greater than 0 
        while self.lives > 0:
            # Set the variable stored_player_input to the output of input_letter method 
            stored_player_input = self.input_letter()
            print(stored_player_input)
            # If the word is within the random_word generated from the previous method
            if stored_player_input in random_word:
                print('Correct letter')
                # Append the users' input to intial empty list 
                self.letters_chosen.append(stored_player_input)
                # Whatever is in here : ['_', '_', '_' etc....] has to be replaced by the users' input in the right area. 
                # Find the index of the letter inside the random word. 


                # For the random_word chosen, find its index given the users' input 
                # indices can be refactored to be: [index for index, value in enumerate(random_word) if value == stored_player_input]
                # Initalise an empty list 
                indices = []
                for index, value in enumerate(random_word):
                    # If the current value matches something, append the index to the list
                    if value == stored_player_input:
                        indices.append(index)
                # print(index)
                # Loop returns a list of indexes which represent the the position of the letter the user has chosen. 
            
                
                for letter in range(len(self.word_list)):
                # For each '_' inside the range of t length of the list of underscores
                    for index in indices:
                        # Iterate through the indices list
                        print(len(indices))
                        # Delete each '_' inside the list of underscores 
                        # which corresponds to the integer value in the indices list
                        # Where the integer value represents the index of the list needed to find the correct character to delete and replace. 
                        del self.word_list[index]
                        self.number_of_letters -= 1
                        # Next, insert the users' input in place of the deleted underscore 
                        self.word_list.insert(index, stored_player_input)
                        # Lastly, remove the integer used at the end of the process. 
                        indices.remove(index)
                    
                    print(f'Correct Letters = {abs(self.number_of_letters)}')
                    
                    # Continue the following loop until the indices list is empty    
                    if indices == []: 
                        # Then break out of the loop
                        break 
                
                # Print the resultant list of underscores for the user to view their progress. 
                print(self.word_list)

            # Condition for incorrect guess
            
            elif stored_player_input not in random_word:
                print('incorrect letter')
                self.letters_chosen.append(stored_player_input)
                print(self.word_list)
                print(self.letters_chosen)
                self.lives -= 1
                print(f'You have {self.lives} lives remaining')
            
            # Logic to set the win condition of the game. 

            if abs(self.number_of_letters) == len(self.word_list):
                print("You Win!")
                break
            
            # Logic for if the number of lives reaches zero
            if self.lives == 0:
                print('YOU LOSE!!!')
                print(f'The word was: {random_word}')

                
        

    def play_again(self):
        '''
        Method to ask the user to play the game again given the result of the game 

        '''
        pass
            
                
    

    def play_game(self):
        new_game = Hangman(5)
        new_game.choose_random_word()
        new_game.check_letter()
        
        


if __name__ == "__main__":

    new_game = Hangman(5)
    new_game.play_game()
    new_game.play_again()