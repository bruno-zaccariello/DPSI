window.onload = function() {
    
    $('[draggable]').draggable();
    $('[sortable]').sortable();
    $('[droppable]').droppable();
    $('[resizable=""]').resizable();
    $('.accordion').accordion({
        collapsible: true,
        active: false
    });

    $('[resizable=sidebar]').resizable({
        handles:"e"
    });

    $('[clickable]').css("cursor", "pointer");

    $('[slider]').each(function() {
        console.log(this);
        if ($(this).attr('slider') == 'priceRange') {
            $(this).slider({
                range: true,
                min: 0,
                max: 5000,
                values: [ 0, 1000 ],
                step: 50,
                classes: {
                    "ui-slider": "stm-slider",
                    "ui-slider-handle": "ui-corner-all",
                    "ui-slider-range": "ui-corner-all ui-widget-header"
                },
                slide: function( event, ui ) {
                  $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
                }
              });
              $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
                " - $" + $( "#slider-range" ).slider( "values", 1 ) );
        }
    })

    $('.nav-subitem').click(() => {
        $(this).parent()
    })

    $('[stm-flatten-form]').each(function() {
        let width = getLargest($(this).find('label'))
        $(this).find('label').each(function() {
            $(this).html(makeContent(this))
        })
    })

}

function HTML(html) {
    let template = document.createElement('template');
    html = html.trim();
    template.innerHTML = html;
    return template.content.firstChild;
}

function getLargest(elements) {
    let biggest = $(elements[0]).width();
    $(elements).each(function() {
        let size = $(this).width();
        if (size > biggest) {
            biggest = size;
        }
    })
    console.log(biggest)
    return biggest
}

function flattenFieldWrapper(label) {
    let field = label.find(':input');
    let replacement = "<span class='lbl-'>"+label.text()+"<>"
}