from google.cloud import language_v1
import json
import emoji


def analyze_entity_sentiment(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(
        content=text,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = client.analyze_entity_sentiment(request={'document': document})
    entities = response.entities
    return entities


def decode_emojis(comment):
    return emoji.demojize(comment)


def find_entity_sentiment(video_id):
    comments_file = f'./data/comments/processed_comments/{video_id}.txt'
    with open(comments_file, 'r', encoding='utf-8') as file:
        comments = file.readlines()

    entity_sentiments_per_comment = []
    for comment in comments:
        entities = analyze_entity_sentiment(comment)
        entity_sentiments_per_comment.append(entities)
    all_entity_sentiments = [entity for entities in entity_sentiments_per_comment for entity in entities]
    entity_scores_count = {}
    for entity in all_entity_sentiments:
        entity_name = entity.name
        if not contains_emojis(entity_name):
            entity_key = (entity_name, entity.type_)
            if entity_key not in entity_scores_count:
                entity_scores_count[entity_key] = {'score_sum': 0, 'count': 0}
            entity_scores_count[entity_key]['score_sum'] += entity.sentiment.score
            entity_scores_count[entity_key]['count'] += 1

    averaged_entity_sentiments = {}
    for entity_key, scores_count in entity_scores_count.items():
        average_score = scores_count['score_sum'] / scores_count['count']
        averaged_entity_sentiments[entity_key] = {
            'name': entity_key[0],
            'type': entity_key[1],
            'average_score': average_score
        }
    decoded_entity_sentiments = {}
    for entity_key, sentiment_data in averaged_entity_sentiments.items():
        decoded_entity_name = decode_emojis(entity_key[0])
        decoded_entity_sentiments[decoded_entity_name] = sentiment_data

    output_file_path = f'./data/entities/raw_entities/{video_id}.json'
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(decoded_entity_sentiments, output_file, ensure_ascii=False, indent=2)


def contains_emojis(text):
    return bool(emoji.emoji_count(text))
