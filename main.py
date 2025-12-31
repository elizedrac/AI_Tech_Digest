from fetch_news import fetch_articles
from rank import score_article

def main():
    articles = fetch_articles()
    ranked = sorted(articles, key=score_article, reverse=True)

    print("\nTop AI & Tech Stories Today:\n")
    for i, article in enumerate(ranked[:5], 1):
        title = article["title"]
        url = article["url"]
        score = score_article(article)

        print(f"{i}. ({score}) {title}")
        print(f"   🔗 {url}\n")

if __name__ == "__main__":
    main()
