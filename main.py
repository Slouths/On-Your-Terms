"""
This program scrapes a specified URL (in this case, an Adobe login page) to find
the first link containing the word 'Terms'. If found, it prints the URL of that link
and then scrapes and prints the content from that link. The program uses Selenium
for dynamic web scraping and BeautifulSoup for parsing the scraped content.
"""

from webScraping import find_term_link, scrape_content_from_link
from dotenv import load_dotenv
import os
import google.generativeai as genai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS


load_dotenv()  # This loads the variables from .env
api_key = os.getenv('API_KEY')

app = Flask(__name__)
CORS(app, resources={r"/receive-url": {"origins": "*"}})  # This allows CORS for all domains on all routes



@app.route('/receive-url', methods=['POST'])
def receiveurl():
    data = request.get_json()
    url = data.get('url')
    print(f'Received URL: {url}')
    return jsonify({"status": "success", "urlreceived": url})

# Step 5: Example usage
if __name__ == "__main__":
    # = 'https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fhomepage_milo%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%3A%2F%2Fwww.adobe.com%2Fhome%23old_hash%3D%26from_ims%3Dtrue%3Fclient_id%3Dhomepage_milo%26api%3Dauthorize%26scope%3DAdobeID%2Copenid%2Cgnav%2Cpps.read%2Cfirefly_api%2Cadditional_info.roles%2Cread_organizations%26state%3D%7B%22jslibver%22%3A%22v2-v0.45.0-8-gd14e654%22%2C%22nonce%22%3A%227424714071001927%22%7D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=homepage_milo&scope=AdobeID%2Copenid%2Cgnav%2Cpps.read%2Cfirefly_api%2Cadditional_info.roles%2Cread_organizations&state=%7B"jslibver"%3A"v2-v0.45.0-8-gd14e654"%2C"nonce"%3A"7424714071001927"%7D&relay=00bc0846-25f4-45d6-91a3-c91343dc14e8&locale=en_US&flow_type=token&idp_flow_type=login&s_p=google%2Cfacebook%2Capple%2Cmicrosoft%2Cline&response_type=token&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fwww.adobe.com%2Fhome%23old_hash%3D%26from_ims%3Dtrue%3Fclient_id%3Dhomepage_milo%26api%3Dauthorize%26scope%3DAdobeID%2Copenid%2Cgnav%2Cpps.read%2Cfirefly_api%2Cadditional_info.roles%2Cread_organizations&use_ms_for_expiry=true#/'
    # result = find_term_link(receiveurl())

    # if result:
    #     print(f"Found link containing 'Terms': {result}")
    #     print(scrape_content_from_link(result))
    # else:
    #     print("No link containing 'Terms' found")
    app.run(debug=True)


    # genai.configure(api_key=api_key)
    # model = genai.GenerativeModel("gemini-1.5-flash")
    # response = model.generate_content("Write a story about a magic backpack.")
    # print(response.text) 
