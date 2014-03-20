function FacebookAuth(appId, callback) {
    var self = this;
    this.loginCallback = callback;

    $.ajaxSetup({ cache: true });
    $.getScript('//connect.facebook.net/en_UK/all.js', function () {
        FB.init({
            appId: appId,
            status: true, // check login status
            cookie: true, // enable cookies to allow the server to access the session
            logging: true, // enable cookies to allow the server to access the session
        });
//        FB.Event.subscribe('auth.authResponseChange', statusUpdate);
        FB.getLoginStatus(self._createStatusChangeHandler());
    });
}

FacebookAuth.prototype = {

    loginCallback: null,

    /**
     * Authenticate user on
     *
     * @param {String} accessToken
     */
    serverAuth: function(accessToken) {
        $.ajax({
            type: "post",
            url: '/token/facebook/',
            data: {
               "auth_token": accessToken
            },
            dataType: "json",
            success: function (response, status, xhr) {
               if (xhr.status = 202) {
                   console.log(202)
                   //show form trigger form to complete details
               } else {
                   console.log(response)
               }
            },
            error: function (xhr, status, err) {
               console.log(err, status);
            }
        });
    },

    loginPrompt: function() {
        return FB.login();
    },

    getUserDetails: function(callback) {
        FB.api('/me', function (response) {
            callback(response);
        });
    },

    _createStatusChangeHandler: function() {
        var self = this;
        return function(response) {
            if (response.status === 'connected') {
                // user logged in facebook and authorized app
                self.serverLogin(response.authResponse.accessToken)
                self.getUserDetails();
            } else if (response.status === 'not_authorized') {
                // user logged in facebook but haven't authorized app
            } else {
                // user logged in facebook
            }
        }
    }
}