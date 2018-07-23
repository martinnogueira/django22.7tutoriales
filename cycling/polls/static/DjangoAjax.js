
/**
 * Este script de javascript permite trabajar transparentemente solicitudes que requieren 
 * protección del token CSRF por medio de AJAX JQUERY.
 * Esto te permitirá hacer solcitudes a web Services de Django por medio de AJAX Jquery.
 * Para utilizarlo basta con integrar el archivo DjangoAjax.js en tu directorio de JS  y hacer referencia a él en tus templates 
 * que requieren del uso de AJAX por POST o algún otro que requiera el token CSRF.
 * Este script está basado en la documentación oficial de Django https://docs.djangoproject.com
 */

$(function(){
    //Obtenemos la información de csfrtoken que se almacena por cookies en el cliente
    var csrftoken = getCookie('csrftoken');

    //Agregamos en la configuración de la funcion $.ajax de Jquery lo siguiente:
    $.ajaxSetup({
                    beforeSend: function(xhr, settings) {
                        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                            // Send the token to same-origin, relative URLs only.
                            // Send the token only if the method warrants CSRF protection
                            // Using the CSRFToken value acquired earlier
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        }
                    }
    });

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

// usando jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


    function csrfSafeMethod(method) {
        // estos métodos no requieren CSRF
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
});
@daronwolff
daronwolff commented on Sep 7, 2015

Pero si esto es una maravilla!! Muchas gracias!!
@vaj25
vaj25 commented on Jan 16, 2016

Me sera de mucha ayuda. Gracias.
@illkufe
illkufe commented on Mar 17, 2016

Muchas gracias Señor, será de muy util
@alexdzul
alexdzul commented on Jun 8, 2016

Super!!!! Me ayudará bastante :D
@ragnarok22
ragnarok22 commented on Nov 15, 2016

Thanks
@Alfredynho
Alfredynho commented on Feb 2, 2017

definitivamente me salvaste la vida gracias Gaspar
@JCHR14
JCHR14 commented on Apr 17

Gracias bro
@martinnogueira

Attach files by dragging & dropping,

, or pasting from the clipboard.
Styling with Markdown is supported

    © 2018 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    API
    Training
    Shop
    Blog
    About

Press h to open a hovercard with more details.
