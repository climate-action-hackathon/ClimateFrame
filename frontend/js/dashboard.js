$(document).ready(function(){

  handleFab();

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

  $(".generate-button").on("click", function(){
    $(".loader").css('visibility', 'visible');
    setTimeout(
      function() {
        $(".loader").css('visibility', 'hidden');
        $("#message").css('visibility', 'visible');
      }, 3000);
  });
  
});

function handleFab(){

  var fab = $(".fab");
  var content = $(".cntt-wrapper");
  var submit = $("#submit");
  var cancel = $("#cancel");
  var protect = $(".protect");
  var fabIcon = $("svg");

  $("#submit").on('click', function() {
    $(".fab").removeClass('active');
    $("svg").css('display', 'block');
    $(".cntt-wrapper").css('display', 'none');
    $(".protect").css('background', 'none');
  });

  //fab click
  fab.on('click', function(event) {
   event.preventDefault();
   protect.css("background", "hsla(0, 100%, 0%, 0.3)");
   fabIcon.css("display", "none");
   fab.addClass('active');
   content.css('display', 'block');
 });

  //Hide if click outside the fab
  $(document).mouseup(function(e) {
    if (!fab.is(e.target) && fab.has(e.target).length === 0) {
      fab.removeClass('active');
      fabIcon.css('display', 'block');
      content.css('display', 'none');
      protect.css('background', 'none');
    }
  });
}

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

  renderDataTemplates();
}

function renderDataTemplates(){

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
  var id = getSelectedListId(listCell);
  $("#sms").css('visibility', 'hidden');
  $("#message").css('visibility', 'hidden');
  switch(id){

    case 1:
    $(".option_h").text("Temperature");
    $(".unit").text("°C");
    break;

    case 2:
    $(".option_h").text("Wind speed");
    $(".unit").text("km/h");
    break;

    case 3:
    $(".option_h").text("Thunder risk");
    $(".unit").text("%");
    break;

    case 4:
    $(".option_h").text("Rain Probability");
    $(".unit").text("%");
    $("#sms").css('visibility', 'visible');
    break;
  }
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
