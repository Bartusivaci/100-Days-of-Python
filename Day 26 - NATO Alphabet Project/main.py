
# Made to understand DataFrame, List and Dictionary Comprehension

import pandas

phonetic_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter:row.code for (index, row) in phonetic_dataframe.iterrows()}

user_input = input("Enter a word: ").upper()

output_list = [phonetic_dictionary[letter] for letter in user_input if letter in phonetic_dictionary]
print(output_list)