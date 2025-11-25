import json
from openai import OpenAI


def get_news_summary(articles):
    client = OpenAI()
    prompt = f"Summarize in one small paragraph (100 words) the following news articles: {articles}"
    try:
        summary = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {
                    "role": "user",
                            "content": prompt
                }
            ]
        )
        summary = summary.choices[0].message.content
    except Exception as e:
        print(f"Error summarizing article: {e}")
    return summary
