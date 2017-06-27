console.log("carregado");
function Altera_Campo() {
	console.log("alterou");
	var id = $("#id_turma_idturma").val();
	console.log(id);
	
    console.log("Evento AJAX");
    
    $.ajax({
        url : "/return_disciplina/",
        type : "POST",
        data : { 
            id : id
             },
        success : function(json) {
            $("#idDiciplina").html("");
            console.log(json)
             $('#idDiciplina').append("<option value='' selected='selected'>Disciplinas</option>");
            for (var i = 0; i < json.length; i++) {
            	$('#idDiciplina').append("<option value="+json[i][0]+">" + json[i][1] + "</option>");
            }

            }

    }); 
  // var idDiciplina = $("#idDiciplina").val(); 
  // console.log(idDiciplina);
  var idDiciplina = $("#idDiciplina").val(); 
   	console.log(idDiciplina);
    var id_nome = $("#id_nome").val();
    console.log(id_nome); 
    var id_descricao = $("#id_descricao").val(); 



}

function register(){
	 var idDiciplina = $("#idDiciplina").val(); 
   	console.log(idDiciplina);
    	var id_nome = $("#id_nome").val();
    console.log(id_nome); 
    	var id_descricao = $("#id_descricao").val(); 
    console.log(id_descricao); 
  
   if (idDiciplina == '' || id_nome == '' || id_descricao == '') {
            alert("Complete todos os campos!");
        } else{
           
            $.ajax({
                url : "/registrar/",
                type : "POST",
                data : { 
                    assunto : id_nome,
                    descricao : id_descricao,
                    iddisciplina : idDiciplina,
                     },

                success : function(json) {
                	$("#id_nome").val("");
                    $("#id_descricao").val("");
                    alert("Cadastrado com Sucesso");


                },

                
            }); 
        }


}

function register_user(){
	 var username = $("#id_username").val();
	 var nome = $("#id_nome").val(); 
	 var sobrenome = $("#id_sobrenome").val(); 
	 var email = $("#id_email").val(); 
	 var senha = $("#id_senha").val(); 
	 var nivel = $("#id_Nivel").val();
	 var escola = $("#id_Escola").val();

   	console.log(nome);
   	console.log(sobrenome);
   	console.log(email);
   	console.log(senha);
   	console.log(nivel);
   	console.log(escola);
 	
  
   if (username == '' || nome == '' || sobrenome == '' || email == '' || senha == '' || nivel == '' || escola == '') {
            alert("Complete todos os campos!");
        } else{
           
            $.ajax({
                url : "/reg/",
                type : "POST",
                data : { 
                    username : username,
                    nome : nome,
                    sobrenome : sobrenome,
                    email : email,
                    senha : senha,
                    nivel : nivel,
                    escola : escola
                     },

                success : function(json) {
                	$("#id_nome").val("");
                    $("#id_descricao").val("");
                    alert("Cadastrado com Sucesso");


                },
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);

                }

                
            }); 
        }
	

}



$('#register').submit(function() {
    var form = $(this);
    $('.t1').addClass("semfunc");
    $.post(form.attr('action'), form.serialize(), function(retorno) {
        
        var idDiciplina = $("#idDiciplina").val(); 
   	console.log(idDiciplina);
    	var id_nome = $("#id_nome").val();
    console.log(id_nome); 
    	var id_descricao = $("#id_descricao").val(); 

       /* if (idDiciplina == '' || id_nome == '' || id_descricao == '') {
            $('.t2').removeClass("semfunc");
        } else{
           
            $.ajax({
                url : "/registrar/",
                type : "POST",
                data : { 
                    assunto : id_nome,
                    descricao : id_descricao,
                    disciplina_iddisciplina : idDiciplina,
                     },

                success : function(json) {
                    console.log("Resultado do processamento: "+json);
                                
                },

                
            }); 
        } */
    });
    
});



function cadastraAssunto() {


	var idDiciplina = $("#idDiciplina").val(); 
   	console.log(idDiciplina);
    var id_nome = $("#id_nome").val();
    console.log(id_nome); 
    var id_descricao = $("#id_descricao").val(); 

}


function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });