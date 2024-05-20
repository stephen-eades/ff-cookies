chrome.runtime.onInstalled.addListener(() => {
  chrome.webRequest.onBeforeRequest.addListener(
    () => ({ cancel: true }),
    { urls: ["*://www.espn.com/*"], types: ["main_frame", "sub_frame"] },
    ["blocking"]
  );
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "fetchCookies") {
    chrome.cookies.get({ url: 'https://www.espn.com', name: 'SWID' }, (swidCookie) => {
      chrome.cookies.get({ url: 'https://www.espn.com', name: 'espn_s2' }, (espnS2Cookie) => {
        sendResponse({
          swid: swidCookie ? swidCookie.value : 'Not found',
          espn_s2: espnS2Cookie ? espnS2Cookie.value : 'Not found'
        });
      });
    });
    return true; // Indicates we want to send a response asynchronously
  }
});
