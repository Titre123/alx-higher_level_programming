$.get('https://www.fourtonfish.com/hellosalut/hello', function (data, textStatus) {
  const x = JSON.parse(data);
  $('INPUT#language_code').html(x.code);
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').html(x.hello);
  });
});
