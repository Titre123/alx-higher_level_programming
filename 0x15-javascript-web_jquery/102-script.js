$('INPUT#btn_translate').click( () => {
   const value = $('INPUT#language_code').val();
   const url = 'https://stefanbohacek.com/hellosalut/?lang=' + value;
   $.get(url, function(data) {
     $('DIV#hello').html(data.hello);
   });
 })
