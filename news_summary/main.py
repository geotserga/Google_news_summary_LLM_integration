import argparse
from dotenv import load_dotenv

from datetime import datetime
from news_extractor import get_articles, filter_articles
from news_summarizer import get_news_summary
from slack import send_slack_notification


def main():
    date = datetime.today().strftime('%Y-%m-%d')  
    articles = get_articles(category="technology", country="us")
    filtered_articles = filter_articles(articles)
    summary = get_news_summary(filtered_articles)
    send_slack_notification(date, summary)

# Runs only if the script is executed directly (not imported as a module)

if __name__ == "__main__":
    main()


def main(date, category, country):
    articles = get_articles(category=category, country=country)
    filtered_articles = filter_articles(articles)
    summary = get_news_summary(filtered_articles)
    send_slack_notification(date, summary)


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Get news summary and send a Slack notification.")

    # Adding arguments for date, category, and country where the user can specify them
    parser.add_argument('--date', type=str, default=datetime.today().strftime( 
        '%Y-%m-%d'), help="The date for the news summary (default: today)")
    parser.add_argument('--category', type=str, default="technology",
                        help="The news category (default: technology)")
    parser.add_argument('--country', type=str, default="us",
                        help="The country for the news (default: us)")

    # Parse arguments
    args = parser.parse_args()

    # Call the main function with arguments
    main(args.date, args.category, args.country)

# Example to run it in terminal with
 # python .\main.py --category sports
