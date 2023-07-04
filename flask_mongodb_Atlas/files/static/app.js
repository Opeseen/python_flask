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
        console.log(ids)
        $.ajax({
            type: "POST",
            contentType: 'application/json;charset=UTF-8',
            url: "/delete",
            data: JSON.stringify({'ids': ids}),
            dataType: "json",
            cache: false,
            success: function(msg) {
                $("#msg").html(msg)
                setTimeout(() =>{
                    window.location.href = '/'
                },1500)
            },
            error: function(jqXHR, textStatus, errorThrown) {
                $("#msg").html("<span class='flash red'>" + textStatus + " " + errorThrown + "</span>");
            }
        });
        
      }else{
        $("#msg").html('<span class="flash red">You must select at least one product for deletion</span>');
      }
    
    })
  })
  
  // $("#msg").html('<span class="flash green">Items successfully picked for deletion</span>');