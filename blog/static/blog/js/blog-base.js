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

// Homepage Entry List: Apply "featured image" ratio class to container
$('.entry').each(function(index, entry){
  $(entry).find('.figure.image').addClass( getImageRatioClass(entry) )
})

function getImageRatioClass(imgContainer){
  imageRatio = Math.round( $(imgContainer).find('img').width() ) / Math.round( $(imgContainer).find('img').height() )
  if(imageRatio > 1){orientation = 'is-horiz'}else{orientation = 'is-vert'}
  return orientation
}
