document.getElementById("send-url").addEventListener("click", () => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        const currentTab = tabs[0].url;

        fetch('http://127.0.0.1:5000/receive-url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: currentTab }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                console.log('Terms link found:', data.terms_link);
                console.log('Content:', data.content);
                // You can update the popup HTML here to display the results
                displayResults(data.terms_link, data.content);
            } else {
                console.error('Error:', data.message);
                // Display error message in the popup
                displayError(data.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            displayError("An error occurred while processing the request.");
        });
    });
});

function displayResults(termsLink, content) {
    const resultsDiv = document.createElement('div');
    resultsDiv.innerHTML = `
        <h3>Terms Link:</h3>
        <p><a href="${termsLink}" target="_blank">${termsLink}</a></p>
        <h3>Content:</h3>
        <pre>${content}</pre>
    `;
    document.body.appendChild(resultsDiv);
}

function displayError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.textContent = `Error: ${message}`;
    errorDiv.style.color = 'red';
    document.body.appendChild(errorDiv);
}