import requests
from config import Config

def search_github(query: str, per_page: int = 5):
    """
    Search GitHub repositories using the public search API.
    """
    if not query:
        return []
    try:
        url = f"{Config.GITHUB_API_URL}/search/repositories"
        headers = {'Accept': 'application/vnd.github.v3+json'}
        params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': per_page}
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        data = resp.json()
        items = data.get('items', [])
        return [
            {
                'name': item['full_name'],
                'url': item['html_url'],
                'stars': item.get('stargazers_count', 0),
                'description': (item.get('description') or '')[:120]
            }
            for item in items
        ]
    except Exception:
        return []
