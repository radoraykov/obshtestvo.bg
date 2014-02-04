function Nav($siteNav) {
    var $body = $('body');

    this.$el = $siteNav;
    this.$sub = $siteNav.find('.sub');
    this.$darkBackground = this.$sub.find('.dark');
    this.$lightBackground = this.$sub.find('.light');
    this.$aboutLink = $siteNav.find('li.about a');
    this.$topLinks = $siteNav.find('ul.top > li > a').not(this.$aboutLink);
    this.$subLinks = this.$sub.find('a');
    this.subLinksDOM = this.$subLinks.get();

    var self = this;

    $body.on('mousedown', function (e) {
        if ((!self.$aboutLink.is(e.target) && self.subLinksDOM.indexOf(e.target) == -1) && self.menuActive) {
            self.hideSubMenu(true)
        }
    })
    self.$aboutLink.click(function (e) {
        e.preventDefault();
        if (!self.menuActive) {
            self.showSubMenu(true)
        } else {
            self.hideSubMenu(true)
        }
    })
    self.$topLinks.click(function (e) {
        if (self.menuActive) {
            e.preventDefault();
            self.hideSubMenu(true)
        }
    })

}


Nav.prototype = {
    menuActive: false,
    automaticMenuHide: false,
    $el: null,
    $sub: null,
    $darkBackground: null,
    $lightBackground: null,
    $aboutLink: null,
    $topLinks: null,
    $subLinks: null,
    subLinksDOM: null,

    hideSubMenu: function (isTriggeredByUser) {
        var self = this;
        self.$sub.unbind('.fix')
        self.$sub.addClass('waiting')
        self.$el.find('ul.top').removeClass('about')
        hideAfterTransition(self.$sub, function () {
            self.menuActive = false;
        })
        if (isTriggeredByUser) {
            self.automaticMenuHide = true;
        }
    },

    showSubMenu: function (isTriggeredByUser) {
        var self = this;
        self.menuActive = true;
        self.$sub.unbind('.fix')
        showAnimated(self.$sub, function () {
            self.$el.find('ul.top').addClass('about')
        })
        if (isTriggeredByUser) {
            self.automaticMenuHide = false;
        }
    },

    switchTheme: function (theme) {
        var self = this;
        if (theme == 'light') {
            self.$sub.addClass('light')
            self.$darkBackground.addClass('hidden');
            self.$lightBackground.removeClass('hidden');
        } else {
            self.$sub.removeClass('light')
            self.$darkBackground.removeClass('hidden');
            self.$lightBackground.addClass('hidden');
        }
    }
}