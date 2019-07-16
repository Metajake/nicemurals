var body = document.body,
    html = document.documentElement;

var height = Math.max( body.scrollHeight, body.offsetHeight,
                       html.clientHeight, html.scrollHeight, html.offsetHeight );


document.addEventListener("DOMContentLoaded", function(){
  $('.world').height(height)
})
