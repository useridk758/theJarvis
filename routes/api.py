from flask import Blueprint, request, jsonify
from services.jarvis_brain import JarvisBrain

api_bp = Blueprint('api', __name__)
brain = JarvisBrain()

@api_bp.route('/command', methods=['POST'])
def command():
    data = request.get_json() or {}
    text = data.get('text', '')
    result = brain.process(text)
    return jsonify(result)
