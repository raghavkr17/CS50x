def main():
    # Get the amount of change owed from the user
    while True:
        try:
            change = float(input("Change owed: "))
            if change > 0:
                break
        except ValueError:
            continue

    # Convert dollars to cents
    cents = round(change * 100)

    # Calculate the minimum number of coins
    coins = 0

    # Quarters
    coins += cents // 25
    cents %= 25

    # Dimes
    coins += cents // 10
    cents %= 10

    # Nickels
    coins += cents // 5
    cents %= 5

    # Pennies
    coins += cents

    # Output the minimum number of coins
    print(coins)


if __name__ == "__main__":
    main()
