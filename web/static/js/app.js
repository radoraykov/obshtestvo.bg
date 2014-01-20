$(function () {
    var $home = $(".home");
    if ($home.length) {
        initHome();
    }
    initNav();

    var $footer = $('footer')
    var $sidebar = $('#sidebar')
    if ($sidebar.length == 0) return;
    var elementPosition = $sidebar.offset();

    var sidebarBottomFix = function (isResize) {
        var scrollTop = $(window).scrollTop();
        var abstop = $sidebar.outerHeight() + 92 + $footer.outerHeight();
        var scrollPass = ($(document).height() - scrollTop) < abstop
        var shouldFix = isResize || !$sidebar.hasClass('bottom-hit');
        if (scrollPass && shouldFix) {
            $sidebar.addClass('bottom-hit')
            $sidebar.css({
                position: 'absolute',
                top: $footer.offset().top - $sidebar.outerHeight() + 'px'
            })
        } else if (!scrollPass) {
            $sidebar.removeClass('bottom-hit')
            $sidebar.css({
                position: '',
                top: ''
            })
        }
    }
    $(window).scroll(function () {
        var scrolledPass = $(window).scrollTop() > elementPosition.top - 92;
        if (scrolledPass && !$sidebar.hasClass('fixed')) {
            $sidebar.addClass('fixed')
        } else if (!scrolledPass && $sidebar.hasClass('fixed')) {
            $sidebar.removeClass('fixed')
        }
        sidebarBottomFix(false);
    });
    $(window).resize(function () {
        sidebarBottomFix(true);
    });

    $('#joinPosition').select2({
        'containerCssClass': 'joinPosition select2'
    })
    $('#joinPosition').change(function () {
        $(this).valid();
    });


    var $toc = $sidebar.find('.toc')
    var $headclone = $('.head').clone().addClass('hidden waiting').addClass('basic-transition-2x')
    $headclone.appendTo($sidebar.find('.nav'))

    $('.half-layout').waypoint(function (dir) {
        if (dir == 'down') {
            $headclone.unbind('.fix')
            $toc.unbind('.fix')
            showAnimated($headclone, function () {
                afterTransition($headclone, function () {
                    $headclone.addClass('static')
                })
            })
            $toc.addClass('waiting')
            hideAfterTransition($toc)
        } else {
            $headclone.unbind('.fix')
            $headclone.removeClass('static')
            $toc.unbind('.fix')
            showAnimated($toc)
            $headclone.addClass('waiting')
            hideAfterTransition($headclone)
        }
    }, {offset: -150})

    var $step2 = $sidebar.find('.step2')
    if ($step2.length == 0) return;
    $('.half-layout').waypoint(function (dir) {
        if (dir == 'down') {
            $step2.unbind('.fix')
            showAnimated($step2)
        } else {
            $step2.unbind('.fix')
            $step2.addClass('waiting')
            hideAfterTransition($step2)
        }
    }, {offset: -400})
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


    var $sidebar = $('#sidebar')
    if ($sidebar.length == 0) return;
    $('.half-layout').waypoint(function (dir) {
        if (dir == 'down') {
            $sub.addClass('light')
            $darkBackground.addClass('hidden');
            $lightBackground.removeClass('hidden');
        } else {
            $sub.removeClass('light')
            $darkBackground.removeClass('hidden');
            $lightBackground.addClass('hidden');
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
            this.$bar.css({
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
        this.$bar = $parent.find('.progress .bar')
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
                $nextTrigger.addClass('active');
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
            var $progressBarClone = $projectsPanel.find('.progress').clone();
            $fixedSliderNav.find('.slider-nav').append($progressBarClone)
            progress.$bar = $('.progress .bar')

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
            hideFixedProjectName()
        } else {
            showFixedSliderNav()
            showFixedProjectName()
        }
    }, { offset: 100})
    $forcesPanel.waypoint(function (dir) {
        if (dir == 'down') {
            progress.isPause = true;
        } else {
            progress.isPause = false;
        }
    }, { offset: 300})
}

var AjaxForm = function ($container, extraValidationOptions) {
    this.$container = $container;
    this._activateValidation(extraValidationOptions);
    this._ajaxify()
}

$.extend($.validator.messages, {
    required: "Без това няма как",
    remote: "Моля, въведете правилната стойност.",
    email: "Май не е точния email.",
    url: "Моля, въведете валидно URL.",
    date: "Моля, въведете валидна дата.",
    dateISO: "Моля, въведете валидна дата (ISO).",
    number: "Моля, въведете валиден номер.",
    digits: "Моля, въведете само цифри.",
    creditcard: "Моля, въведете валиден номер на кредитна карта.",
    equalTo: "Моля, въведете същата стойност отново.",
    extension: "Моля, въведете стойност с валидно разширение.",
    maxlength: $.validator.format("Моля, въведете повече от {0} символа."),
    minlength: $.validator.format("Моля, въведете поне {0} символа."),
    rangelength: $.validator.format("Моля, въведете стойност с дължина между {0} и {1} символа."),
    range: $.validator.format("Моля, въведете стойност между {0} и {1}."),
    max: $.validator.format("Моля, въведете стойност по-малка или равна на {0}."),
    min: $.validator.format("Моля, въведете стойност по-голяма или равна на {0}.")
});
AjaxForm.prototype = {
    $container: null,

    block: function () {
        this.$container.block({
            message: null,
            overlayCSS: {
                backgroundColor: 'rgba(255, 255, 255, 0.6)',
                opacity: 1
            }
        });
        var $veil = this.$container.find('.blockOverlay');
        this._genSpinner().spin($veil.get(0))
    },

    unblock: function () {
        this.$container.unblock();
    },

    _genSpinner: function () {
        return new Spinner({
            top: 'auto',
            left: 'auto',
            lines: 15, // The number of lines to draw
            length: 0, // The length of each line
            width: 5, // The line thickness
            radius: 4, // The radius of the inner circle
            corners: 1, // Corner roundness (0..1)
            color: '#000', // #rgb or #rrggbb
            speed: 1, // Rounds per second
            trail: 31, // Afterglow percentage
            shadow: false, // Whether to render a shadow
            hwaccel: true // Whether to use hardware acceleration
        })
    },

    _switchContent: function ($hide, $show, speed, final) {
        var self = this;
        var $container = self.$container.find('.animation-container');

        var toggleFixedHeight = function ($el, isFixed) {
            if (isFixed) {
                $el.height($el.height() + 'px');
                $el.css('overflow', 'hidden');
            } else {
                $el.css('height', '');
                $el.css('overflow', 'auto');
            }
        }
        toggleFixedHeight($container, true)
        $container.animateContentSwitch($hide, $show, {
            speed: speed,
            width: false,
            beforeShow: function (show) {
                // do stuff when both slides are hidden
                show();
            },
            final: function () {
                toggleFixedHeight($container, false)
                if ($.isFunction(final)) {
                    final()
                }
            }
        });
    },

    _ajaxify: function () {
        var self = this;
        var $form = self.$container;
        var handler = function (e) {
            e.preventDefault();
            if (!$form.valid()) {
                return false;
            }
            self.block();
            $.ajax({
                type: $form.find('input[name="X-Method"]').val() || $form.attr('method'),
                url: $form.attr('action'),
                data: $form.serialize(),
                dataType: "json",
                success: function (data) {
                    $form.css({
                        "background-image": 'url(http://www.gravatar.com/avatar/' + md5($form.find('#joinEmail').val()) + '.jpg?s=35&d=http%3A%2F%2Fwww.obshtestvo.bg%2Fstatic%2Fimg%2Fuser-silhouette.png)'
                    })
                    $form.find('.msg').html(data.Status)
                    $form.addClass('success')
                },
                error: function (xhr, status, err) {
                    $form.find('.msg').html(data.Status)
                    $form.addClass('error')
                },
                complete: function () {
                    self.unblock();
                    self._switchContent($form.find('.controls'), $form.find('.msg'), 100)
                }
            });
        };
        $form.find('button').click(handler)
        $form.submit(handler);
    },

    _activateValidation: function (extraValidationOptions) {
        var self = this;
        var $form = self.$container;
        $form.validate($.extend({}, {
            errorPlacement: function ($err, $el) {
                $err.appendTo($el.siblings('span.' + $el.attr('name') + '.err'))
            }
        }, extraValidationOptions));
    }
}

/**
 * Booting application.
 *
 * Waiting for various processes or services to finish loading and then trigger the correct actions
 */
// Wait for DOM
var initialisingDOM = $.Deferred()
$(function () {
    initialisingDOM.resolve()
})
// When DOM is ready
$.when(initialisingDOM).then(function () {
    var $form = $('form.join');
    $form.find('.msg.hide').css('display', 'none').removeClass('hide')
    var joinForm = new AjaxForm($form)
});
