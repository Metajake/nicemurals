var body = document.body,
    html = document.documentElement,
    docHeight = Math.max(
      body.scrollHeight,
      body.offsetHeight,
      html.clientHeight,
      html.scrollHeight,
      html.offsetHeight
    ),
    existingAncestors = $('.has-location > section, .has-location > header, .has-location > footer'),
    existingParents = $('.has-location > section > *, .has-location > header > *, .has-location > footer > *'),
    elementsToFadeOut = document.querySelectorAll('.has-fade-out');

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

function mouseMoveInteraction(){
  existingAncestors.each(function(i,e){ $(e).addClass('fade-in') })

  elementsToFadeOut.forEach(function(item){
    item.classList.remove('fade-in')
    item.classList.add('fade-out')
  })
  
  existingAncestors.each(function(){
    $(this).find('a').css('pointer-events', 'auto');
  })
}

document.addEventListener("DOMContentLoaded", function(){
  $(document).mousemove(function(e){ mouseMoveInteraction() });
  $(document).scroll(function(e){ mouseMoveInteraction() });
  document.addEventListener("touchstart", function(e){ mouseMoveInteraction() })
})


// "Load" (all content including css, images and javascript has loaded)
$(window).bind("load", function(){
  $('.world').height(docHeight)

  $(".world").addClass('fade-in')
  $("#space").addClass('fade-in')

  centerVAlignItems(document.querySelectorAll('.is-client-vcenter'))
})
