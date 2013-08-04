$(function() {
    var $animated = $('#content, a.contact');
    $animated.addClass('visible')
    // wait for animation to finish
    setTimeout(function() {
        $animated.removeClass('loaded')
    }, 600)
})
