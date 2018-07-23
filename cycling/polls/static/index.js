

var envio = document.querySelector('button');
    envio.onclick = function(){

	var miTitulo = document.querySelector('h3');
	miTitulo.innerHTML = 'funciona js!';
	//hasta aqui arriba funciona ajax aun nop
	var formData = new FormData(this);
    	$.ajax({
    		type: "POST",
    		url: "views.py/post",
    		data: formData,
    		processData: false,
            contentType: false,
            success:function(response){
                var message = response.content.message
                alert(message);
            },
        });




};




		

	
   
