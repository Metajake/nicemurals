$('#home-link').click(function(e){
  e.preventDefault();
  destination = $(this).attr('href')

  $(this).addClass("move")

  setTimeout(function(){
    window.location.href = destination;
  }, 1000);
})

$('.fa-skull').click(function(e){
  console.log("glick")
  $(this).addClass("spook")
  // setTimeout(function(){console.log("Remobing");$(this).removeClass('spook')}, 1500);
  this.addEventListener("animationend", function(){$(this).removeClass('spook')})
})
