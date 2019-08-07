var body = document.body,
    html = document.documentElement;

var docHeight = Math.max( body.scrollHeight, body.offsetHeight,
                       html.clientHeight, html.scrollHeight, html.offsetHeight );

var worldBrand = document.querySelector('.world .is-size-brand')

$(window).bind("load", function(){
  $('.world').height(docHeight)
  worldBrand.style.marginTop = window.innerHeight/2 - worldBrand.clientHeight/2 + "px"
})
