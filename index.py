import random

def guess_the_number():
   
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to Guess the Number!")
    print("I am thinking of a number between 1 and 100.")

   
    while True:
        try:
            
            user_guess = int(input("Take a guess: "))
            attempts += 1

            
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f" Correct! You found the number in {attempts} attempts.")
                break
                
        except ValueError:
            print("Please enter a valid valid integer.")


if __name__ == "__main__":
    guess_the_number()
