$(function () {
    var $home = $(".home");
    if ($home.length) {
        initNav();
        initHome();
    }
});

function initNav() {
    var $fixedNav = $('nav.main');
    $fixedNav.drop
}

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


    var $sub = $('.sub');
    var $darkBackground = $sub.find('.dark');
    var $lightBackground = $sub.find('.light');
    var $aboutLink = $fixedNav.find('li.about a');
    var $topLinks = $fixedNav.find('ul.top > li > a').not($aboutLink);
    var $subLinks = $sub.find('a');
    var menuActive = false;
    var hideSubMenu = function () {
        $sub.addClass('waiting')
        $fixedNav.find('ul.top').removeClass('about')
        menuActive = false;
    }
    $('body').on('click', function (e) {
        if ((!$aboutLink.is(e.target) && $subLinks.get().indexOf(e.target) == -1) && menuActive) {
            hideSubMenu();
        }
    })
    $aboutLink.click(function (e) {
        e.preventDefault();
        if (!menuActive) {
            $sub.removeClass('waiting')
            $fixedNav.find('ul.top').addClass('about')
            menuActive = true;
        } else {
            hideSubMenu();
        }
    })
    $subLinks.click(function (e) {
        e.preventDefault();
        console.log('asdasd')
    })
    $topLinks.click(function (e) {
        if (menuActive) {
            e.preventDefault();
            hideSubMenu()
        }
    })


    $('#projects').waypoint(function (dir) {
        if (dir == 'down') {
            $sub.addClass('light')
            $darkBackground.addClass('hidden');
            $lightBackground.removeClass('hidden');
        } else {
            $sub.removeClass('light')
            $darkBackground.removeClass('hidden');
            $lightBackground.addClass('hidden');
        }
    }, { offset: 125})

}