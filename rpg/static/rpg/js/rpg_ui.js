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

function callback(){
  document.querySelector('.has-glow').classList.add('glow')
}

$(window).bind("load", function(){
  $('.world').height(docHeight)

  var itemsProcessed = 0;
  clientValignCenteredItems.forEach(function(item, index, array){
    item.style.marginTop = window.innerHeight/2 - item.clientHeight/2 + "px"
    itemsProcessed ++;
    if(itemsProcessed === array.length){
      callback()
    }
  })
})
