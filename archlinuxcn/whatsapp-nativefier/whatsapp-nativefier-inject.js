if (document.body.innerText.replace(/\n/g, ' ').search(/whatsapp works with.*to use whatsapp.*update/i) !== -1)
  navigator.serviceWorker.getRegistration().then(function (r) { r.unregister(); document.location.reload() });
