import random

def adventure():
    current_door = 1
    final_door = 100

    while current_door <= final_door:
        print(f"You are at door number {current_door}.")
        choice = input("Do you want to go through the door? (yes/y or no/n): ").strip().lower()

        if choice in ["no", "n"]:
            print("You decided not to go through the door. Game over.")
            return
        elif choice in ["yes", "y"]:
            current_door += 1
            if current_door > final_door:
                print("You're Winner!")
                return

            encounter_chance = min(0.02 + (current_door / final_door) * 0.1, 1.0)
            if current_door >= 5 and random.random() < encounter_chance:
                print("You encountered a monster!")
                monster_choice = input("Do you want to run back (run/r), fight (fight/f), or run past (past/p)? ").strip().lower()

                if monster_choice in ["run", "r"]:
                    current_door = max(1, current_door - 4)
                    print(f"You ran back to door number {current_door}.")
                elif monster_choice in ["fight", "f"]:
                    if random.random() < 0.7:
                        current_door += 1
                        print("You defeated the monster and moved to the next door.")
                    else:
                        current_door = 1
                        print("You lost the fight and were sent back to door number 1.")
                elif monster_choice in ["past", "p"]:
                    if random.random() < 0.5:
                        current_door += 1
                        print("You successfully ran past the monster and moved to the next door.")
                    else:
                        current_door = 1
                        print("You failed to run past the monster and were sent back to door number 1.")
                else:
                    current_door = max(1, current_door - 1)
                    print(f"Invalid choice. You were sent back to door number {current_door}.")
                    continue
        else:
            current_door = max(1, current_door - 1)
            print(f"Invalid choice. You were sent back to door number {current_door}.")
            continue

if __name__ == "__main__":
    adventure()