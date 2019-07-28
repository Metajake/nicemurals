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
// and Margin-Left to horizontal orientation images
$('.entry').each(function(index, entry){
  orientation = getImageRatioClass(entry)
  $(entry).find('.figure.image').addClass( orientation )
  if(orientation == 'is-horiz'){
    setImageMarginLeft(entry)
  }
})

function getImageRatioClass(imgContainer){
  imgWidth = $(imgContainer).find('img').width()
  imgHeight = $(imgContainer).find('img').height()
  imageRatio = Math.round( imgWidth ) / Math.round( imgHeight )
  if(imageRatio > 1){orientation = 'is-horiz'}else{orientation = 'is-vert'}
  return orientation
}

function setImageMarginLeft(entryContainer){
  imgContainer = $(entryContainer).find('.figure.image')
  image = imgContainer.find('img')
  containerWidth = Math.abs( imgContainer.width() )
  imageWidth = Math.abs( image.width() )
  difference = Math.round( imageWidth - containerWidth )
  marginLeft = Math.round( difference / 2 )
  image.css('margin-left', -marginLeft+'px')
}
