/*
 * View model for Google Drive Backup
 *
 * Author: jneilliii
 * License: MIT
 */
const redirectHost = `https://jneilliii.github.io`;
const redirectUri = `${redirectHost}/OctoPrint-GoogleDriveBackup/`;
const redirectStep = '15'

const isCorrectRedirectUri = (setting) => setting === redirectUri;

const getRedirectUriFeedback = (setting) => {
    const linkText =
        `<a target="_blank" href="https://github.com/jneilliii/OctoPrint-GoogleDriveBackup#create-a-google-oauth-app">step ${15}</a>.`;
    if (setting) {
        if (!setting.startsWith(redirectHost)) {
            return `Please use the host '${redirectHost}' for Authorized Redirect URI as specified in ${linkText}`;
        } else if (!setting.endsWith("/")) {
            return `Make sure the Authorized Redirect URI ends with a trailing slash as specified in ${linkText}`;
        }
    }
    return `Missing Authorized Redirect URI "${redirectUri}" in ${linkText}`;
};

$(function() {
    function GoogledrivebackupViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        self.settingsViewModel = parameters[0];
        self.cert_saved = ko.observable(false);
        self.cert_authorized = ko.observable(false);
        self.authorizing = ko.observable(false);
        self.cert_file_name = ko.observable('');
        self.cert_file_data = undefined;
        self.auth_code = ko.observable('');
        self.auth_url = ko.observable('#');
        self.client_secret_alert = ko.observable('');

        var certFileuploadOptions = {
            dataType: "json",
            maxNumberOfFiles: 1,
            autoUpload: false,
            headers: OctoPrint.getRequestHeaders(),
            add: function(e, data) {
                if (data.files.length === 0) {
                    // no files? ignore
                    return false;
                }

                self.cert_file_name(data.files[0].name);
                self.cert_file_data = data;
            },
            done: function(e, data) {
                self.cert_file_name(undefined);
                self.cert_file_data = undefined;
            }
        };

        $("#googledrivebackup_cert_file").fileupload(certFileuploadOptions);

        $("#googledrivebackup_cert_file").change(() => {
            // Change in file selection, so we don't know if invalid or not yet
            self.client_secret_alert('');
        });

        self.onBeforeBinding = function() {
			self.cert_saved(self.settingsViewModel.settings.plugins.googledrivebackup.cert_saved());
			self.cert_authorized(self.settingsViewModel.settings.plugins.googledrivebackup.cert_authorized());
		};

        self.uploadCertFile = function(){
            if (self.cert_file_data === undefined) return;
            self.authorizing(true);
            var input, file, fr;

            if (typeof window.FileReader !== 'function') {
              alert("The file API isn't supported on this browser yet.");
              self.authorizing(false);
              return;
            }

            file = self.cert_file_data.files[0];
            fr = new FileReader();
            fr.onload = receivedText;
            fr.readAsText(file);

            function receivedText(e) {
                let lines = e.target.result;
                var json_data = JSON.parse(lines);
				if (!json_data.hasOwnProperty("web")) {
					self.client_secret_alert('Incorrect oAuth Credential type selected in <a target="_blank" href="https://github.com/jneilliii/OctoPrint-GoogleDriveBackup#create-a-google-oauth-app">step 13</a>.');
                    self.authorizing(false);
                    return
				} else if(!isCorrectRedirectUri(json_data["web"]["redirect_uris"][0])) {
                    self.client_secret_alert(getRedirectUriFeedback(json_data["web"]["redirect_uris"][0]));
                    self.authorizing(false);
                    return
                } else {
                    self.client_secret_alert('');
                }
                $.ajax({
                    url: API_BASEURL + "plugin/googledrivebackup",
                    type: "POST",
                    dataType: "json",
                    data: JSON.stringify({command: "gen_secret", json_data: json_data}),
                    contentType: "application/json; charset=UTF-8"
                }).done(function(data){
                    if(data.cert_saved){
                        self.cert_saved(true);
                        self.auth_url(data.url);
                        self.authorizing(false);
                    }
                }).fail(function(data){
                    console.log("error uploading cert file");
                    self.authorizing(false);
                });
            }
        };

        self.authorizeCertFile = function(){
            if(self.auth_code() === '') return;
            self.authorizing(true);
            $.ajax({
                url: API_BASEURL + "plugin/googledrivebackup",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({command: "authorize", auth_code: self.auth_code()}),
                contentType: "application/json; charset=UTF-8"
            }).done(function(data){
                if(data.authorized){
                    self.cert_authorized(true);
                    self.authorizing(false);
                }
            }).fail(function(data){
                console.log("error authorizing");
                self.cert_authorized(false);
                self.authorizing(false);
            });
        };

        self.deleteCertFiles = function(){
            self.cert_saved(false);
			self.cert_authorized(false);
        };

        self.onDataUpdaterPluginMessage = function (plugin, data) {
            if (plugin !== "googledrivebackup") {
                return;
            }

            if (data.error) {
                new PNotify({
					title: 'Google Drive Backup Error',
					text: '<div class="row-fluid"><p>There was an error.</p></div><p><pre style="padding-top: 5px;">'+data.error+'</pre></p>',
					hide: false,
                    type: 'error'
				});
            }
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: GoogledrivebackupViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ "settingsViewModel" ],
        // Elements to bind to, e.g. #settings_plugin_googledrivebackup, #tab_plugin_googledrivebackup, ...
        elements: [ "#settings_plugin_googledrivebackup" ]
    });
});
