// Jquery function to delete items through checkbox selecion option
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
  
  $("#deleteNoteBySelection").click( () => {
    let ids = '';
    let comma = '';
    $("input:checkbox[name='row-check']:checked").each(function() {
      ids = ids + comma + this.value;
      comma = ',';   
    });
    
    if(ids.length > 0){
      // Bootbox confirm box for delete
      bootbox.confirm({
        title: "ARE YOU SURE YOU WANT TO DELETE THE SELECTED NOTE.?",
        message:'<p class="text-danger font-weight-bold text-uppercase">Warning: This will delete permanently and cannot be undone</p>',
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
              url: "/deleteNote",
              data: JSON.stringify({'ids': ids}),
              dataType: "json",
              cache: false,
              success: function(msg){
                $("#msg").html(msg)
                setTimeout(() =>{
                  window.location.href = '/dashboard'
                },1000)
              },
              error: function(jqXHR, textStatus, errorThrown){
                $("#msg").html("<span class='flash red'>" + textStatus + " " + errorThrown + "</span>");
              }
            });
          }
        }

      });    
      
    }else{
      $("#msg").html('<span class="flash red">You must select at least one field for deletion</span>');
    }
  
  })
})


// Jquery function to update note
$(function(){
  $(document).ready(function(){
    $('#modifyNote').submit(function(event){
      event.preventDefault()
      input = {}
      input_values =  $(this).serializeArray()
      input_values.forEach((element) =>{
        input[element.name] = element.value
      })
      $.ajax({
        type: "POST",
        contentType: 'application/json;charset=UTF-8',
        url: "/updateNote",
        data: JSON.stringify({'data': input}),
        dataType: "json",
        cache: false,
        success: function(mssg){
          $("#msg").html(mssg)
          setTimeout(() =>{
            window.location.href = '/dashboard'
          },1000)
        },
        error: function(jqXHR, textStatus, errorThrown){
          $("#msg").html("<span class='flash red'>" + textStatus + " " + errorThrown + "</span>");
        }
      })
    })
  })

})


// Jquery function to delete note, not by checkbox selection
$(function(){
  $(document).ready(function(){
    $('#deleteNote').submit(function(event){
      event.preventDefault()
      const ids = $("input[name='note_id']",this).val();
      $.ajax({
        type: "POST",
        contentType: 'application/json;charset=UTF-8',
        url: "/deleteNote",
        data: JSON.stringify({'ids': ids}),
        dataType: "json",
        cache: false,
        success: function(msg){
          $("#msg").html(msg)
          setTimeout(() =>{
            window.location.href = '/dashboard'
          },1000)
        },
        error: function(jqXHR, textStatus, errorThrown){
          $("#msg").html("<span class='flash red'>" + textStatus + " " + errorThrown + "</span>");
        }

      });
    })
  })

})

// Jquery function to style note based on certain condition
$(function(){
  $(document).ready(function() {
    var dataTable = $('#myTable').dataTable()
    $(dataTable.fnGetNodes()).each(function(){
      var self = $(this);
      var col_value = self.find("td:eq(2)").text()
      if (col_value == "COMPLETED") {
        self.addClass("p-3 mb-2 bg-success text-white");
      }else if(col_value == "UNCOMPLETED"){
        self.addClass("p-3 mb-2 bg-danger text-white");
      }else{
        self.addClass("p-3 mb-2 bg-warning text-white")
      }
    })
  });
})