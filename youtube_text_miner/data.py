from typing import List
import csv
import json
from argparse import ArgumentParser
from pathlib import Path

from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi


def get_youtube_video_ids(keyword: str, limit: int = 10) -> List[str]:
    """
    Returns list of video ids we find for the given 'keyword'
    """
    video_search = VideosSearch(keyword, limit=limit)
    results = video_search.result()['result']
    return [r['id'] for r in results]


def get_youtube_video_transcript(video_id: str) -> str:
    """"
    Returns transcript of the given 'video_id'
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['en-US', 'en']
        )
        utterances = [p['text'] for p in transcript]
        return ' '.join(utterances)

    except Exception as e:
        pass


def save_transcripts(transcripts: List[str], keyword: str, path: Path):
    """
    Stores locally in file the transcripts with associated keyword
    """
    output = [{'keyword': keyword, 'text': t} for t in transcripts if t is not None]

    # check if path points to a csv or a json file
    if path.suffix == '.csv':
        # save as csv
        keys = output[0].keys()
        with open(path, 'w', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(output)

    else:
        # save as json
        with open(path, 'w') as output_file:
            json.dump(output, output_file)


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--keyword', type=str, required=True)
    parser.add_argument('--n_samples', type=int, default=100)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()

    video_ids = get_youtube_video_ids(keyword=args.keyword, limit=args.n_samples)

    transcripts = [get_youtube_video_transcript(id) for id in video_ids]

    save_transcripts(transcripts, args.keyword, args.output)
