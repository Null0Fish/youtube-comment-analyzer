import json


def main():
    output_file = '../dictionaries/slang_dict.json'
    filter_slang_dict(output_file)


def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def filter_slang_dict(output_file):
    english_dict_file_path = '../dictionaries/full_english_dict.json'
    slang_dict_file_path = '../dictionaries/full_slang_dict.json'

    english_dict = load_dictionary(english_dict_file_path)
    slang_dict = load_dictionary(slang_dict_file_path)
    filtered_slang_dict = {key: value for key, value in slang_dict.items() if key.lower() not in english_dict}
    with open(output_file, 'w') as file:
        json.dump(filtered_slang_dict, file, indent=2)


if __name__ == '__main__':
    # main()
    # DO NOT RUN THIS NEW WORDS HAVE BEEN ADDED TO DICT (mf)
    pass
