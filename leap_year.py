#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 3, 2025
# Program that takes in a year from the user,
# it then determines whether it is a leap year or not
# according to the Gregorian calendar.


def main():
    # Get the year as a string
    year_as_string = input("Enter a year: ")

    try:
        # Convert the year input to an integer
        year = int(year_as_string)

        # Check if the year is positive
        if year > 0:
            # Check if the year is divisible by 4
            if year % 4 == 0:
                # Check if the year is divisible by 100
                if year % 100 == 0:
                    # Check if the year is divisible by 400
                    if year % 400 == 0:
                        # If it's divisible by 4, 100, and 400,
                        # it's a leap year
                        print(f"{year} is a leap year.")
                    else:
                        # If it's divisible by 4 and 100,
                        # but not divisible by 400,
                        # it's a leap year
                        print(f"{year} is NOT a leap year.")
                else:
                    # If it's divisible by 4
                    # and not divisible by 100,
                    # it's a leap year
                    print(f"{year} is a leap year.")
            else:
                # If it's not divisible by 4,
                # it's not a leap year
                print(f"{year} is NOT a leap year.")
        else:
            # Tell the user that their input must be positive
            print("The year must be a positive integer.")
    except ValueError:
        # Tell the user that their input wasn't an integer
        print(f"{year_as_string} is not an integer.")
    finally:
        # Program completion message
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
