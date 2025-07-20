import pandas
file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {row.letter: row.code for (index, row) in file.iterrows()}
user_input = input("Enter the word to encode: ").upper()
nato_list = [nato_dic[words] for words in user_input if words != " "]
print(nato_list)