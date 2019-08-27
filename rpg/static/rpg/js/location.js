let world = document.querySelector('.world');

function worldFadedEvent(){
  existingAncestors.each(function(){
    $(this).css('pointer-events', 'auto');
  })
  document.dispatchEvent(blogNavHomeLinkArrive);
}

document.addEventListener("DOMContentLoaded", function(){
  document.querySelector("#home-link").style.left = parseInt(-window.innerWidth / 6)+'px';
  world.addEventListener('transitionend', worldFadedEvent)
  world.addEventListener('webkitTransitionEnd', worldFadedEvent)
})
