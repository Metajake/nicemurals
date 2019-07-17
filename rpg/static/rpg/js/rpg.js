var lastValue, enableExpHandler

game = {
  'power': 0,
  'on': false,
}

function takeTurnIfReady(functionToExecute){
  if (enableExpHandler) { functionToExecute() }
}

function mouseMoveInteraction(){
  if (enableExpHandler) {
    game['power'] += 1
    enableExpHandler = false;
  }
}

function toggleGameElementFades(){
  existingAncestors = $('.can-exist > section, .can-exist > header')
  existingParents = $('.can-exist > section > *, .can-exist > header > *')
  toggleParentThreshold = 1
  switch (true){
    case game['power'] > toggleParentThreshold:
      existingParents.each(function(i,e){ $(e).addClass('fade-in') })
      game['on'] = true;
      break;
    case game['power'] > 0 && game['power'] <= toggleParentThreshold:
      existingAncestors.each(function(i,e){ $(e).addClass('fade-in') })
      // existingParents.each(function(i,e){ $(e).removeClass('fade-in') })
      $('.world').addClass('fade-out')
      break;
    case game['power'] <= 0:
      // existingAncestors.each(function(i,e){ $(e).removeClass('fade-in') })
      // $('.world').removeClass('fade-out')
      break;
    default:
      break;
  }
}

function updateGameStatus(){
  if(game['power'] > 0){
    game['power'] -= 1
  }
  $('#game-power').html(game['power'])
}

roundTimer = window.setInterval(function(){
  window.clearInterval(roundTimer)
  updateGameStatus()
}, 1500);

movementTimer = window.setInterval(function(){
  window.clearInterval(movementTimer)
  enableExpHandler = true;
}, 500);

uiTimer = window.setInterval(function(){
  window.clearInterval(uiTimer)
  toggleGameElementFades()
}, 300)

document.addEventListener("DOMContentLoaded", function(){
  $(document).mousemove(function(e){ takeTurnIfReady(mouseMoveInteraction) });
  $(document).scroll(function(e){ takeTurnIfReady(mouseMoveInteraction) });
  document.addEventListener("touchstart", function(e){ takeTurnIfReady(mouseMoveInteraction) })

  $('.game-lvl').html('{{game.lvl}}')
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
