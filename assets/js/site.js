/* Mobile menu toggle. Without JavaScript the menu is simply always shown. Stores nothing. */
(function () {
  var button = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (!button || !nav) return;
  function setOpen(open) {
    button.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
  }
  button.addEventListener('click', function () {
    setOpen(button.getAttribute('aria-expanded') !== 'true');
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      setOpen(false);
      button.focus();
    }
  });
})();
