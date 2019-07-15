var lastValue, enableExpHandler

game = {
  'life': 0,
  'lvl' : 0,
}

function takeTurnIfReady(functionToExecute){
  if (enableExpHandler) { functionToExecute() }
}

function mouseMoveInteraction(){
  if (enableExpHandler) {
    game['life'] += 1
    enableExpHandler = false;
  }
}

function toggleGameElementFades(){
  existingAncestors = $('.can-exist > section, .can-exist > header')
  existingParents = $('.can-exist > section > *, .can-exist > header > *')
  toggleParentThreshold = 2
  switch (true){
    case game['life'] > toggleParentThreshold:
      existingParents.each(function(i,e){ $(e).addClass('fade-in') })
      break;
    case game['life'] > 0 && game['life'] <= toggleParentThreshold:
      existingAncestors.each(function(i,e){ $(e).addClass('fade-in') })
      existingParents.each(function(i,e){ $(e).removeClass('fade-in') })
      $('.world').addClass('fade-out')
      break;
    case game['life'] <= 0:
      existingAncestors.each(function(i,e){ $(e).removeClass('fade-in') })
      $('.world').removeClass('fade-out')
      break;
    default:
      break;
  }
}

function updateGameStatus(){
  game['life'] > 0 ? game['life'] -= 1 : ''
  $('#game-life').html(game['life'])
}

roundTimer = window.setInterval(function(){
  updateGameStatus()
}, 1500);

movementTimer = window.setInterval(function(){
  enableExpHandler = true;
}, 500);

statusTimer = window.setInterval(function(){
  toggleGameElementFades()
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
