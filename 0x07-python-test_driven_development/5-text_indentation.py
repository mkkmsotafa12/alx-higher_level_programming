#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """
    Write a function that prints a text 
    with 2 new lines after each of these
    characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = ""
    for char in text:
        new_line += char
        if char in ".?:":
            formatted_line = new_line.strip()

            print(formatted_line)
            print("")


            new_line = ""


    if new_line:
        formatted_line = new_line.strip()
        print(formatted_line, end="")
