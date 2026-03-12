import random
import time

def generate_number() -> str:
    """
    Generates a unique four-digit number for the game.
    Ensures that the first digit is not zero.
    """
    ### Lists of numbers to choose from
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_without_zero = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    ### Setting the number so it doesn't start with zero and has no duplicates
    first_number = random.choice(list_without_zero)
    number_list.remove(first_number)
    remaining_numbers = random.sample(number_list, 3)
    final_list = [first_number] + remaining_numbers
    return "".join(str(num) for num in final_list)

def evaluate_bulls_cows(guessed_number: str, secret_number: str) -> tuple[int, int]:
    """
    Compares the user's guess with the generated secret number.
    Returns the count of bulls (correct digit and position) and cows (correct digit).
    """
    bulls = 0
    cows = 0
    for i in range(4):
        ### If it's in the same position, it's a bull/bulls
        if guessed_number[i] == secret_number[i]:
            bulls += 1
        ### If it's not in the same position but exists in the number, it's a cow/cows
        elif guessed_number[i] in secret_number:
            cows += 1
    return bulls, cows

def get_guess_text(attempts: int) -> str:
    """Adjusts the correct form of guess/guesses based on the number of attempts."""
    word = "guess" if attempts == 1 else "guesses"
    return f"{attempts} {word}"

def main_game():
    """Main function of the entire game."""
    while True:
        guessed_number = ""
        attempts = 0
        secret_number = generate_number()

        ### Introductory text for the user
        print("Hi there!")
        print("-" * 47) 
        print("I've generated a random 4 digit number for you.", 
              "Let's play a bulls and cows game.", sep="\n")
        print("-" * 47) 

        start_time = time.time()  # Starting the timer

        ### Main loop: repeats until the user guesses correctly
        while guessed_number != secret_number:
            guessed_number = input("Enter a number: ")
            print("-" * 47)

            ### Validation of user input
            # 1. Length check
            if len(guessed_number) != 4:
                print("Error! You must enter a 4-digit number.")
                continue

            # 2. Digit check
            if not guessed_number.isdigit():
                print("Error! You must enter digits only.")
                continue
            
            # 3. Check for leading zero
            if guessed_number[0] == "0":
                print("Error! The number must not start with zero.")
                continue

            # 4. Duplicate check using a set
            if len(set(guessed_number)) != len(guessed_number):
                print("Error! The number must not contain duplicates.")
                continue
            
            attempts += 1

            # Victory check
            if guessed_number == secret_number:
                break

            ### Evaluation
            bulls, cows = evaluate_bulls_cows(guessed_number, secret_number)

            # Pluralization of bulls/cows
            b_text = "bull" if bulls == 1 else "bulls"
            c_text = "cow" if cows == 1 else "cows"
            
            print(f"{bulls} {b_text}, {cows} {c_text}")
            print("-" * 47)

        ### End of the game and time calculation
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        print(f"Correct, you've guessed the right number\nin {get_guess_text(attempts)}!")
        print(f"It took you {duration} seconds.")
        print("-" * 47)
        print("That's amazing!")
        print("-" * 47)

        ### Ask to play again?
        play_again = input("Do you want to play again? (y/n): ").lower()
        print("-" * 47)
        if play_again != 'y':
            print("Thanks for playing! Bye.")
            break

if __name__ == "__main__":
    main_game()