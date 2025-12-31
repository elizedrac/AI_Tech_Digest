import os

NEWS_API_KEY = os.environ["NEWS_API_KEY"]
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


AI_KEYWORDS = {
    "openai": 5,
    "google deepmind": 5,
    "anthropic": 5,
    "nvidia": 4,
    "artificial intelligence": 4,
    "machine learning": 3,
    "llm": 3,
    "ai regulation": 3,
    "chip": 2,
    "startup": 1,
}

SOURCE_WEIGHTS = {
    "Reuters": 5,
    "Bloomberg": 5,
    "The New York Times": 4,
    "The Verge": 3,
    "TechCrunch": 3,
}


