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

function setImageMarginLeft(imgContainer){
  image = $(imgContainer).find('img')
  containerWidth = Math.abs( $(imgContainer).width() )
  imageWidth = Math.abs( image.width() )
  difference = Math.round( imageWidth - containerWidth )
  marginLeft = Math.round( difference / 2 )
  image.css('margin-left', -marginLeft+'px')
}

document.addEventListener("DOMContentLoaded", function(){
  $('.landscape').each(function(index, imgContainer){
    setImageMarginLeft(imgContainer)
  })
})
