// No analytics vendor is loaded here. Connect a provider to consume these events.
document.addEventListener('click', (event) => {
  const link = event.target.closest('a[data-procedure], a[data-contact]');
  if (!link) return;
  const incoming = new URLSearchParams(location.search);
  const payload = {
    event: 'whatsapp_click',
    procedure: link.dataset.procedure || null,
    placement: link.dataset.contact || 'procedimentos',
    utm_source: incoming.get('utm_source') || 'instagram',
    utm_medium: incoming.get('utm_medium') || 'bio',
    utm_campaign: incoming.get('utm_campaign') || 'dentista_vs10',
    utm_content: link.dataset.procedure || link.dataset.contact,
  };
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push(payload);
  window.dispatchEvent(new CustomEvent('vs10:whatsapp-click', { detail: payload }));
});
