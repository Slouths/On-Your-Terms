from webScraping import find_term_link, scrape_content_from_link
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
from gemini import summarize_content

load_dotenv()  # Load environment variables
api_key = os.getenv('API_KEY')

app = Flask(__name__)
CORS(app)

# Route to receive the URL and language from the extension
@app.route('/receive-url', methods=['POST'])
def receiveurl():
    data = request.get_json()
    url = data.get('url')
    language = data.get('language', 'en')
    print(f'Received URL: {url}, Language: {language}')

    # Find the 'Terms' link
    terms_link = find_term_link(url)

    if terms_link:
        # Scrape content from the 'Terms' link
        content = scrape_content_from_link(terms_link)
        # Summarize the content in the specified language
        summary = summarize_content(content, language)
        return jsonify({
            "status": "success",
            "terms_link": terms_link,
            "summary": summary
        })
    else:
        return jsonify({
            "status": "error",
            "message": "No 'Terms' link found"
        })


if __name__ == "__main__":
    app.run(debug=True)