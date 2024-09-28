from webScraping import find_term_link, scrape_content_from_link
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/receive-url', methods=['POST'])
def receiveurl():
    data = request.get_json()
    url = data.get('url')
    print(f'Received URL: {url}')
    
    # Find the 'Terms' link
    terms_link = find_term_link(url)
    
    if terms_link:
        # Scrape content from the 'Terms' link
        content = scrape_content_from_link(terms_link)
        return jsonify({
            "status": "success",
            "terms_link": terms_link,
            "content": content
        })
    else:
        return jsonify({
            "status": "error",
            "message": "No 'Terms' link found"
        })

if __name__ == "__main__":
    app.run(debug=True)