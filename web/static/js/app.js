var app = {
    $nav: null,
    nav: null,
    $footer: null,
    $content: null,
    panels: {}
};
if ($.blockUI) {
    $.blockUI.defaults.css = {};
    $.blockUI.defaults.overlayCSS =  {
        backgroundColor: '#09232c',
        opacity:         0.95,
        cursor:          'wait'
    }
}
if ($.magnificPopup) {
    $.extend(true, $.magnificPopup.defaults, {
        enableEscapeKey: false,
        removalDelay: 300,
        closeOnBgClick: false,
        mainClass: 'mfp-zoom-in',
        callbacks: {
            open: function() {
                $('nav.main > div').css('padding-right', $('html').css('margin-right'));
            },
            close: function() {
                $('nav.main > div').css('padding-right',0)
            }
        }
    });
}
$(function () {
    if (Modernizr.input.placeholder) $('html').addClass('placeholder')

    app.$nav = $('nav.main');
    app.nav = new Nav(app.$nav);
    app.$footer = $('footer');

    var home = $(".home");
    if (home.length) home = new HomePage(home);

    var $innerPage = $('.inner')
    if ($innerPage.length) {
        app.$content = $innerPage.find('.half-layout')
        app.$content.waypoint(function (dir) {
            if (dir == 'down') {
                app.nav.switchTheme('light')
            } else {
                app.nav.switchTheme('dark')
            }
        }, { offset: 100})
    }

    var support = $innerPage.filter('.support');
    if (support.length) support = new SupportPage(support);

    var project = $innerPage.filter('.project');
    if (project.length) project = new ProjectPage(project);

    var about = $innerPage.filter('.about');
    if (about.length) about = new AboutPage(project);

    var report = $innerPage.filter('.report');
    if (report.length) report = new ReportPage(report);
});


function ProjectPage($context) {

    var $form = $context.find('form.join');
    $form.find('.msg.hidden').css('display', 'none').removeClass('hidden')
    var joinForm = new AjaxForm($form, {
        success: function () {
            $form.css({
                "background-image": 'url(http://www.gravatar.com/avatar/' + md5($form.find('#joinEmail').val()) + '.jpg?s=35&d=http%3A%2F%2Fwww.obshtestvo.bg%2Fstatic%2Fimg%2Fuser-silhouette.png)'
            })
        }
    })
    var $joinPosition = $('#joinPosition')
    $joinPosition
        .select2({
            'containerCssClass': 'joinPosition select2'
        })
        .change(function () {
            $(this).valid();
        });

    var sidebar = new Sidebar($('#sidebar'), {
        $waypoint: app.$content
    });
}

function AboutPage($context) {
    var sidebar = new Sidebar($('#sidebar'), {
        $waypoint: app.$content,
        step2: {
            $waypoint: app.$content,
            offset: -400
        }
    });
}

function ReportPage($context) {
    var sidebar = new Sidebar($('#sidebar'), {
        $waypoint: app.$content,
        offsets: {
            screenReduce: false
        }
    });
}


function HomePage($context) {
    app.panels.$forces = $('#forces')

    var carousel = new Carousel({
        containerSelector: '#projects',
        pauseBelow: {
            $waypoint: app.panels.$forces
        }
    })
    app.panels.$projects = carousel.$container;

    var carouselFixedNav = new FixedCarouselNav({
        'carousel': carousel,
        $context: app.$nav,
        containerSelector: '.slider-nav-wrapper',
        slideTitleSelector: '.title-holder',
        waypoints: {
            $up: carousel.$nav,
            $down: app.panels.$forces
        }
    })
    carousel.init()

    app.panels.$projects.waypoint(function (dir) {
        if (dir == 'down') {
            app.nav.switchTheme('light')
        } else {
            app.nav.switchTheme('dark')
        }
    }, { offset: 125})
}