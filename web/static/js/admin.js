
$(function() {

    $('select').each(function() {
        var $select = $(this)
        var options = {}
        if ($select.find('option').length < 7) {
            options['minimumResultsForSearch'] = -1
        }

        if ($select.is('[multiple]')) {
            $select.siblings('.help-inline').addClass('hide')
        } else {
            options['formatSelection'] =  function (item) {
                return item.text + ' <i class="info">('+$select.data('placeholder')+')</i>';
            }
        }
        $select.select2($.extend({
            width: $select.width(),
            allowClear: true
        },options))
    })
    $('.select2-chosen').on('mouseenter', function(){
        var $this = $(this);

        if(this.offsetWidth < this.scrollWidth && !$this.attr('title')){
            $this.attr('title', $this.text());
    }
});
})

function dismissAddAnotherPopup(win, newId, newRepr) {
    // newId and newRepr are expected to have previously been escaped by
    // django.utils.html.escape.
    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem) {
        var elemName = elem.nodeName.toUpperCase();
        if (elemName == 'SELECT') {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
            $(elem).trigger('change')
        } else if (elemName == 'INPUT') {
            if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
                elem.value += ',' + newId;
            } else {
                elem.value = newId;
            }
        }
    } else {
        var toId = name + "_to";
        elem = document.getElementById(toId);
        var o = new Option(newRepr, newId);
        SelectBox.add_to_cache(toId, o);
        SelectBox.redisplay(toId);
    }
    win.close();
}
