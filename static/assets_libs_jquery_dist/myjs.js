function submit(){
    let mobile=$('#Mobile').val();
    let name=$('#name').val();
    let re = /^[0-9]{10}$/;
    let re_name=/^([a-zA-Z]*[ ]*[a-zA-Z]*)$/;
    if (re.test(mobile) && re_name.test(name)) {
        if($('#name').val().length!=0 && $('#Mobile').val().length!=0 && $('#Query').val().length!=0)
        {
            $.ajax({
                type:'POST',
                url:'/post_query/',
                data:{
                    name:$('#name').val(),
                    Mobile:$('#Mobile').val(),
                    Query:$('#Query').val(),
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                },
                success:function(data){
                    console.log(data.msg);
                    alert(data.msg);
                },
                error: function (jqXHR, exception) {
                    console.log(jqXHR);
                }
            });
        }
        else{
            if($('#name').val().length==0)
            {
                alert("Provide Name");
                focus('#name');
            }
            else if($('#Mobile').val().length==0)
            {
                alert("Provide Mobile");
                focus('#Mobile');
            }
            else if($('#Query').val().length==0)
            {
                alert("Provide Message");
                focus('#Query');
            }
        }
    }
    else {
            if(!re_name.test(name))
            {
                alert("Provide correct Name");
                focus('#name');
            }
            else if(!re.test(mobile))
            {
                alert("Provide correct Mobile");
                focus('#Mobile');
            }
    }
}