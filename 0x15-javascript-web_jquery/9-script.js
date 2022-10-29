$(document).ready(() => {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data, textStatus) {
    $('#hello').html(data.hello);
  });
})
