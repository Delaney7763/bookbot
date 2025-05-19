import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
path = sys.argv[1]

from stats import get_num_words

from stats import character_count

characters = character_count(path)

from stats import dict_to_list_of_dicts

character_dict_list = dict_to_list_of_dicts(characters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
get_num_words(path)
print("--------- Character Count -------")
for item in character_dict_list:
	if item["char"].isalpha() == True:
		print(f"{item["char"]}: {item["num"]}")
print("============= END ===============")
