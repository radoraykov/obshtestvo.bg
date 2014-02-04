var AjaxForm = function ($container, extraValidationOptions, success, error) {
    this.$container = $container;
    this.success = success;
    this.error = error;
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
    success: null,
    error: null,

    block: function () {
        this.$container.block({
            message: null,
            overlayCSS: {
                backgroundColor: 'rgba(245, 245, 245, 0.6)',
                opacity: 1
            }
        });
        var $veil = this.$container.find('.blockOverlay');
        AjaxForm._genSpinner().spin($veil.get(0))
    },

    unblock: function () {
        this.$container.unblock();
    },

    _switchContent: function ($hide, $show, speed, final) {
        var self = this;
        var $container = self.$container.find('.animation-container');

        toggleFixedHeight($container, true)
        $container.animateContentSwitch($hide, $show, {
            speed: speed,
            width: false,
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
                    if ($.isFunction(self.success)) self.success(data);
                    $form.find('.msg').html(data.Status)
                    $form.addClass('success')
                },
                error: function (xhr, status, err) {
                    var error = xhr.responseJSON ? xhr.responseJSON.Status : err
                    if ($.isFunction(self.error)) self.error(error);
                    $form.find('.msg').html(error)
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
        $form.find(':text').on('input', function (e) {
            $(this).valid();
        })
    }
}

AjaxForm._genSpinner = function () {
    return new Spinner({
        top: 'auto',
        left: 'auto',
        lines: 15, // The number of lines to draw
        length: 0, // The length of each line
        width: 5, // The line thickness
        radius: 4, // The radius of the inner circle
        corners: 1, // Corner roundness (0..1)
        color: '#469704', // #rgb or #rrggbb
        speed: 1, // Rounds per second
        trail: 31, // Afterglow percentage
        shadow: false, // Whether to render a shadow
        hwaccel: true // Whether to use hardware acceleration
    })
}