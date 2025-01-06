import random

print("2205238")
print("sarvansh")
def game():
    total_weight = 0
    used_values = []
    print("Welcome to the Set Weight game! The total weight is set to 50.")

    while total_weight < 50:
        while True:
            try:
                user_value = int(input(
                    f"Enter a weight value between 1 and 9 (Unique value): "))
                if user_value < 1 or user_value > 9:
                    print("Value must be between 1 and 9.")
                elif user_value in used_values:
                    print(
                        "Value has already been used. Choose a unique value.")
                else:
                    used_values.append(user_value)
                    total_weight += user_value
                    print(
                        f"Your choice: {user_value}, Total weight: {total_weight}")
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

        if total_weight == 50:
            print(
                f"Congratulations! You won the game by adding {user_value}. Total weight: {total_weight}")
            break

        remaining_values = [i for i in range(1, 10) if i not in used_values]
        if not remaining_values:
            print("No unique values left. It's a draw!")
            break

        comp_value = random.choice(remaining_values)
        used_values.append(comp_value)
        total_weight += comp_value
        print(f"Computer's choice: {comp_value}, Total weight: {total_weight}")

        if total_weight == 50:
            print(
                f"Sorry, you lost! The computer won the game by adding {comp_value}. Total weight: {total_weight}")
            break


game()
