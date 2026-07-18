#outer function
def make_hangman(secret_word):
    #guess list
    guesses = []

    #inner function
    def hangman_closure(letter):
        guesses.append(letter)

        #check the guessed letter to the word
        result = ''
        for letter in secret_word:
            if letter in guesses:
                result += letter
            else:
                result += "_"
        
        #print the result
        print(result)

        # check if the secret word was matched
        if '_' in result:
            return False
        else:
            return True
        
    return hangman_closure


game = make_hangman('money')

guess = input('Welcome to hangman, your first guess?')

while not game(guess):
     guess = input('Another guess?')
     game(guess)

print('Congratulation you guessed it')
