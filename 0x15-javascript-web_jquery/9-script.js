$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
  const x = JSON.parse(data);
  $('#hello').html(x.hello);
});
