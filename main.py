from fetch_news import fetch_articles
from rank import score_article
from email_digest import send_email

def main():
    articles = fetch_articles()
    ranked = sorted(articles, key=score_article, reverse=True)

    lines = []
    for i, article in enumerate(ranked[:3], 1):
        lines.append(f"{i}. {article['title']}")
        lines.append(article["url"])
        lines.append("")

    body = "\n".join(lines)

    send_email(
        subject="Daily AI & Tech Digest",
        body=body
    )

if __name__ == "__main__":
    main()

