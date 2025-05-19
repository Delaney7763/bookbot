def get_book_text(path):

        with open(path) as f:
                file_contents = f.read()
        return file_contents

def get_num_words(path):
        text = get_book_text(path)
        num_words = len(text.split())
        print(f"Found {num_words} total words")

def character_count(path):
	text = get_book_text(path)
	lowercase = text.lower()
	char_frequency = {}

	for char in lowercase:
		if char in char_frequency:
			char_frequency[char] += 1
		else:
			char_frequency[char] = 1
	return char_frequency

def sort_on(dict):
	return dict["num"]

def dict_to_list_of_dicts(input_dict):
	dict_list = [{"char": key, "num": value} for key, value in input_dict.items()]
	dict_list.sort(reverse=True, key=sort_on)
	return dict_list
