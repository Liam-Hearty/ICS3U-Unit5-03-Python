#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program converts a number grade to a percent.


def convert_mark(grade):
    # calculate area

    new_mark = None

    if grade == "4+":
        new_mark = 97
    elif grade == "4":
        new_mark = 90
    elif grade == "4-":
        new_mark = 83
    elif grade == "3+":
        new_mark = 78
    elif grade == "3":
        new_mark = 75
    elif grade == "3-":
        new_mark = 71
    elif grade == "2+":
        new_mark = 68
    elif grade == "2":
        new_mark = 65
    elif grade == "2-":
        new_mark = 61
    elif grade == "1+":
        new_mark = 58
    elif grade == "1":
        new_mark = 55
    elif grade == "1-":
        new_mark = 51
    elif grade == "R":
        new_mark = 30
    elif grade == "NE":
        new_mark = 0
    else:
        new_mark = "-1"

    return new_mark


def main():
    # this function gets base and height

    # input
    grade_from_user = str(input("Enter your grade: "))
    print("")

    # call functions
    new_mark = convert_mark(grade_from_user)

    # show results
    if new_mark == "-1":
        print("Please make sure your number grade is valid or capitalized.")
    else:
        print("{}%".format(new_mark))


if __name__ == "__main__":
    main()
