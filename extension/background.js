chrome.action.onClicked.addListener((tab) => {
    const tabUrl = tab.url;
  
    fetch('http://127.0.0.1:5000/receive-url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: tabUrl }),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  });  