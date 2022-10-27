$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, textStatus) {
  const x = JSON.parse(data);
  $('#character').html(x);
});
