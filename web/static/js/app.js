$(function () {
    var $home = $(".home");
    if ($home.length) {
        initHome();
    }
});

function initHome() {
    var $slider = $(".slider");
    var $slides = $slider.find('.item')
    var slidesCount = $slides.length;
    var $prevTrigger = $(".slider-nav .nav.prev");
    var $nextTrigger = $(".slider-nav .nav.next");
    var $fixedNav = $('nav.main')
    var $fixedSliderNav = $fixedNav.find('.slider-nav-wrapper')
    var $fixedProjectName = $fixedNav.find('.title-holder')
    var $fixedProjectNameHelper = $fixedProjectName.find('.helper')

    var slider = $slider.owlCarousel({
        navigation: false,
        pagination: false,
        autoHeight: true,
        slideSpeed: 400,
        paginationSpeed: 400,
        singleItem: true,
        afterAction: function () {
            $fixedProjectNameHelper.html($(this.owl.owlItems[this.owl.visibleItems[0]]).find('header .heading').text())
            if (this.owl.currentItem == 0) {
                $prevTrigger.removeClass('active');
            } else if (this.owl.currentItem == slidesCount - 1) {
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
    $prevTrigger.click(function () {
        if ($prevTrigger.hasClass('active')) {
            slider.trigger('owl.prev');
        }
    })
    $nextTrigger.click(function () {
        if ($nextTrigger.hasClass('active')) {
            slider.trigger('owl.next');
        }
    })


    $('#projects .slider-nav').waypoint(function (dir) {
        if (dir == 'down') {
            $fixedSliderNav.unbind('.fix')
            $fixedSliderNav.removeClass('hidden')
            setTimeout(function () {
                $fixedSliderNav.removeClass('waiting')
            }, 30)
        } else {
            $fixedSliderNav.addClass('waiting')
            $fixedSliderNav.bind("webkitTransitionEnd.fix transitionend.fix oTransitionEnd.fix", function () {
                $fixedSliderNav.addClass('hidden')
            });
        }
    }, { offset: 60})

    $('#projects .slider-nav').waypoint(function (dir) {
        if (dir == 'down') {
            $fixedProjectName.unbind('.fix')
            $fixedProjectName.bind("webkitTransitionEnd.fix transitionend.fix oTransitionEnd.fix", function () {
                $fixedProjectName.removeClass('basic-transition-slow')
                $fixedProjectName.addClass('basic-transition')
            });
            $fixedProjectName.removeClass('hidden')
            setTimeout(function () {
                $fixedProjectName.removeClass('waiting')
            }, 30)
        } else {
            $fixedProjectName.unbind('.fix')
            $fixedProjectName.bind("webkitTransitionEnd.fix transitionend.fix oTransitionEnd.fix", function () {
                $fixedProjectName.addClass('hidden')
                $fixedProjectName.removeClass('basic-transition')
                $fixedProjectName.addClass('basic-transition-slow')
            });
            $fixedProjectName.addClass('waiting')
        }
    }, { offset: -20})

    $('#forces').waypoint(function (dir) {
        if (dir == 'down') {
            $fixedSliderNav.addClass('waiting')
            $fixedSliderNav.bind("webkitTransitionEnd.fix transitionend.fix oTransitionEnd.fix", function () {
                $fixedSliderNav.addClass('hidden')
            });
            $fixedProjectName.unbind('.fix')
            $fixedProjectName.bind("webkitTransitionEnd.fix transitionend.fix oTransitionEnd.fix", function () {
                $fixedProjectName.addClass('hidden')
                $fixedProjectName.removeClass('basic-transition')
                $fixedProjectName.addClass('basic-transition-slow')
            });
            $fixedProjectName.addClass('waiting')
        } else {
            $fixedSliderNav.unbind('.fix')
            $fixedSliderNav.removeClass('hidden')
            setTimeout(function () {
                $fixedSliderNav.removeClass('waiting')
            }, 30)
            $fixedProjectName.unbind('.fix')
            $fixedProjectName.bind("webkitTransitionEnd.fix transitionend.fix oTransitionEnd.fix", function () {
                $fixedProjectName.removeClass('basic-transition-slow')
                $fixedProjectName.addClass('basic-transition')
            });
            $fixedProjectName.removeClass('hidden')
            setTimeout(function () {
                $fixedProjectName.removeClass('waiting')
            }, 30)
        }
    }, { offset: 100})
}