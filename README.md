# Google news summary - LLM integration

This project automatically fetches the latest news from NewsAPI, filters the retrieved articles, generates a concise summary using OpenAI, and sends the summary to a Slack channel.

## 📂 Project Structure

🔸 main.py
The main orchestrator script. It retrieves articles, filters them, generates a summary, and sends it to Slack.

🔸 news_extractor.py
Handles communication with the NewsAPI and returns filtered article metadata.

🔸 news_summarizer.py
Uses OpenAI GPT to generate a 100-word summary of the news articles.

🔸 slack.py
Sends the generated summary to Slack using an incoming webhook.

## 🚀 How It Works

- Fetches headlines from NewsAPI based on category and country
- Extracts title, description, and content fields
- Sends the aggregated articles to OpenAI for summarization
- Formats and posts the summary to Slack

## 🔑 Environment Variables

Create a .env file in the root directory:

NEWS_API_KEY=your_news_api_key
OPENAI_API_KEY=your_openai_api_key
SLACK_WEBHOOK_URL=your_slack_webhook_url


These keys are required for:
- Fetching news
- Generating summaries
- Sending Slack notifications
