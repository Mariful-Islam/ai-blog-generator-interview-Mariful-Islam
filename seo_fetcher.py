import random


def fetch_seo_metrics(keyword: str)->dict:
    return {
        "keyword": keyword,
        "search_volume": random.randint(10000, 9000000),
        "keyword_difficulty": random.randint(10, 60),
        "avg_cpc": round(random.uniform(0.5, 5.0), 2)
    }