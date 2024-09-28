document.getElementById("send-url").addEventListener("click", () => {
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
      const currentTab = tabs[0].url;
  
      fetch('http://127.0.0.1:5000/receive-url', {
        method: 'POST',
        mode: 'no-cors',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: currentTab }),
      })
      .then(response => response.json())
      .then(data => {
        console.log('URL sent:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    });
  });