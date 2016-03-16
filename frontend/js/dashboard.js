$(document).ready(function(){
  initLists();

  $("[id^=list-cell]").on("click", function(){
    handleListClick($(this));
  });

  $("[id^=option-cell]").on("click", function(){
    handleOptionClick($(this));
  });

  $("[id^=action-cell]").on("click", function(){
    handleActionClick($(this));
  });
});

function initLists(){
  $("[id^=list-cell]").each(function(){
    $(this).css("background-color", "#fafafa")
  });

  $("[id^=option-cell]").each(function(){
    $(this).css("background-color", "#283593")
  });

  $("[id^=action-cell]").each(function(){
    $(this).css("background-color", "#283593")
  });
}

function handleClick(listCell, id, clickColor, hoverColor){
  var color = hexc(listCell.css("background-color"));
  var allListCells = $(id);
  if (allListCells.length > 1){
    allListCells.each(function(){ 
      if ($(this) != listCell){
        $(this).css("background-color", clickColor);
      }
    });
  }
  if (color == clickColor){
    listCell.css("background-color", hoverColor);
  } else {
    listCell.css("background-color", clickColor);
  }
}

function handleListClick(listCell){
  handleClick(listCell, "[id^=list-cell]", "#fafafa", "white");
}

function handleOptionClick(listCell){
 handleClick(listCell, "[id^=option-cell]", "#283593", "#5C6BC0"); 
}

function handleActionClick(listCell){
 handleClick(listCell, "[id^=action-cell]", "#283593", "#5C6BC0"); 
}

function getSelectedListId(listCell){
  var id = listCell.attr('id');
  id = parseInt((id.slice(-1)), 10);
  return id != NaN ? id : -1;
}

function hexc(colorval){
  var parts = colorval.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
  delete(parts[0]);
  for (var i = 1; i <= 3; ++i){
    parts[i] = parseInt(parts[i]).toString(16);
    if (parts[i].length == 1) parts[i] = '0' + parts[i];
  }
  return '#' + parts.join('');
}
