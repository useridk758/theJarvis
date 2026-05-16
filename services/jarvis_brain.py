import datetime
from services.math_solver import solve_math
from services.news_service import get_top_news
from services.github_service import search_github

class JarvisBrain:
    """Parses natural language and routes to the correct backend service."""

    def process(self, text: str):
        cmd = text.lower().strip()

        # Mathematics
        if self._looks_like_math(cmd):
            expr = self._extract_math(cmd)
            result = solve_math(expr)
            if result is not None:
                return {
                    'type': 'math',
                    'message': f'The answer is {result}',
                    'result': result
                }

        # Greeting
        if any(g in cmd for g in ['hello', 'hi jarvis', 'hey jarvis', 'greetings']):
            return {
                'type': 'greeting',
                'message': 'Hello sir. I am Jarvis, your personal assistant. How may I help you today?'
            }

        # Time
        if 'time' in cmd:
            now = datetime.datetime.now().strftime('%I:%M %p')
            return {'type': 'time', 'message': f'The current time is {now}'}

        # Date
        if 'date' in cmd and 'update' not in cmd:
            today = datetime.datetime.now().strftime('%A, %B %d, %Y')
            return {'type': 'date', 'message': f"Today's date is {today}"}

        # News
        if any(k in cmd for k in ['news', 'headlines', 'latest news']):
            links = get_top_news()
            return {
                'type': 'news',
                'message': 'Opening the latest news in new tabs, sir.',
                'links': links
            }

        # GitHub trending
        if 'trending' in cmd:
            return {
                'type': 'redirect',
                'message': 'Opening GitHub trending repositories.',
                'url': 'https://github.com/trending'
            }

        # GitHub search
        if 'search github' in cmd:
            q = cmd.replace('search github', '').replace('for', '').strip()
            if q:
                results = search_github(q)
                return {
                    'type': 'github_search',
                    'message': f'Searching GitHub for {q} and opening top results.',
                    'query': q,
                    'results': results
                }
            return {'type': 'github_search', 'message': 'What should I search for on GitHub?'}

        # Open GitHub
        if 'open github' in cmd:
            return {'type': 'redirect', 'message': 'Opening GitHub.', 'url': 'https://github.com'}

        # Help
        if any(k in cmd for k in ['help', 'what can you do', 'commands']):
            return {
                'type': 'help',
                'message': 'I can open latest news, solve math, tell the time and date, open GitHub, search GitHub, and respond to your voice commands.'
            }

        # Unknown / fallback
        return {
            'type': 'unknown',
            'message': "I'm not sure I understood, sir. Try asking me to open news, solve math, or search GitHub."
        }

    def _looks_like_math(self, cmd: str) -> bool:
        has_keyword = any(k in cmd for k in ['math', 'calculate', 'solve', 'what is', 'plus',](streamdown:incomplete-link)
