import typer
from youtube_transcript_api import YouTubeTranscriptApi

app = typer.Typer()

def get_transcript(video_id: str) -> str:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([entry['text'] for entry in transcript])

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.command()
def transcript(video_id: str):
    """
    Get the transcript of a YouTube video.
    """
    transcript_text = get_transcript(video_id)
    typer.echo(transcript_text)


if __name__ == "__main__":
    app()
