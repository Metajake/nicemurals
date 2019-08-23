let world = document.querySelector('.world');

function worldFadeEvent(){
  existingAncestors.each(function(){
    $(this).css('pointer-events', 'auto');
  })
  document.dispatchEvent(homeLinkEvent);
}

document.addEventListener("DOMContentLoaded", function(){
  document.querySelector("#home-link").style.left = parseInt(-window.innerWidth / 6)+'px';
  world.addEventListener('transitionend', worldFadeEvent)
  world.addEventListener('webkitTransitionEnd', worldFadeEvent)
})
