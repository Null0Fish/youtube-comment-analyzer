from googleapiclient.discovery import build
from credentials.youtube_api_key import YOUTUBE_API_KEY


def fetch_comments(video_id):
    youtube_service = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    video_comment_params = {
        'part': 'snippet',
        'videoId': video_id,
        'maxResults': 100
    }

    try:
        video_comments = request_comments(youtube_service, **video_comment_params)

        # Save valid comments to a text file in the data directory
        output_file = f'./data/comments/raw_comments/{video_id}.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            for comment in video_comments:
                if isinstance(comment, str):
                    file.write(comment + '\n')
                else:
                    print(f"Skipping invalid comment: {comment}")
    except Exception as e:
        print(f"Error while fetching or writing comments: {e}")


def request_comments(youtube, **kwargs):
    comments = []

    while True:
        results = youtube.commentThreads().list(**kwargs).execute()

        for item in results['items']:
            comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment_text)

        # Check if there are more pages of comments
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
        else:
            break

    return comments
