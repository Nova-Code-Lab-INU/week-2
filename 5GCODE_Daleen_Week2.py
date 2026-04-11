import random 
#genearte a secert number between  and 100
def secret_code_game():
    secret_number=random.randint(1.100)
    attempts=0
    print("---Welcome To The Secret GAME!---")
    print("I`m thinking of a number betwwwn 1and 100.")

    while True:
        try:
            guess=int(input("Enter your guess:"))
            attempts+=1

            if  guess == secret_number:
                print(f"Congratulations! you found the code {attempts} attempts.")
            elif guess < secret_number:
                print("Higher! Try again.")
            else:
                print("Lower! Try again.")
        except ValueError:
            print("Invalid input. Please  enter a whole number.")
if __name__ =="__main__":
    secret_code_game()

        

