// Add Animations to Masthead Nav Anchors
animateElement("#home-link", "move")
animateElement("#about-link", "swipe")
animateElement("#login-link", "unlock")

$('.fa-skull').click(function(e){
  e.preventDefault();

  $(this).addClass("spook")
  this.addEventListener("animationend", function(){
    $(this).removeClass('spook');
    if(this.parentElement.hasAttribute('href')){
      window.location.href = this.parentElement.getAttribute('href');
    }
  });
})

function animateElement(toAnimate, animationName){
  $(toAnimate).click(function(e){
    e.preventDefault();

    $(this).addClass(animationName)
    this.addEventListener("animationend", function(){
      window.location.href = $(this).attr('href');
    });
  })
}

// Listen for Dispatched Events
var blogNavHomeLinkArrive = new Event('blogNavHomeLinkArrive')

document.addEventListener('blogNavHomeLinkArrive', function (e){
  document.querySelector('#home-link').classList.add('arrive');
})

//Add Syntax Highlighting class to Project or Blog Entry <Pre>'s
var codeBlocks = document.querySelectorAll('pre')

function setSyntaxHighlightingAttributes(toSet){
  var codeContent = toSet.children[0].innerHTML
  toSet.classList.add('microlight')
}

// On DOM Content Load
document.addEventListener('DOMContentLoaded', function(){
  document.querySelector("#home-link").style.left = parseInt(-window.innerWidth / 6)+'px';
  if (!document.querySelector("#space")){
    document.dispatchEvent(blogNavHomeLinkArrive);
  }
  codeBlocks.forEach(function(item){
    setSyntaxHighlightingAttributes(item)
  })
})
