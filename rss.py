import os
from dotenv import load_dotenv
import feedparser
from pathlib import Path
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Load environment variables
load_dotenv()

# Define constants
FEED_URL = "[INPUT YOUR FEED URL]"

def fetch_news_feed(url):
    """Parse the news feed and return articles."""
    return feedparser.parse(url)['entries']

def generate_summary(input_text):
    """Generate a summary for the given news article."""
    chat = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0125")
    messages = [
        SystemMessage(content="あなたは世界最高のニュースキャスターです。"),
        HumanMessage(content="これからあるウェブニュースのHTML情報をインプットします。このニュースの内容をわかりやい日本語で伝えるニュース原稿を300文字以内で書いてください。"),
        AIMessage(content="わかりました。HTMLを入力してください。"),
        HumanMessage(content=input_text),
    ]
    return chat.invoke(messages).content

def create_audio_from_text(text, file_path):
    """Generate an audio file from the given text."""
    client = OpenAI()
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(file_path)

def main():
    articles = fetch_news_feed(FEED_URL)
    audio_text = ""

    for article in articles:
        if len(article.content[0].value) > 30000:
            continue

        article_info = "Title: {}\nSummary: {}\nPublished At: {}\n".format(
            article.title, article.summary, article.published)
        input_text = "Title: {}\nSummary: {}\nPublished At: {}\nContent: {}".format(
            article.title, article.summary, article.published, article.content[0].value)

        summary = generate_summary(input_text)
        print(article_info + "Summary: " + summary)
        audio_text += article_info + summary + "\n"

    speech_file_path = Path(__file__).parent / "news.mp3"
    create_audio_from_text(audio_text, speech_file_path)

if __name__ == "__main__":
    main()

