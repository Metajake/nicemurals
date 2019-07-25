var lastValue, enableExpHandler

game = {
  'power': 0,
  'on': false,
}
existingAncestors = $('.can-exist > section, .can-exist > header')
existingParents = $('.can-exist > section > *, .can-exist > header > *')

function takeTurnIfReady(functionToExecute){
  if (enableExpHandler) { functionToExecute() }
}

function mouseMoveInteraction(){
  initLevelOne()
  initLevelTwo()
  // 
  // if (enableExpHandler) {
  //   game['power'] += 1
  //   enableExpHandler = false;
  // }
}

function initLevelOne(){
  existingAncestors.each(function(i,e){ $(e).addClass('fade-in') })
  // existingParents.each(function(i,e){ $(e).removeClass('fade-in') })
  $('.world').addClass('fade-out')
}

function initLevelTwo(){
  existingParents.each(function(i,e){ $(e).addClass('fade-in') })
  game['on'] = true;
}

function toggleGameElementFades(){
  toggleParentThreshold = 1
  switch (true){
    case game['power'] > toggleParentThreshold:
      initLevelTwo()
      break;
    case game['power'] > 0 && game['power'] <= toggleParentThreshold:
      initLevelOne()
      break;
    case game['power'] <= 0:
      existingAncestors.each(function(i,e){ $(e).removeClass('fade-in') })
      $('.world').removeClass('fade-out')
      break;
    default:
      break;
  }
}

function updateGameStatsUI(){
  if(game['power'] > 0){
    game['power'] -= 1
  }
  $('#game-power').html(game['power'])
}

function initTimers(){
  // roundTimer = window.setInterval(function(){
  //   window.clearInterval(roundTimer)
  //   updateGameStatsUI()
  // }, 1500);

  movementTimer = window.setInterval(function(){
    window.clearInterval(movementTimer)
    enableExpHandler = true;
  }, 500);

  // uiTimer = window.setInterval(function(){
    //   window.clearInterval(uiTimer)
    //   toggleGameElementFades()
    // }, 300)
}


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

document.addEventListener("DOMContentLoaded", function(){
  initTimers()

  $(document).mousemove(function(e){ mouseMoveInteraction() });
  $(document).scroll(function(e){ mouseMoveInteraction() });
  document.addEventListener("touchstart", function(e){ mouseMoveInteraction() })
  $('.game-lvl').html('{{game.lvl}}')
})
