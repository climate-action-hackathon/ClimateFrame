$(document).ready(function(){
  var value;
  var uploadImageId;
  var uploadFileId;
  var messageCheckingCounter = 0;

// this function if for enabling toggle of message input
  
  $(document).on('click','.text_nav',function(){
    value = $(this).data('value');
    
    if ($("#drop" + value).css("display") == "block") {
       $("#drop" + value).slideUp(600);
    }else{
     $("#drop" + value).slideDown(900);
    }  
    
    });
  
 // sending message
  
  $(document).on('click','.send',function(){
    var messageValue = $(this).closest(":has(textarea)").find('textarea').val();
    if(value!=null){
      
    $.ajax({
      type:'POST',
      url:'/user/sendMessage/',
      data:{
        message : messageValue,
        receiver_id: value
        
      },
      dataType:'text',
      
      success:function(data){
        $("#notification" + value).text(data);
        $("#notification" + value).slideDown(1500);
        $("#notification" + value).fadeOut(2000);
      }
      });
    }else{
      
    }
    });
  //user should see messages, when mouse is on inbox link
  
  $("#inbox_link").hover(function(){
       $("#message_note").css("text-shadow","none");
       $(".inbox-messages").css("display","block");
    },
    function(){
     $("#message_note").css("text-shadow","1px 2px black");
    });
  $(".inbox-messages").hover(function(){
    $(".inbox-messages").css("display","block");
    },function(){
      $(".inbox-messages").css("display","none");
      });
  
  
  //checking for inbox
  function check() {
    $.ajax({
      type:'POST',
      url:'/user/checkNewMessage/',
      datatype:'text',
      success:function(data){
        
        var messages = parseInt(data);
        if (messages > 0 ) {
          messageCheckingCounter++;
          if (($(".mnote1").css("display") == "none") || ($(".mnote2").css("display") == "none")){
              $(".mnote1").text(messages);
              $(".mnote1").css("display","inline");
              $(".mnote2").text(messages);
              $(".mnote2").css("display","inline");
          }else if (($(".mnote1").css("display") == "inline") || ($(".mnote2").css("display") == "inline")) {
              $(".mnote1").text(messages);
              $(".mnote1").css("display","inline");
              $(".mnote2").text(messages);
              $(".mnote2").css("display","inline");
          }
          else if (($(".mnoteWithData1").css("display") == "none") || ($(".mnoteWithData2").css("display") == "none")) {
               $(".mnoteWithData1").text(messages);
              $(".mnoteWithData1").css("display","inline");
              $(".mnoteWithData2").text(messages);
              $(".mnoteWithData2").css("display","inline");
          }
          if (messageCheckingCounter > 0) {
           if ($(window).width() <= 767) {
           $("#navhide").slideDown(600);
            $("#navhide").css("display","block");
           }
           
           messageCheckingCounter = 0;
          }
        }
      }
     
    });
     messageCheckingCounter = 0;
  }
  
    setInterval(check,2000);
    
    
    
    //for user search
    $("#searchIn").keyup(function(){
      var searchText = $("#searchIn").val();
      var dataPage = $("#dataPage").data('value');
      if (searchText != "") {
      
      $.ajax({
        type:'POST',
        url:'/user/search/',
        data:{
          searchValue:searchText,
          dataPage : dataPage
        },
        dataType:'html',
        success:function(data){
         $("#sResult").css("display","block");
         
         $("#resultUl").html(data);
        }
        
        });
      }
      return false;
      
    });
    
    //when removing search results
   $(document).live("click",function(event){
        var clicked = $(event.target);
          if (!clicked.hasClass("searchIn")) {
             $("#sResult").fadeOut();
          }
          if (!clicked.hasClass("postText")) {
            if (!clicked.hasClass("postB")) {
                if ($(".postText").val()=="") {
                  $(".postText").val("Write your post here...");
                } 
            }
          }else{
            if ($(".postText").val()=="Write your post here..."){
              $(".postText").val("");
            }
          }
    });
   $(".searchIn").click(function(){
        $("#sResult").fadeIn();
    });
   
   
   //for customizing background in post
   
   $("#postButton").click(function(){
       if ($(".postText").val()!="" && $(".postText").val()!="Write your post here...") {
            $(".alert").hide();
           $(".load").css("display","inline");
           var postContent = $(".postText").val();
           $.ajax({
        type:'POST',
        url:'/user/post/',
        data:{
          content:postContent,
          uploadImageId:uploadImageId
        },
        dataType:'text',
        success:function(response){
          if (response=="success") {
             
             $(".load").hide();
             $(".alert").removeClass("failed"); 
             $(".alert").addClass("success");
              $(".alert").css("display","inline");
             $(".alert").text("Posted successfully");
             $(".alert").delay(3000).fadeOut(1000);
          }else{
            $(".load").hide();
            $(".alert").removeClass("success");
            $(".alert").addClass("failed");
            
              $(".alert").css("display","inline");
             $(".alert").text("problem in posting, please try again");
             //$(".alert").delay(3500).fadeOut(500);
          }
         
         
        }
        
        });
           
       }
       else{
        $(".alert").removeClass("success");
         $(".alert").addClass("failed");
         
         $(".alert").css("display","inline");
        $(".alert").text("Write something before posting");
       }
    });
   
   
   /* when user click inside post textarea
    */
   $(".postText").click(function(){
    $(".alert").hide();
    });
   
   /* show div for password change */
   $("#triggerPass").click(function(){
    if ($(".passwordDiv").css("display") == "none") {
     $(".passwordDiv").show();
      $(".passwordDiv").slideDown();
    }else{
      $(".passwordDiv").slideDown();
      $(".passwordDiv").hide();
    }
    });
   
   /* checking posts*/
   function checkPost() {
    $.ajax({
      type:'POST',
      url:'/user/checkNewPost/',
      datatype:'html',
      success:function(data){
        if (data != '' && data.indexOf("Unable") == -1) {
          
          $('.posts').prepend(data);
          
        }
       
      }
    });
  }
  /*deleting message*/
  $(".remove").tooltip({
                       animation:false
                       });
  
  $(document).on('click','.remove',function(){
    var messageId = $(this).data('value');
    var loaderId = "#loadms"+messageId;
    $(loaderId).css("display","inline");
    
    $.ajax({
      type:'POST',
      url:'/user/deleteMessage/'+messageId,
      datatype:'text',
      success:function(data){
        if (data == "success") {
          var idValue = "#ms"+messageId;
          
            $(loaderId).fadeOut(2500,function(){
              $(idValue).remove();
              });
        }else{
          $(loaderId).hide();
          var info = "inf"+messageId;
          $(info).css("display","inline");
          $(info).fadeOut(3000);
          
          
        }
        
      }
      });
    });
   
   /* deleting post */
   $(".removepost").tooltip({
                       animation:false
                       });
   $(document).on('click','.removepost',function(){
         var postId = $(this).data('value');
         var loaderId = "#loadps"+postId;
         $(loaderId).css("display","inline");
         
    $.ajax({
      type:'POST',
      url:'/user/deletePost/'+postId,
      datatype:'text',
      success:function(data){
        if (data == "success") {
          var idValue = "#ps"+postId;
          
            $(loaderId).fadeOut(2500,function(){
              $(idValue).remove();
             
              });
        }else{
          $(loaderId).hide();
          var info = "inf"+postId;
          $(info).css("display","inline");
          $(info).fadeOut(3000);
          
          
        }
        
      }
      });
         
         
    });
   
   
   setTimeout(function(){
            $('.new_ms').css("background-color","white");
            $(".new_not").remove();
      },15000);
  
    setInterval(checkPost,2000);



$(':file').change(function(){
    var file = this.files[0];
    var name = file.name;
    var size = file.size;
    var type = file.type;
    //Your validation
});


$(document).on("change",'#infileImage',function(){
  if ($("#imageProgress").css("display") == "inline") {
      $('#imageProgress').attr({value:0});
  }else{
      $("#imageProgress").css("display","inline");
  }
  $("#imageProgressNote").text("Uploading");
  
    var formData = new FormData();
    formData.append('file',$('#infileImage').prop("files")[0]);
    $.ajax({
        url: '/user/uploadPostImage',  //Server script to process data
        type: 'POST',
        xhr: function() {  // Custom XMLHttpRequest
            var myXhr = $.ajaxSettings.xhr();
            if(myXhr.upload){ // Check if upload property exists
                myXhr.upload.addEventListener('progress',progressHandlingFunctionImage, false); // For handling the progress of the upload
            }
            return myXhr;
        },
        //Ajax events
        //beforeSend: beforeSendHandler,
        success: function(data){
          if (data.indexOf("success") != -1) {
             uploadImageId = data.substring((data.lastIndexOf('s') + 1),data.length);
             
          $("#noty").text(data);
          $("#imageProgressNote").text("Upload Complete");
           }else{
            $("#imageProgressNote").text("Problem in uploading image");
           }
          },
        error: function(data){
          $("#noty").text(data);
          $("#imageProgressNote").text("Failed, Please check the network connection");
          },
        // Form data
        data: formData,
        //Options to tell jQuery not to process data or worry about content-type.
        cache: false,
        contentType: false,
        processData: false
    });
});

function progressHandlingFunctionImage(e){
    if(e.lengthComputable){
        $('#imageProgress').attr({value:e.loaded,max:e.total});
    }
}

//file uploading
$(document).on("change",'#infileFile',function(){
  $("#fileProgress").css("display","inline");
  $("#fileProgressNote").text("Uploading");
  
    var formData = new FormData();
    formData.append('fileAttached',$('#infileFile').prop("files")[0]);
    $.ajax({
        url: '/user/uploadPostFile',  //Server script to process data
        type: 'POST',
        xhr: function() {  // Custom XMLHttpRequest
            var myXhr = $.ajaxSettings.xhr();
            if(myXhr.upload){ // Check if upload property exists
                myXhr.upload.addEventListener('progress',progressHandlingFunctionFile, false); // For handling the progress of the upload
            }
            return myXhr;
        },
        //Ajax events
        //beforeSend: beforeSendHandler,
        success: function(data){
          if (data.indexOf("success") != -1) {
             uploadFileId = data.substring((data.lastIndexOf('s') + 1),data.length);
             
          $("#noty").text(data);
          $("#fileProgressNote").text("Upload Complete");
           }else{
            
           }
          },
        error: function(data){
          $("#noty").text(data);
          $("#fileProgressNote").text("Failed, Please check the network connection");
          },
        // Form data
        data: formData,
        //Options to tell jQuery not to process data or worry about content-type.
        cache: false,
        contentType: false,
        processData: false
    });
});

function progressHandlingFunctionFile(e){
    if(e.lengthComputable){
        $('#fileProgress').attr({value:e.loaded,max:e.total});
    }
}






//user commenting functions
$(document).on('click','.comment',function(){
    var commentValue = $(this).closest(":has(textarea)").find('textarea').val();
    if(value!=null){
      
    $.ajax({
      type:'POST',
      url:'/user/postComment/',
      data:{
        comment : commentValue,
        post_id: value
        
      },
      dataType:'text',
      
      success:function(data){
        $("#notification" + value).text(data);
        $("#notification" + value).slideDown(1500);
         $("#notification" + value).slideUp(1200).delay(1000);
      }
      });
    }else{
      
    }
    });

    
    
    /* checking comments*/
   function checkComment() {
    $.ajax({
      type:'POST',
      url:'/user/checkNewComments/',
      datatype:'html',
      success:function(data){
        if (data != '') {
          $(".hide").append(data);
          var list = $(".hide").find($("li"));
          for(var i =0; i < list.length; i++ ){
            if ($("#comm"+$(list[i]).attr("data-value")).length) {
                $("#comm"+$(list[i]).attr("data-value")).prepend(list[i]);
            }else{
              $("#dropdown"+$(list[i]).attr("data-value"))
              .before('<div class="row">'+
		       '<div class="comments"  >'+
		       '<ul  class="nav comment-ul" id="comm'+$(list[i]).attr("data-value")+'" >'+
                       
                       '</ul>'+
                       '</div>'+
                       '</div>'
                       );
              $("#comm"+$(list[i]).attr("data-value")).prepend(list[i]);
              
              
            }
           
          }
          
        }
       
      }
    });
  }
  //handling scrolling behaviour
  if ((".message_content").children < 3) {
    (".message_content").css("overflow-y","none");
  }
  
  //loading more post
  $(document).on('click','.post_load',function(){
    $.ajax({
      type:'POST',
      url:'/user/morePosts/',
      datatype:'html',
      success:function(data){
        if (data != '') {
          $('.posts').text(" ");
          $('.posts').prepend(data);
          
        }
       
      }
    });
    });
  
  //checking for scrolling options in messages
  if ($('.message_lists').children().length < 3) {
      $('.message_lists').css("height","none");
      $('.message_lists').css("overflow-y","none");  
  }
  
  setInterval(checkComment,3000);

});




