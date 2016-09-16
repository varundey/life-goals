$(document).ready(function() {
    $.ajax({
        url: '/goals/',
        type: 'GET',
        success: function(data) {
            // console.log(data);
            data = data.goals
            for (i=0; i < data.length; i++){
              var s = ("<h3>"+data[i].title+"</h3><div class='row'><div class='col-md-9'>"+data[i].end+"</div>");
              if(data[i].done===true){s+="<div class='col-md-1'><span class='glyphicon glyphicon-ok-circle'></span></div>"}
              else{s+="<div class='col-md-1'><span class='glyphicon glyphicon-minus'></span></div>"}
              s+=("<div class='col-md-1'><a class='btn btn-default' href='/goal/"+ data[i].id +"/edit/'><span class='glyphicon glyphicon-pencil'></span></a></div>");
              s+=("<div class='col-md-1'><a class='btn btn-danger' href='/goal/"+ data[i].id +"/delete/'><span class='glyphicon glyphicon-trash'></span></a></div>");
              s+="<p>"+ data[i].description +"</p><hr>"
              $(".container").append(s);
            }
        }
    });
});
