$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  const x = JSON.parse(data);
  for (const movie of x) {
    $('UL#list_movies').append(`<li>${movie}</li>`);
  }
});
