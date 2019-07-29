// Add Animation to Masthead Homepage Anchor
$('#home-link').click(function(e){
  e.preventDefault();

  homepageDelay = 1000
  destination = $(this).attr('href')

  $(this).addClass("move")

  setTimeout(function(){
    window.location.href = destination;
  }, homepageDelay);
})

// Add Animation to Masthead Logout Anchor
$('.fa-skull').click(function(e){
  $(this).addClass("spook")
  this.addEventListener("animationend", function(){$(this).removeClass('spook')})
})
