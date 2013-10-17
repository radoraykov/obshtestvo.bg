$(function() {
    var $menu = $('.sticky');
    var s = skrollr.init({
        render: function(data) {
//           if ($menu.css('opacity')==1) {
//               $menu.css('top', 0)
//           }
        }
    });
//    var $veil = $('#veil')
//    new Spinner({
//        top: 'invalid',
//        left: 'invalid',
//        lines: 15, // The number of lines to draw
//        length: 0, // The length of each line
//        width: 5, // The line thickness
//        radius: 4, // The radius of the inner circle
//        corners: 1, // Corner roundness (0..1)
//        color: '#546574', // #rgb or #rrggbb
//        speed: 1, // Rounds per second
//        trail: 31, // Afterglow percentage
//        shadow: false, // Whether to render a shadow
//        hwaccel: true // Whether to use hardware acceleration
//    }).spin($veil.get(0));
//    $('<img/>').attr('src', 'img/bg.png').load(function() {
//        $veil.fadeOut(300)
//        var $animated = $('#content, a.contact');
//        $animated.addClass('visible')
//        // wait for animation to finish
//        setTimeout(function() {
//            $animated.removeClass('loaded')
//        }, 600)
//    });

})

$(document).ready(function(){
    $('.bxslider').bxSlider({
    	auto: true,
    	pause: 6000,
  		autoControls: true
    });

});
