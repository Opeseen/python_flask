$(function(){
  $("#check_all").click(function () {
    if ($("input:checkbox").prop("checked")) {
      $("input:checkbox[name='row-check']").prop("checked", true)
    } else {
      $("input:checkbox[name='row-check']").prop("checked", false);
    }
  });
  
  $("input:checkbox[name='row-check']").change(function () {
    const total_boxes = $("input:checkbox[name='row-check']").length;
    const total_checked_boxes = $("input:checkbox[name='row-check']:checked").length;
  
    // If all checked manually then check check_all checkbox
    if (total_boxes === total_checked_boxes) {
      $("#check_all").prop("checked", true);
    }
    else {
      $("#check_all").prop("checked", false);
    }
  });
  
  $("#multiple_delete").click( () => {
    let ids = '';
    let comma = '';
    $("input:checkbox[name='row-check']:checked").each(function() {
      ids = ids + comma + this.value;
      comma = ',';   
    });
    
    if(ids.length > 0){
      // Confirm box
      bootbox.confirm({
        message: "Are you sure you want to delete the selected record.?",
        buttons:{
          confirm:{
            label: 'Yes',
            className: 'btn-success'
          },
          cancel:{
            label: 'No',
            className: 'btn-danger'
          }
        },
        // Write a callback function
        callback: function(result){
          if(result){
            $.ajax({
              type: "POST",
              contentType: 'application/json;charset=UTF-8',
              url: "/deleteSelected",
              data: JSON.stringify({'ids': ids}),
              dataType: "json",
              cache: false,
              success: function(msg){
                $("#msg").html(msg)
                setTimeout(() =>{
                  window.location.href = '/dashboard'
                },1500)
              },
              error: function(jqXHR, textStatus, errorThrown){
                $("#msg").html("<span class='flash red'>" + textStatus + " " + errorThrown + "</span>");
              }
            });
          
          }else{
            bootbox.alert("Selected items cancelled for deletion")
          }
        }

      });    
      
    }else{
      $("#msg").html('<span class="flash red">You must select at least one id for deletion</span>');
    }
  
  })
})