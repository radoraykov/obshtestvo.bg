$(function() {
    var $home =  $(".home");
    if ($home.length) {
        initHome();
    }
});

function initHome() {
    var $slider = $(".slider");
    var $slides = $slider.find('.item')
    var slidesCount = $slides.length;
    var $prevTrigger =  $(".slider-nav .nav.prev");
    var $nextTrigger =  $(".slider-nav .nav.next");

    var slider = $slider.owlCarousel({
        navigation : false,
        pagination : false,
        autoHeight : true,
        slideSpeed : 400,
        paginationSpeed : 400,
        singleItem:true,
        afterAction: function() {
            if (this.owl.currentItem == 0) {
                $prevTrigger.removeClass('active');
            } else if (this.owl.currentItem == slidesCount-1) {
                $nextTrigger.removeClass('active');
            } else {
                $prevTrigger.addClass('active');
                $nextTrigger.addClass('active');
            }
        }
        // "singleItem:true" is a shortcut for:
        // items : 1,
        // itemsDesktop : false,
        // itemsDesktopSmall : false,
        // itemsTablet: false,
        // itemsMobile : false

    });
    // Custom Navigation Events
    $prevTrigger.click(function(){
        if ($prevTrigger.hasClass('active')) {
            slider.trigger('owl.prev');
        }
    })
    $nextTrigger.click(function(){
        if ($nextTrigger.hasClass('active')) {
            slider.trigger('owl.next');
        }
    })
}