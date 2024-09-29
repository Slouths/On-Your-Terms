let currentLanguage = 'en';

document.getElementById('language-select').addEventListener('change', (event) => {
    currentLanguage = event.target.value;
});

document.getElementById("send-url").addEventListener("click", () => {
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

function displayResults(termsLink, summary) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <h3>Terms Link:</h3>
        <p><a href="${termsLink}" target="_blank">${termsLink}</a></p>
        <h3>Summary:</h3>
        <div>${summary}</div>
    `;
}

function displayError(message) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `<p style="color: red;">Error: ${message}</p>`;
}