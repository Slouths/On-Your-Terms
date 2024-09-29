let currentLanguage = 'en';

document.addEventListener('DOMContentLoaded', function() {
    const languageSelect = document.getElementById('language-select');
    const sendUrlButton = document.getElementById("send-url");
    const resultsDiv = document.getElementById('results');

    if (languageSelect) {
        languageSelect.addEventListener('change', (event) => {
            currentLanguage = event.target.value;
        });
    }

    if (sendUrlButton) {
        sendUrlButton.addEventListener("click", () => {
            // Click animation
            sendUrlButton.style.transform = "scale(0.95)";
            setTimeout(() => {
                sendUrlButton.style.transform = "scale(1)";
            }, 100);

            // Show loading message
            resultsDiv.innerHTML = '<p>Loading summary...</p>';

            chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
                const currentTab = tabs[0].url;

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

function parseSummary(summary) {
    const lines = summary.split('\n');
    const sections = [];
    let currentSection = null;

    lines.forEach(line => {
        if (line.trim() === '') return; // Skip empty lines

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