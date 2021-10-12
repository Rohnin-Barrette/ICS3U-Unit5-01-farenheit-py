#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# this program calculates fahrenheit


def calculate_fahrenheit():
    # this function calculates fahrenheit when given celcius

    # input
    celcius_string = input("Enter a temperature (°C): ")

    # process and output
    try:
        celcius = float(celcius_string)
        fahrenheit = (9 / 5) * celcius + 32
        print("{0}°C is equal to {1}°F.".format(celcius, fahrenheit))
    except Exception:
        print("{0} is not a valid input.".format(celcius_string))
    finally:
        print("\nDone.")


def main():
    # this function calls calculate_fahrenheit
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
