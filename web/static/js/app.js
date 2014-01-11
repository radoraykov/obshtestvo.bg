$(function () {
    var $home = $(".home");
    if ($home.length) {
        initHome();
    }
    initNav();

    var $sidebar = $('#sidebar')
    if ($sidebar.length == 0) return;
    var elementPosition = $sidebar.offset();

    $(window).scroll(function () {
        if ($(window).scrollTop() > elementPosition.top - 92) {
            $sidebar.addClass('fixed')
        } else {
            $sidebar.removeClass('fixed')
        }
    });
});

var afterTransition = function ($el, callback) {
    $el.bind("webkitTransitionEnd.fix transitionend.fix oTransitionEnd.fix", function () {
        if ($.isFunction(callback)) callback();
    });
}

var hideAfterTransition = function ($el, callback) {
    afterTransition($el, function () {
        $el.addClass('hidden')
        if ($.isFunction(callback)) callback();
    })
}
var showAnimated = function ($el, callback) {
    $el.removeClass('hidden')
    setTimeout(function () {
        $el.removeClass('waiting')
        if ($.isFunction(callback)) callback();
    }, 30)
}
var speedUpAnimationAfterTransition = function ($el) {
    $el.bind("webkitTransitionEnd.fix transitionend.fix oTransitionEnd.fix", function () {
        $el.removeClass('basic-transition-slow')
        $el.addClass('basic-transition')
    });
}

function initNav() {
    var $fixedNav = $('nav.main')
    var $body = $('body');
    var $sub = $fixedNav.find('.sub');
    var $darkBackground = $sub.find('.dark');
    var $lightBackground = $sub.find('.light');
    var $aboutLink = $fixedNav.find('li.about a');
    var $topLinks = $fixedNav.find('ul.top > li > a').not($aboutLink);
    var $subLinks = $sub.find('a');
    var subLinksDOM = $subLinks.get();
    var menuActive = false;
    var automaticMenuHide = false;
    // Fixed slider navigation
    var $projectsPanel = $('#projects');
    var $forcesPanel = $('#forces');
    var $projectsSliderNav = $projectsPanel.find('.slider-nav')


    var hideSubMenu = function () {
        $sub.unbind('.fix')
        $sub.addClass('waiting')
        $fixedNav.find('ul.top').removeClass('about')
        hideAfterTransition($sub, function () {
            menuActive = false;
        })
    }

    var showSubMenu = function () {
        menuActive = true;
        $sub.unbind('.fix')
        showAnimated($sub, function () {
            $fixedNav.find('ul.top').addClass('about')
        })
    }
    $body.on('mousedown', function (e) {
        if ((!$aboutLink.is(e.target) && subLinksDOM.indexOf(e.target) == -1) && menuActive) {
            hideSubMenu();
        }
    })
    $aboutLink.click(function (e) {
        e.preventDefault();
        if (!menuActive) {
            showSubMenu();
        } else {
            hideSubMenu();
        }
    })
    $topLinks.click(function (e) {
        if (menuActive) {
            e.preventDefault();
            hideSubMenu()
        }
    })

    $projectsPanel.waypoint(function (dir) {
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


    $projectsSliderNav.waypoint(function (dir) {
        if (dir == 'down') {
            if (menuActive) {
                hideSubMenu();
                automaticMenuHide = true;
            }
        } else {
            if (automaticMenuHide) {
                showSubMenu()
                automaticMenuHide = false;
            }
        }
    }, { offset: 60})

    $forcesPanel.waypoint(function (dir) {
        if (dir == 'down') {
            if (automaticMenuHide) {
                showSubMenu()
                automaticMenuHide = false;
            }
        } else {
            if (menuActive) {
                hideSubMenu();
                automaticMenuHide = true;
            }
        }
    }, { offset: 100})
}


function ProgressBar($parent) {
    this.time = 7;
    this.$parent = $parent;
}
ProgressBar.prototype = {
    time: undefined,
    isPause: false,
    tick: undefined,
    percentTime: undefined,
    $progressBar: undefined,
    $bar: undefined,
    $parent: undefined,
    $elem: undefined,
    moved: function () {
        //clear interval
        clearTimeout(this.tick);
        //start again
        this.start();
    },
    pauseOnDragging: function () {
        this.isPause = true;
    },
    init: function ($elem) {
        var self = this;
        self.$elem = $elem;
        self.$elem.on('mouseover', function () {
            self.isPause = true;
        })
        self.$elem.on('mouseout', function () {
            self.isPause = false;
        })
        self.$elem.on('mouseup', function () {
            self.isPause = false;
        })
        self.build(self.$parent)
        self.start()
    },
    _interval: function () {
        if (this.isPause === false) {
            this.percentTime += 1 / this.time;
            $('.slider-nav .progress .bar').css({
                width: this.percentTime + "%"
            });
            //if percentTime is equal or greater than 100
            if (this.percentTime >= 100) {
                //slide to next item
                this.$elem.trigger('owl.next')
            }
        }
    },
    start: function () {
        var self = this;
        //reset timer
        this.percentTime = 0;
        this.isPause = false;
        //run interval every 0.01 second
        this.tick = setInterval(function () {
            self._interval()
        }, 10);
    },
    build: function ($parent) {
        this.$progressBar = $("<div>", {
            class: "progress"
        });
        this.$bar = $("<div>", {
            class: "bar"
        });
        this.$progressBar.append(this.$bar).prependTo($parent);
    }
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
    // Fixed slider navigation
    var $projectsPanel = $('#projects');
    var $forcesPanel = $('#forces');
    var $projectsSliderNav = $projectsPanel.find('.slider-nav')

    var progress = new ProgressBar($('#projects .slider-nav'));
    var slider = $slider.owlCarousel({
        navigation: false,
        pagination: false,
        autoHeight: true,
        slideSpeed: 500,
        paginationSpeed: 400,
        singleItem: true,
        // "singleItem:true" is a shortcut for:
        // items : 1,
        // itemsDesktop : false,
        // itemsDesktopSmall : false,
        // itemsTablet: false,
        // itemsMobile : false
        afterAction: function () {
            var projectName = $(this.owl.owlItems[this.owl.visibleItems[0]]).find('header .heading').text()
            $fixedProjectNameHelper.html(projectName)
            if (this.owl.currentItem == 0) {
                $prevTrigger.removeClass('active');
            } else if (this.owl.currentItem == slidesCount - 1) {
                $nextTrigger.removeClass('active');
            } else {
                $prevTrigger.addClass('active');
                $nextTrigger.addClass('active');
            }
            setTimeout(function () {
                $.waypoints('refresh');
            }, 500)
        },
        afterInit: function ($elem) {
            progress.init($elem)
            $fixedSliderNav.find('.slider-nav').append($projectsPanel.find('.progress').clone())
        },
        afterMove: function () {
            progress.moved()
        },
        startDragging: function () {
            progress.pauseOnDragging()
        }

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
    $nextTrigger.add($prevTrigger).attr('unselectable', 'on')
        .css({'-moz-user-select': '-moz-none',
            '-moz-user-select': 'none',
            '-o-user-select': 'none',
            '-khtml-user-select': 'none', /* you could also put this in a class */
            '-webkit-user-select': 'none', /* and add the CSS class here instead */
            '-ms-user-select': 'none',
            'user-select': 'none'
        }).bind('selectstart', function () {
            ;
            return false;
        });

    var showFixedSliderNav = function () {
        $fixedSliderNav.unbind('.fix')
        $fixedSliderNav.removeClass('hidden')
        showAnimated($fixedSliderNav);
    }
    var hideFixedSliderNav = function () {
        $fixedSliderNav.unbind('.fix')
        hideAfterTransition($fixedSliderNav)
        $fixedSliderNav.addClass('waiting')
    }

    var showFixedProjectName = function () {
        $fixedProjectName.unbind('.fix')
        speedUpAnimationAfterTransition($fixedProjectName)
        showAnimated($fixedProjectName);
    }

    var hideFixedProjectName = function () {
        $fixedProjectName.unbind('.fix')
        hideAfterTransition($fixedProjectName, function () {
            //slows animation down
            $fixedProjectName.removeClass('basic-transition')
            $fixedProjectName.addClass('basic-transition-slow')
        })
        $fixedProjectName.addClass('waiting')
    }

    $projectsSliderNav.waypoint(function (dir) {
        if (dir == 'down') {
            showFixedSliderNav()
        } else {
            hideFixedSliderNav()
        }
    }, { offset: 50})

    $projectsSliderNav.waypoint(function (dir) {
        if (dir == 'down') {
            showFixedProjectName()
        } else {
            hideFixedProjectName()
        }
    }, { offset: -20})

    $forcesPanel.waypoint(function (dir) {
        if (dir == 'down') {
            hideFixedSliderNav()
            progress.isPause = true;
            hideFixedProjectName()
        } else {
            progress.isPause = false;
            showFixedSliderNav()
            showFixedProjectName()
        }
    }, { offset: 100})
}