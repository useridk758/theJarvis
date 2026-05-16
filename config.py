import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'jarvis-dev-secret')
    GITHUB_API_URL = 'https://api.github.com'
    HN_API_URL = 'https://hacker-news.firebaseio.com/v0'
