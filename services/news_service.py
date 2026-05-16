import requests

def get_top_news(limit=5):
    """
    Fetch latest stories from the Hacker News API.
    Falls back to curated links if the API fails.
    """
    try:
        resp = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json', timeout=6)
        story_ids = resp.json()[:limit]
        stories = []
        for sid in story_ids:
            item_resp = requests.get(
                f'https://hacker-news.firebaseio.com/v0/item/{sid}.json', timeout=6
            )
            item = item_resp.json()
            stories.append({
                'title': item.get('title', 'Story'),
                'url': item.get('url') or f'https://news.ycombinator.com/item?id={sid}'
            })
        return stories
    except Exception:
        return [
            {'title': 'Hacker News', 'url': 'https://news.ycombinator.com'},
            {'title': 'GitHub Trending', 'url': 'https://github.com/trending'},
            {'title': 'TechCrunch', 'url': 'https://techcrunch.com'},
        ]
