#########################
#### Working Version ####
#########################
# If editing in the future, please change the verison number and final print statement (line number statement) accordingly.
# idk if this actually works as CeWL does or not, but I got tired of waiting an hour for CeWL to make a simple wordlist.
print("##################################################")
print("#### ECPI University's NCL Wordlist Generator ####")
print("##################################################")
print("Created by saintnik")
print("Version 1.0.2\n")
print("Make sure that you go into your C drive and create a file called 'Wordlists'")
print("If you do not have the file C:\Wordlists, modify the code on line 60 for your desired output\n")

import os
import re

def generate_wordlist(data, min_length=3, max_length=15, include_numbers=True):
    # extract words using regular expression
    words = re.findall(r'\b\w+\b', data)

    # filter words based on length and whether to include numbers
    if include_numbers:
        words = [w.lower() for w in words if min_length <= len(w) <= max_length]
    else:
        words = [w.lower() for w in words if min_length <= len(w) <= max_length and not any(c.isdigit() for c in w)]

    return words


def write_wordlist(words, file_path):
    # write the wordlist to a file
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')


if __name__ == '__main__':
    # get user input for the link to be wordlisted
    link = input("Enter the link to be wordlisted: ")

    # get user input for the minimum character count of the words
    min_length = int(input("Enter the minimum character count of the words: "))

    # get user input for whether to include numbers in the wordlist
    include_numbers = input("Include numbers in the wordlist? (y/n): ").lower() == 'y'

    # get user input for the output file name
    output_name = input("Enter the name of the output file (without .txt extension): ")

    # fetch the webpage data
    import requests

    response = requests.get(link)
    data = response.text

    # generate the wordlist
    words = generate_wordlist(data, min_length=min_length, include_numbers=include_numbers)

    # specify the output directory path
    output_dir = 'C:/Wordlists'

    # write the wordlist to a file in the output directory
    output_file = os.path.join(output_dir, output_name + '.txt')
    write_wordlist(words, output_file)

    print(f"Wordlist generated successfully and saved to {output_file}")
