function __init()
{

    $('#search_input')
        .val('')
        .focus()
        .keyup(function(){

            if(!$.trim($(this).val()))
                $('.results .error').empty().hide();
        });

    var cache = {};
    $('#search_input').autocomplete({
        minLength: 2,
        select: function( event, ui ) {
            return false;
        },
        open: function() {
            $('.results .wrapper').html($(this).autocomplete("widget").html());
            $(this).autocomplete("widget").hide();
        },
        source: function( request, response ) {

            if (cache[request.term]) {
                response(cache[request.term]);
                return;
            }

            $.ajax({
                dataType : 'json',
                method : 'POST',
                url : '/ajax/search/',
                data : {
                    q : encodeURIComponent(request.term),
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success : function(data) {
                    var users = [];

                    for(var x in data)
                    {
                        users.push({
                            sender : data[x].fields['sender'],
                            folio : data[x].fields['folio'],
                            date : data[x].fields['date']
                        });
                    }

                    cache[request.term] = users;
                    response(users);
                }
            });
        },
        response: function(event, ui) {

            if (ui.content.length === 0) {
                $('.results .error').html('No se encontraron resultados').show();
                $('.results .wrapper').empty();
            }
            else
                $('.results .error').empty().hide();
        }
    }).autocomplete('instance')._renderItem = function(ul, item) {

        var user_tmpl = $('<div />')
                        .addClass('sender')
                        .append('<a href="/" />').find('a').addClass('sender').html(item.sender)
                        .parent()
                        .append('<span class="identity"><strong>Identidad:</strong><span></span></span>')
                        .find('.folio > span').append(item.folio)
                        .parent().parent()
                        .append('<span class=""><strong>Email:</strong><span></span></span>')
                        .find('.date > span').append(item.sender)
                        .parent().parent();

        return $('<div></div>')
            .data('item.autocomplete', item)
            .append(user_tmpl)
            .appendTo(ul);
    };
}

$(document).ready(__init);