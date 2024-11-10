Ships CLI
The Ships CLI is a simple command-line interface tool written in Python for displaying information about ships and their countries from a JSON data file (ships_data.json). It offers options to view countries, list the top countries by ship count, and more.

Table of Contents
Installation
Usage
Commands
Data File Structure
License
Installation
Clone or download this repository.
Make sure Python 3 is installed on your system.
Place ships_data.json in the same directory as the script, or adjust the file path in the script if needed.
Usage
Run the CLI by executing the following command in the terminal:

bash
Code kopieren
python <filename>.py
Replace <filename> with the actual name of your script file.

The program will prompt you with a welcome message and offer available commands.

Commands
help or 1

Shows a list of all available commands.
show countries or 2

Displays all unique countries from the data file in alphabetical order.
top countries or 3

Prompts for a number, then shows a list of top countries with the most ships.
Example: If you enter 5, the program will show the top 5 countries with the most ships.
exit or 4

Exits the program.
Data File Structure
The ships_data.json file should contain data in the following format:

json
Code kopieren
{
  "data": [
    {
      "COUNTRY": "CountryName",
      "OtherFields": "OtherData"
    },
    ...
  ]
}
Make sure that each entry includes a "COUNTRY" field, as it is required by the CLI.

License
This project is licensed under the MIT License. Feel free to modify and distribute.
