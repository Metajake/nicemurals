var lastValue, enableExpHandler, gameLife = 0

function takeTurnIfReady(functionToExecute){
  if (enableExpHandler) { functionToExecute() }
}

function checkGameStatus(){
  existingAncestors = $('.can-exist > section, .can-exist > header')
  existingParents = $('.can-exist > section > *, .can-exist > header > *')
  toggleParentThreshold = 4
  switch (true){
    case gameLife > toggleParentThreshold:
      existingParents.each(function(i,e){ $(e).addClass('fade-in') })
      break;
    case gameLife > 0 && gameLife <= toggleParentThreshold:
      existingAncestors.each(function(i,e){ $(e).addClass('fade-in') })
      existingParents.each(function(i,e){ $(e).removeClass('fade-in') })
      $('.world').addClass('fade-out')
      break;
    case gameLife <= 0:
      existingAncestors.each(function(i,e){ $(e).removeClass('fade-in') })
      $('.world').removeClass('fade-out')
      break;
    default:
      break;
  }
}

roundTimer = window.setInterval(function(){
  gameLife > 0 ? gameLife -= 1 : ''
  $('#game-life').html(gameLife)
}, 1500);

movementTimer = window.setInterval(function(){
  enableExpHandler = true;
}, 500);

statusTimer = window.setInterval(function(){
  checkGameStatus()
}, 300)

document.addEventListener("DOMContentLoaded", function(){
  $(document).mousemove(function(e){ takeTurnIfReady(mouseMoveInteraction) });
  $(document).scroll(function(e){ takeTurnIfReady(mouseMoveInteraction) });
  document.addEventListener("touchstart", function(e){ takeTurnIfReady(mouseMoveInteraction) })
})

function gainExp(url, entityId, difference, csrfToken){
  $.ajax({
    type: "POST",
    url: url,
    data: {
      entityId :entityId,
      experienceAmount: difference,
      csrfmiddlewaretoken: csrfToken,
    },
    success: function(data){
      firstEntity = JSON.parse(data)[0]
      $( '#entity-' + firstEntity['pk'].toString() ).html()
      $( '#entity-' + firstEntity['pk'].toString() + ' .exp').html(firstEntity['fields']['experience'])
    }
  })
}
