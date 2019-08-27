var body = document.body,
    html = document.documentElement,
    docHeight = Math.max(
      body.scrollHeight,
      body.offsetHeight,
      html.clientHeight,
      html.scrollHeight,
      html.offsetHeight
    );

function centerItemsCallback(){
  document.querySelector('.has-glow').classList.add('glow')
}

function centerVAlignItems(clientValignCenteredItems){
  var itemsProcessed = 0;
  clientValignCenteredItems.forEach(function(item, index, array){
    item.style.marginTop = window.innerHeight/2 - item.clientHeight/2 + "px"
    itemsProcessed ++;
    if(itemsProcessed === array.length){
      centerItemsCallback()
    }
  })
}

// "Load" (all content including css, images and javascript has loaded)
$(window).bind("load", function(){
  $('.world').height(docHeight)
  
  document.querySelector(".world").classList.add('fade-in')
  document.querySelector("#space").classList.add('fade-in')

  centerVAlignItems(document.querySelectorAll('.is-client-vcenter'))
})
