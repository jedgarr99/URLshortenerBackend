from flask import  request, jsonify, redirect
from .models import db, URL
import string
import random

def shorten_url():
    """
    Shorten a URL
    ---
    tags:
      - URL Shortener
    parameters:
      - name: url
        in: body
        type: string
        required: true
        description: The URL to be shortened
        schema:
          type: object
          required:
            - url
          properties:
            url:
              type: string
              example: "http://example.com"
    responses:
      200:
        description: A shortened URL
        schema:
          type: object
          properties:
            short_url:
              type: string
              example: "http://localhost:5000/abcd1234"
      400:
        description: Invalid input
    """
    data = request.get_json()
    original_url = data['url']

    prefix='https://ur-lshortener-beryl.vercel.app/'
    ending=''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    short_url = prefix+ending

    new_url = URL(original_url=original_url, short_url=ending)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({"short_url": short_url})


def redirect_url(short_url):
    """
    Redirect to original URL
    ---
    tags:
      - URL Shortener
    parameters:
      - name: short_url
        in: path
        type: string
        required: true
        description: The shortened URL part
    responses:
      302:
        description: Redirects to the original URL
      404:
        description: Shortened URL not found
    """
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)