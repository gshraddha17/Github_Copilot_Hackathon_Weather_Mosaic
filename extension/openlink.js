(() => {
    window.onload = () => {
      chrome.runtime.connectNative("com.google.chrome.extension.siri");
    }
  })();