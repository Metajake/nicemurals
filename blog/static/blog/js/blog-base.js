// Add Animations to Masthead Nav Anchors
animateElement("#home-link", "move")
animateElement("#about-link", "swipe")
animateElement("#login-link", "unlock")

function animateElement(toAnimate, animationName){
  $(toAnimate).click(function(e){
    e.preventDefault();

    $(this).addClass(animationName)
    this.addEventListener("animationend", function(){
      window.location.href = $(this).attr('href');
    });
  })
}

// Add Animation to Masthead Logout Anchor
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

// Listen for Dispatched Events
var homeLinkEvent = new Event('homeLinkArrive')

document.addEventListener('homeLinkArrive', function (e){
  console.log(e)
  document.querySelector('#home-link').classList.add('arrive');
})

//Add Syntax Highlighting class to Project or Blog Entry <Pre>'s
var codeBlocks = document.querySelectorAll('pre')

function setSyntaxHighlightingAttributes(toSet){
  var codeContent = toSet.children[0].innerHTML
  var syntaxType = getSyntaxType(codeContent);
  toSet.classList.add('ft-syntax-highlight')
  toSet.setAttribute('data-syntax', syntaxType)
  toSet.setAttribute('data-syntax-theme', 'one-dark')
}

function getSyntaxType(toIndex){
  var firstWhiteSpaceIndex = toIndex.indexOf('\n');
  var firstWord = toIndex.substring(0, firstWhiteSpaceIndex);
  var toReturn;
  switch(firstWord){
    case '//javascript':
      toReturn = 'js'
      break;
    case '//python':
      toReturn = 'js'
      break;
  }
  return toReturn
}

// On DOM Content Load
document.addEventListener('DOMContentLoaded', function(){
  codeBlocks.forEach(function(item){
    setSyntaxHighlightingAttributes(item)
  })
})
