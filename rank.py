from datetime import datetime
from config import AI_KEYWORDS, SOURCE_WEIGHTS

def score_article(article):
    score = 0
    text = (article["title"] + " " + (article.get("description") or "")).lower()

    for keyword, weight in AI_KEYWORDS.items():
        if keyword in text:
            score += weight

    source = article["source"]["name"]
    score += SOURCE_WEIGHTS.get(source, 1)

    # adhere to only news articles
    for keyword in EXCLUDE_KEYWORDS:
        if keyword in text:
            return 0

    published = datetime.fromisoformat(article["publishedAt"].replace("Z", ""))
    hours_old = (datetime.utcnow() - published).total_seconds() / 3600

    if hours_old < 24:
        score += 3
    elif hours_old < 48:
        score += 1

    return score
