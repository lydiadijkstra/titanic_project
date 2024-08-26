import json
import operator


with open("ships_data.json", "r") as fileobj:
    all_data = json.load(fileobj)


def command_help():
    """
    Shows a list with all the user-Options
    """
    print("""Available commands:\n
    1. help => Show all Options
    2. show countries => Show all countries from the file
    3. top countries => Show a list with the top countries
    4. exit => Leave the programm
    """)


def command_show_countries():
    """
    Shows every country without duplicates in alphabetic order
    print: country
    """
    unique_countries = set()
    for ship in all_data["data"]:
        unique_countries.add(ship["COUNTRY"])
    sorted_countries = sorted(unique_countries)
    for country in sorted_countries:
        print(country)


def count_ships():
    """
    Counts the ships for every country
    return: dictionary
    """
    country_ship_count = {}
    for ship in all_data["data"]:
        country_name = ship["COUNTRY"]
        if country_name not in country_ship_count:
            country_ship_count[country_name] = 0
        country_ship_count[country_name] += 1
    return country_ship_count


def command_top_countries(top_num):
    """
    prints a list of top countries with the most ships
    return: prints country and ship amount
    """
    country_ship_count = count_ships()
    top_ship_count = list(country_ship_count.items())
    top_ship_count.sort(key=operator.itemgetter(1), reverse=True)
    for country, amount in top_ship_count[:top_num]:
        print(f"Country: {country}: {amount}")


def main():
    """
    main function to get input and run the choosen functions
    """
    while True:
        choice = input("\nWelcome to the Ships CLI! Enter 'help' to view available commands. ")
        if choice in ("help","1"):
            command_help()
        elif choice in ("show countries", "2"):
            command_show_countries()
        elif choice in ("top countries", "3"):
            while True:
                try:
                    top_num = int(input("Enter the number of top-countries to be shown: "))
                    if top_num <= 0:
                        print("Only positive numbers allowed!")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number")
                    continue
            command_top_countries(top_num)
        elif choice in ("exit", "4"):
            print("Have a nice day!")
            break
        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
