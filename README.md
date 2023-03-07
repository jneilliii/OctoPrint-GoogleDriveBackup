# Google Drive Backup

This plugin will automatically upload a backup upon completion to your authorized Google Drive. In order for the plugin to work properly you will have to create a Google OAuth App to authorize access. To create your own Google OAuth app please follow the directions outlined in the Prerequisites section below.

## Prerequisites

### OctoPrint 1.5.0
If you are using a version of OctoPrint older than version 1.5.0, this plugin will not work.

### Dependencies
Due to upstream dependencies this plugin has been updated to only work in Python 3. You can either flash OctoPi 0.18 which ships with Python 3 standard or use the upgrade instructions [here](https://github.com/cp2004/Octoprint-Upgrade-To-Py3) to upgrade your instance.

You may also need to install some system dependencies, specifically if you manually installed OctoPrint and didn't use the OctoPi image. Known dependencies that have been reported are `Rust` and `libssl-dev`. Use the commands to below to install them.

```
sudo apt install rustc
sudo apt install libssl-dev
```

### Create a Google OAuth App
1.	Login to the [Google Developers Console](https://console.cloud.google.com/) <br>
![screenshot](screenshots/settings_step1.png)
2.	Create a new project giving it a name of your choice. <br>
![screenshot](screenshots/settings_step2.png)
3.	In the sidebar on the left (via ![screenshot](screenshots/settings_menu.png)), select **APIs and Services** > **Dashboard** then at the top of the page click the button to `Enable APIS and Services`. <br>
![screenshot](screenshots/settings_step3.png)
4.	Enter drive in the search box at the top of the page and click `Google Drive API`. <br>
![screenshot](screenshots/settings_step4.png)
5.	Click the `Enable` button to allow our app to use the Google Drive API. <br>
![screenshot](screenshots/settings_step5.png)
6.	In the sidebar on the left, select **APIS and Services** > **Credentials** <br>
![screenshot](screenshots/settings_step6.png)
7.	Click `CONFIGURE CONSENT SCREEN` button at the top of the page. <br>
![screenshot](screenshots/settings_step7.png)
8.	Select the `External` user type if you do not use Google G Suite, otherwise you can select `Internal` and click `Create`. <br>
![screenshot](screenshots/settings_step8.png)
9.	Add a user support email and developer contact email, then press `Save and Continue`. <br>
![screenshot](screenshots/settings_step9.png)
10.	No scopes are necessary. Click `Save and Continue`. <br>
![screenshot](screenshots/settings_step10.png)
11.	If you don't publish your app you need to add the user email that you will be using to access Google Drive as a Test User. After doing so, press `Save and Continue`. <br>
![screenshot](screenshots/settings_step11.png)
12.	Confirm all the information then click `Back to Dashboard`. <br>
![screenshot](screenshots/settings_step12.png)
13.	In the sidebar on the left (via ![screenshot](screenshots/settings_menu.png)), select **APIs and Services** > **Credentials** again. <br>
![screenshot](screenshots/settings_step13.png)
14.	Click on `Create credentials` and select `OAuth client ID`. <br>
![screenshot](screenshots/settings_step14.png)
15.	Select `Web application` for application type and then enter a name (can be anything and does not really matter). Fill in the Authorized redirect URIs as `https://jneilliii.github.io/OctoPrint-GoogleDriveBackup/` and then click `Create`. <br>
![screenshot](screenshots/settings_step15.png)
16.	In the dialog box that appears, click the download button ![screenshot](screenshots/settings_download.png) to save your client_secrets#####.json file then press `OK`. <br>
![screenshot](screenshots/settings_step16.png)
17.	Use the downloaded client_secrets#####.json file to upload into the plugin’s settings to authorize its access to your Google Drive as described in the Configuration section below.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/jneilliii/OctoPrint-GoogleDriveBackup/archive/master.zip

## Configuration
Once the Prerequisite steps above have been completed and you have downloaded your client_secrets.json file follow these steps to authorize the plugin to your newly created app.

1. Open OctoPrint's settings from the System menu at the top of the page and select `Google Drive Backup` in the left-hand navigation menu. <br>
![screenshot](screenshots/configuration_step1.png)
2. Use the `Browse` button to select your downloaded client_secrets#####.json file and press the `Upload` button. <br>
![screenshot](screenshots/configuration_step2.png)
3. An authentication URL will be generated and presented to you. Click that new URL to open a new window and authorize your custom Google app. <br>
![screenshot](screenshots/configuration_step3.png)
4. Log in to your Google account you want to give Drive access to. You will get a warning that the App isn't verified. This is normal as you have not submitted your custom app for verification by Google. You can choose to do that if you want but is not necessary for the operation of the plugin. Click the `Advanced` link at the bottom of the page and the click `Go to <app name>`. <br>
![screenshot](screenshots/configuration_step4.png)
5. Click the `Allow` button to retrieve your authentication code to enter in the plugin's settings in the next step. <br>
![screenshot](screenshots/configuration_step5.png)
6. Copy the code from step 5 and paste it into the **Auth Code** field and click `Authorize`. <br>
![screenshot](screenshots/configuration_step6.png)
7. If everything went well then you will be presented with a successful message. <br>
![screenshot](screenshots/configuration_step7.png)

## To-Do

- [X] ~~Improve documentation.~~
- [X] ~~Add custom upload folder.~~
- [ ] Add route hook to allow for local redirect URIs during authentication.
- [ ] Delete certs instead of just clearing flags to start over.
- [ ] Improve error handling, display messages in UI.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker by clicking issues above.

## Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

## Sponsors
- Andreas Lindermayr
- [@Mearman](https://github.com/Mearman)
- [@TheTuxKeeper](https://github.com/thetuxkeeper)
- [@tideline3d](https://github.com/tideline3d/)
- [OctoFarm](https://octofarm.net/)
- [SimplyPrint](https://simplyprint.dk/)
- [Andrew Beeman](https://github.com/Kiendeleo)
- [Calanish](https://github.com/calanish)
- [Lachlan Bell](https://lachy.io/)
- [Johnny Bergdal](https://github.com/bergdahl)
- [Leigh Johnson](https://github.com/leigh-johnson)
- [Stephen Berry](https://github.com/berrystephenw)
- [Guyot François](https://github.com/iFrostizz)
- [Steve Dougherty](https://github.com/Thynix)
- [Flying Buffalo Aerial Photography](http://flyingbuffalo.info/)
## Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](screenshots/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](screenshots/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com

You can use [this](https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=jneilliii@gmail.com) link too. But the normal PayPal fee will be deducted.
</small>







