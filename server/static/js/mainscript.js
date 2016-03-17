$(document).ready(function(){
  var value;
  
    
  $("#trigger").click(function(){
    if (($("#navhide").css("display")) == "block") {
       $("#navhide").slideUp(); 
    }
    else{
   
    $("#navhide").slideDown(600);
     $("#navhide").css("display","block");
    }
  });
  
  
  
  $(document).on('click','.toggleSearchFirst',function(){
    if (($("#search").css("display")) == "block") {
      $("#search").slideUp("slow");
      $(".searchIconFirst").removeClass("glyphicon glyphicon-arrow-up");
      $(".searchIconFirst").addClass("glyphicon glyphicon-search");
        
    }else{
      $(".searchIconFirst").removeClass("glyphicon glyphicon-search");
      $("#search").css("display","block");
      $("#search").hide();
      $("#search").slideDown(900);
      $(".searchIconFirst").addClass("glyphicon glyphicon-arrow-up");
      
    }
    
    });
  
  $(document).on('click','#toggleSearchSecond',function(){
    if (($("#search").css("display")) == "block") {
      $("#search").slideUp("slow");
      $("#searchIconSecond").removeClass();
      $("#searchIconSecond").addClass("glyphicon glyphicon-search");
        
    }else{
      $("#searchIconSecond").removeClass();
      $("#search").slideDown(900);
      $("#searchIconSecond").addClass("glyphicon glyphicon-arrow-up");
      
    }
    
    });
  
  $(window).resize(function(){
    if ($(window).width() > 767) {
      $("#navhide").css("display","none");
    }
    
    });
  
  
  
  
});