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
// and Margin-Left to horizontal images
$('.entry').each(function(index, entry){
  $(entry).find('.figure.image').addClass( getImageRatioClass(entry) )
  setMarginLeftToHorizontalImages(entry)
})

function getImageRatioClass(imgContainer){
  imageRatio = Math.round( $(imgContainer).find('img').width() ) / Math.round( $(imgContainer).find('img').height() )
  if(imageRatio > 1){orientation = 'is-horiz'}else{orientation = 'is-vert'}
  return orientation
}

function setMarginLeftToHorizontalImages(imgContainer){
  containerWidth = $(imgContainer).find('.figure.image').width()
  imageWidth = $(imgContainer).find('.figure.image img').width()
  difference = Math.round( Math.abs(containerWidth - imageWidth) )
  marginLeft = Math.round( difference / 2 )
  $(imgContainer).find('.figure.image img').css('margin-left', -marginLeft+'px')
}
