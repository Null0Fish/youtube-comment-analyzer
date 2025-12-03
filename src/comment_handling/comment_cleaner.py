import json
import html
import re


def clean_comments(video_id):
    with open(f'./data/comments/raw_comments/{video_id}.txt', 'r', encoding='utf-8') as file:
        comments = [line.strip() for line in file]

    cleaned_comments = [
        clean_comment(comment)
        for comment in comments
    ]

    with open(f'./data/comments/processed_comments/{video_id}.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_comments))


def clean_comment(comment):
    comment = remove_tags(comment)
    comment = comment.lower()
    comment = convert_phrases(comment)
    return comment


def remove_tags(comment):
    return re.sub(r'<[^>]*>', '', html.unescape(comment))


def load_phrases(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def convert_phrases(input_string):
    phrase_file_path = './dictionaries/slang_dict.json'
    phrases_dict = load_phrases(phrase_file_path)
    for phrase, meaning in phrases_dict.items():
        # Use regular expression with word boundaries and check for no letter characters before or after
        pattern = re.compile(r'\b' + re.escape(phrase) + r'\b', re.IGNORECASE)
        input_string = re.sub(pattern, meaning, input_string)
    return input_string
