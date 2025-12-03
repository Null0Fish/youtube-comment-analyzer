import json


def clean_entity_sentiments(video_id):
    raw_file_path = f'./data/entities/raw_entities/{video_id}.json'
    output_file_path = f'./data/entities/processed_entities/{video_id}.json'

    with open(raw_file_path, 'r') as file:
        data = json.load(file)
        filtered_data = {
            key: value for key, value in data.items() if value['average_score'] != 0.0
        }
        with open(output_file_path, 'w') as output_file:
            json.dump(filtered_data, output_file, ensure_ascii=False, indent=2)
