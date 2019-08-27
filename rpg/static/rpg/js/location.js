
function eventWorldFade(){
  document.dispatchEvent(blogNavHomeLinkArrive);
}

document.addEventListener("DOMContentLoaded", function(){
  document.querySelector("#home-link").style.left = parseInt(-window.innerWidth / 6)+'px';

  document.querySelector('header').addEventListener('transitionend', eventWorldFade)
  document.querySelector('header').addEventListener('webkitTransitionEnd', eventWorldFade)
})
