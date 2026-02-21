from fetch_news import fetch_articles
from rank import score_article
from email_digest import send_email

def main():
    articles = fetch_articles()

    # dedupe by normalized title (fallback to url) while preserving order
    seen = set()
    deduped = []
    for article in articles:
        title = (article.get("title") or "").strip()
        url = (article.get("url") or "").strip()
        norm_title = " ".join(title.lower().split())
        norm_url = url.split("?", 1)[0].lower()
        key = norm_title or norm_url
        if key and key not in seen:
            seen.add(key)
            deduped.append(article)

    ranked = sorted(deduped, key=score_article, reverse=True)
    
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

