from flask import Blueprint, jsonify

"""
    health check
    
    from config flask [+-]
    
    models with schemas
    
    views with logic
"""

common_bp = Blueprint('common_bp', __name__)


@common_bp.route('/')
def home():
    response = {"status": "ok"}
    return jsonify(response)
