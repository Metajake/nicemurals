$('#home-link').click(function(e){
  e.preventDefault();
  destination = $(this).attr('href')

  $(this).addClass("move")

  setTimeout(function(){
    window.location.href = destination;
  }, 1000);
})

$(document).ready(function(){
  $('.world').height( $(document).height() )
})
