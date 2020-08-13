// ==UserScript==
// @include https://web.whatsapp.com/
// ==/UserScript==

// Quirk for WhatsApp Web, based on:
// https://github.com/jiahaog/nativefier/issues/719

"use strict";

var id = setInterval(bypass, 50);
function bypass() {
  console.log("Checking for 'Update browser' message...");
  if (document.querySelector("a[href='https://support.google.com/chrome/answer/95414']")) {
    console.log("Bypassing 'Update browser' message...");
    navigator.serviceWorker.getRegistration().then((registration) => {
      registration.unregister();
      document.location.reload();
      console.log("'Update browser' message bypassed.");
      clearInterval(id);
    });
  }
}
window.setTimeout(
  function() {
    console.log("No 'Update browser' message found after 5 seconds.");
    clearInterval(id); 
  }, 5000
);
