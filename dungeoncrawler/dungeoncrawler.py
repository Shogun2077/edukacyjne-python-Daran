# dungeoncrawler.py
def main():
    # Initialize player parameters
    player = {
        "pieniądze": 50,
        "Punkty Życia": 100,
        "Atak": 5,
        "mikstury zdrowia": 1,
        "mikstury wsparcia": 1
    }

    # Greet the player
    print("Witamy przed jaskinią!")
    print("Gdzie chcesz iść?")
    print("Miasto (M), Jaskinia (J), Las (L)")

    # Get player's choice
    choice = input("Wybierz miejsce: ").strip().upper()

    # Load the corresponding module based on the player's choice
    if choice == "M":
        import city
        city.explore(player)
    elif choice == "J":
        import cave
        cave.explore(player)
    elif choice == "L":
        import forest
        forest.explore(player)
    else:
        print("Nieprawidłowy wybór. Gra zakończona.")

if __name__ == "__main__":
    main()