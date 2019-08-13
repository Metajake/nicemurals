let world = document.querySelector('.world');

function worldFadeEvent(){
  existingAncestors.each(function(){
    $(this).css('pointer-events', 'auto');
  })
}

document.addEventListener("DOMContentLoaded", function(){
  document.quertSelector('.can-exist > section, .can-exist > header, .can-exist > footer').foreach(function(item){
    console.log(item)
  })
  world.addEventListener('transitionend', worldFadeEvent)
  world.addEventListener('webkitTransitionEnd', worldFadeEvent)
})
