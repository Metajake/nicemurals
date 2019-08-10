var body = document.body,
    html = document.documentElement,
    docHeight = Math.max(
      body.scrollHeight,
      body.offsetHeight,
      html.clientHeight,
      html.scrollHeight,
      html.offsetHeight
    );

var clientValignCenteredItems = document.querySelectorAll('.is-client-vcenter')

$(window).bind("load", function(){
  $('.world').height(docHeight)
  clientValignCenteredItems.forEach(function(item){
    item.style.marginTop = window.innerHeight/2 - item.clientHeight/2 + "px"
  })
})
