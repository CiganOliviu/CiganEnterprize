$(function() {
  $('.scroll-down').click (function() {
    $('html, body').animate({scrollTop: $('#content').offset().top }, 'slow');
    return false;
  });
});
