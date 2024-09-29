# On-Your-Terms 📜✨

**LEGALEASE** is a powerful Chrome extension that finds the terms of service during registration and summarizes it into clear, concise language. Leverage cutting-edge AI to understand exactly what you're agreeing to, **without the legalese**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 👥 Authors

- [Patrick Davenport](https://github.com/monochromatrick)
  <br><sub>Discord: monochromatrick</sub>

- [Taher Akolawala](https://github.com/TaherA51)
  <br><sub>Discord: permameme</sub>

- [Chris Garate](https://github.com/GheeMann)
  <br><sub>Discord: gheeman</sub>

- [Nicholas Nunez](https://github.com/Slouths)
  <br><sub>Discord: slouths</sub>

## 🚀 Features

### Effortless Navigation Through Legal Jargon 📖

* **Simplified Summaries:** Get the gist of lengthy terms of service during registration in a flash.
* **Plain Language Explanations:** Demystify complex terms with easy-to-understand definitions.
* **Multilingual Support:** Access summaries in English, Spanish, and Haitian Creole.
* **Seamless Chrome Integration:** Effortlessly analyze webpages where ToS is hidden or hard to find directly within your browser.

## 🛠️ Built with Cutting-Edge Technology

* **AI-Powered Insights:** Google Gemini API delivers accurate and insightful legal summaries .
* **Modern Development Stack:** Built with industry-standard tools for optimal performance and scalability.

## 🔍 Under the Hood: A Deep Dive

### Tech Stack

* **Frontend:** HTML, CSS, JavaScript 
* **Backend:** Python, Flask 
* **AI:** Google Gemini API
* **Chrome Extension:** Chrome Extension API
* **Deployment:** Locally Hosted

### Development Journey

1. **Effortless Chrome Extension Setup:** A concise guide on creating the Chrome extension structure.
2. **AI Integration Made Simple:** Instructions on incorporating the Google Gemini API for legal analysis.
3. **Streamlined Backend Development:** Explanation of the backend logic for processing user requests and interacting with the AI model.
4. **Intuitive User Interface Design:** Best practices for designing a user-friendly Chrome extension interface.

## 💪 Challenges Overcome, Solutions Delivered

| Challenge | Solution |
|-----------|----------|
| Making web scraper to find ToS | We troubleshooted the URL endpoints to make sure the correct connections were being made. |
| Getting hosting to work | We removed specific versions from certain libraries and backtraced to find the correct versions that would allow us to successfully host. |
| Connecting the extension and webpage to the backend | We all contributed to writing the code to connect the extension to the backend through the use of GitHub and communicating non-stop to ensure that the code was working. |

## 🧠 Lessons Learned for Future Iterations

- Consistent GitHub commits are crucial: We should have started committing through GitHub consistently from the beginning. This oversight created numerous issues when merging our contributions later, especially as we approached the project deadline.

- Documentation is key: More thorough documentation throughout the development process would have been beneficial. This aligns with the first issue, as we found ourselves backtracing significantly to reconstruct our documentation history.

- Early skill assessment and Git proficiency: Identifying team members' strengths earlier and improving our collective knowledge of Git could have saved considerable time during the final collaboration stages of the project.

## ✨ Envisioning the Future: Planned Features

- [ ] Remote hosted servers via AWS or Google Cloud Services to run 24/7
- [ ] Ability for user to enter their own API key so as to not overload individual API key used for project. 
- [ ] Pagination: Extension will have different pages to store past ToS(s) that have been agreed to by the user for reviewal.


## 🛠️ Local Development Setup
- To run locally, create a .env file within the On-Your-Terms project file. Within this file create a variable called GOOGLE_API_KEY and set that equal to your own custom Gemini API key that can be found at https://aistudio.google.com/app/apikey.
- NOTE: .env FILE WITH PERSONAL API KEY WILL BE STORED WITHIN REPO FOR THE DURATION OF HACKATHON. THEREFORE THE STEPS ABOVE MAY BE IGNORED DURING HACKATHON.

