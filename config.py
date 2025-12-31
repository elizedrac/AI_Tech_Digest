import os

NEWS_API_KEY = os.environ["NEWS_API_KEY"]
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

AI_KEYWORDS = {
    # Core AI concepts (high signal)
    "artificial intelligence": 5,
    "machine learning": 4,
    "deep learning": 4,
    "large language model": 5,
    "llm": 4,
    "foundation model": 4,

    # Major AI labs / companies
    "openai": 5,
    "google deepmind": 5,
    "anthropic": 5,
    "meta ai": 4,
    "microsoft ai": 4,
    "nvidia": 4,

    # Models & architectures
    "gpt": 4,
    "chatgpt": 3,
    "gemini": 3,
    "claude": 3,
    "transformer": 3,

    # Chips & infrastructure
    "gpu": 3,
    "ai chip": 3,
    "semiconductor": 3,
    "data center": 2,
    "compute": 2,

    # Policy / regulation (important but less technical)
    "ai regulation": 3,
    "ai policy": 2,
    "antitrust": 2,

    # Business & ecosystem
    "ai startup": 2,
    "venture capital": 1,
    "funding round": 1,
    "acquisition": 1,
}

SOURCE_WEIGHTS = {
    # Tier 1: Deep technical + industry-accurate
    "Reuters": 5,
    "Bloomberg": 5,
    "Financial Times": 5,

    # Tier 2: Strong reporting, less technical depth
    "The New York Times": 4,
    "The Wall Street Journal": 4,

    # Tier 3: Tech-focused but lighter analysis
    "The Verge": 3,
    "TechCrunch": 3,
    "Wired": 3,

    # Tier 4: General tech news / aggregators
    "Ars Technica": 2,
    "Engadget": 2,
    "ZDNet": 2,

    # Tier 5: Blogs / unknowns handled by default = 1
}



