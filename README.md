# Google Drive Backup

This plugin will automatically upload a backup upon completion to your authorized Google Drive. In order for the plugin to work properly you will have to create a Google OAuth App to authorize access. To create your own Google OAuth app please follow the directions outlined in the Prerequisites section below.

## Prerequisites

### OctoPrint 1.5.0

If you are using a version of OctoPrint older than version 1.5.0 this plugin will not work.

### Python

Due to upstream dependencies this plugin has been updated to only work in Python 3. You can either flash OctoPi 0.18 which ships with Python 3 standard or use the upgrade instructions [here](https://github.com/cp2004/Octoprint-Upgrade-To-Py3) to upgrade your instance.

### Create a Google OAuth App

1. Login to the [Google Developers Console](https://cloud.google.com/console)   


   ![screenshot](.gitbook/assets/settings_step1.png)

2. Create a new project giving it a name of your choice.   


   ![screenshot](.gitbook/assets/settings_step2.png)

3. In the sidebar on the left \(via ![screenshot](.gitbook/assets/settings_menu%20%281%29.png)\), select **APIs and Services** &gt; **Dashboard** then at the top of the page click the button to `Enable APIS and Services`.   


   ![screenshot](.gitbook/assets/settings_step3.png)

4. Enter drive in the search box at the top of the page and click `Google Drive API`.   


   ![screenshot](.gitbook/assets/settings_step4.png)

5. Click the `Enable` button to allow our app to use the Google Drive API.   


   ![screenshot](.gitbook/assets/settings_step5.png)

6. In the sidebar on the left, select **APIS and Services** &gt; **Credentials**   


   ![screenshot](.gitbook/assets/settings_step6.png)

7. Click `CONFIGURE CONSENT SCREEN` button at the top of the page.   


   ![screenshot](.gitbook/assets/settings_step7.png)

8. Select the `External` user type if you do not use Google G Suite, otherwise you can select `Internal` and click `Create`.   


   ![screenshot](.gitbook/assets/settings_step8.png)

9. If you don't publish your app you need to add the user email that you will be using to access Google Drive as a Test User.   


   ![screenshot](.gitbook/assets/settings_step8b.png)

10. Click `Save and Continue` on the remaining pages for your consent screen, and then click `Back to Dashboard`.   


    ![screenshot](.gitbook/assets/settings_step9.png)

11. In the sidebar on the left \(via ![screenshot](.gitbook/assets/settings_menu.png)\), select **APIs and Services** &gt; **Credentials** again.   


    ![screenshot](.gitbook/assets/settings_step10.png)

12. Click on `Create credentials` and select `OAuth client ID`.   


    ![screenshot](.gitbook/assets/settings_step11.png)

13. Select `Desktop App` for application type and then enter a name \(can be anything and does not really matter\) and then click `Create`.   


    ![screenshot](.gitbook/assets/settings_step12.png)

14. Click `OK` to the confirmation page and then use the download button ![screenshot](.gitbook/assets/settings_download.png) to save your client\_secrets\#\#\#\#\#.json file.   


    ![screenshot](.gitbook/assets/settings_step13.png)

15. Use the downloaded client\_secrets\#\#\#\#\#.json file to upload into the plugin’s settings to authorize its access to your Google Drive as described in the Configuration section below.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html) or manually using this URL:

```text
https://github.com/jneilliii/OctoPrint-GoogleDriveBackup/archive/master.zip
```

## Configuration

Once the Prerequisite steps above have been completed and you have downloaded your client\_secrets.json file follow these steps to authorize the plugin to your newly created app.

1. Open OctoPrint's settings from the System menu at the top of the page and select `Google Drive Backup` in the left-hand navigation menu.   


   ![screenshot](.gitbook/assets/configuration_step1.png)

2. Use the `Browse` button to select your downloaded client\_secrets\#\#\#\#\#.json file and press the `Upload` button.   


   ![screenshot](.gitbook/assets/configuration_step2.png)

3. An authentication URL will be generated and presented to you. Click that new URL to open a new window and authorize your custom Google app.   


   ![screenshot](.gitbook/assets/configuration_step3.png)

4. Log in to your Google account you want to give Drive access to. You will get a warning that the App isn't verified. This is normal as you have not submitted your custom app for verification by Google. You can choose to do that if you want but is not necessary for the operation of the plugin. Click the `Advanced` link at the bottom of the page and the click `Go to <app name>`.   


   ![screenshot](.gitbook/assets/configuration_step4.png)

5. Click the `Allow` button to retrieve your authentication code to enter in the plugin's settings in the next step.   


   ![screenshot](.gitbook/assets/configuration_step5.png)

6. Copy the code from step 5 and paste it into the **Auth Code** field and click `Authorize`.   


   ![screenshot](.gitbook/assets/configuration_step6.png)

7. If everything went well then you will be presented with a successful message.   


   ![screenshot](.gitbook/assets/configuration_step7.png)

## To-Do

* \[X\] ~~Improve documentation.~~
* [ ] Add route hook to allow for local redirect URIs during authentication.
* [ ] Delete certs instead of just clearing flags to start over.
* [ ] Improve error handling, display messages in UI.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker by clicking issues above.

## Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

## Sponsors

* Andreas Lindermayr
* [@Mearman](https://github.com/Mearman)
* [@TxBillbr](https://github.com/TxBillbr)
* Gerald Dachs
* [@TheTuxKeeper](https://github.com/thetuxkeeper)
* @tideline3d
* [SimplyPrint](https://simplyprint.dk/)
* [Andrew Beeman](https://github.com/Kiendeleo)
* [Calanish](https://github.com/calanish)
* [Will O](https://github.com/4wrxb)

## Support My Efforts

I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](.gitbook/assets/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](.gitbook/assets/paypal-with-text.png)](https://paypal.me/jneilliii)

No paypal.me? Send funds via PayPal to jneilliii@gmail.com

You can use [this](https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=jneilliii@gmail.com) link too. But the normal PayPal fee will be deducted. &lt;/small&gt;

