let world = document.querySelector('.world');

function worldFadeEvent(){
  existingAncestors.each(function(){
    $(this).css('pointer-events', 'auto');
  })
}

document.addEventListener("DOMContentLoaded", function(){
  world.addEventListener('transitionend', worldFadeEvent)
  world.addEventListener('webkitTransitionEnd', worldFadeEvent)
})
