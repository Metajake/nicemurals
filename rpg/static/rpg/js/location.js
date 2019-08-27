let world = document.querySelector('.world');

function eventWorldFade(){
  existingAncestors.each(function(){
    $(this).css('pointer-events', 'auto');
  })
  document.dispatchEvent(blogNavHomeLinkArrive);
}

document.addEventListener("DOMContentLoaded", function(){
  document.querySelector("#home-link").style.left = parseInt(-window.innerWidth / 6)+'px';
  world.addEventListener('transitionend', eventWorldFade)
  world.addEventListener('webkitTransitionEnd', eventWorldFade)
})
