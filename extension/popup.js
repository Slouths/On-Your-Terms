// Set the default language to English
let currentLanguage = 'en';

// Wait for the DOM content to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Get references to important DOM elements
    const languageSelect = document.getElementById('language-select');
    const sendUrlButton = document.getElementById("send-url");
    const resultsDiv = document.getElementById('results');

    // Set up language selection functionality
    if (languageSelect) {
        languageSelect.addEventListener('change', (event) => {
            // Update the current language when the user selects a new one
            currentLanguage = event.target.value;
        });
    }

    // Set up the main functionality for the "send URL" button
    if (sendUrlButton) {
        sendUrlButton.addEventListener("click", () => {
            // Add a click animation to the button
            sendUrlButton.style.transform = "scale(0.95)";
            setTimeout(() => {
                sendUrlButton.style.transform = "scale(1)";
            }, 100);

            // Show a loading message while fetching the summary
            resultsDiv.innerHTML = '<p>Loading summary...</p>';

            // Get the URL of the current active tab
            chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
                const currentTab = tabs[0].url;

                // Send a request to the backend server
                fetch('http://127.0.0.1:5000/receive-url', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ url: currentTab, language: currentLanguage }),
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === "success") {
                        console.log('Terms link found:', data.terms_link);
                        console.log('Summary:', data.summary);
                        displayResults(data.terms_link, data.summary);
                    } else {
                        console.error('Error:', data.message);
                        displayError(data.message);
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                    displayError("An error occurred while processing the request.");
                });
            });
        });
    }
});

function displayResults(termsLink, summary) {
    const resultsDiv = document.getElementById('results');

    // Parse the summary into sections
    const sections = parseSummary(summary);

    let summaryHTML = '';
    sections.forEach(section => {
        summaryHTML += `
            <div class="summary-section">
                <h4>${section.title}</h4>
                <p>${section.content}</p>
            </div>
        `;
    });

    resultsDiv.innerHTML = `
        <h3>Terms Link:</h3>
        <p><a href="${termsLink}" target="_blank">${termsLink}</a></p>
        <h3>Summary:</h3>
        <div class="summary-container">${summaryHTML}</div>
    `;
}

// Function to parse the summary into sections
function parseSummary(summary) {
    const lines = summary.split('\n');
    const sections = [];
    let currentSection = null;

    // Loop through each line in the summary
    lines.forEach(line => {
        if (line.trim() === '') return; // Skip empty lines

        // Check if the line contains a colon, indicating a new section
        if (line.includes(':')) {
            // This line is likely a title
            if (currentSection) sections.push(currentSection);
            currentSection = { title: line.trim(), content: '' };
        } else if (currentSection) {
            // This line is content for the current section
            currentSection.content += line.trim() + ' ';
        }
    });

    if (currentSection) sections.push(currentSection);
    return sections;
}

function displayError(message) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `<p style="color: red;">Error: ${message}</p>`;
}