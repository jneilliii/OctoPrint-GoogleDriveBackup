# Google Drive Backup

This plugin will automatically upload a backup upon completion to your authorized Google Drive. In order for the plugin to work properly you will to create a Google Developer app to authorize access. To create your own Google app please follow the directions outlined in the Prerequisite section below.

## Prerequisite

1.	Go to the Google Developers Console
![screenshot](screenshots/settings_step1.png)
2.	Create a new project giving it a name of your choice.
![screenshot](screenshots/settings_step2.png)
3.	In the sidebar on the left (via ![screenshot](screenshots/settings_menu.png)), select APIs and Services > Dashboard, at the top click the button to Enable APIS and Services.
![screenshot](screenshots/settings_step3.png)
4.	Enter drive in the search box at the top of the page and click Google Drive API.
![screenshot](screenshots/settings_step4.png)
5.	Click the Enable button to allow our app to use the Google Drive API.
![screenshot](screenshots/settings_step5.png)
6.	In the sidebar on the left, select APIS and Services > Credentials
![screenshot](screenshots/settings_step6.png)
7.	Click CONFIGURE CONSENT SCREEN button at the top of the page.
![screenshot](screenshots/settings_step7.png)
8.	Select the 'External' user type if you do not use Google G Suite, otherwise you can select 'Internal'.
![screenshot](screenshots/settings_step8.png)
9.	Click Save and Continue on the remaining pages for your consent screen, and then click Back to Dashboard.
![screenshot](screenshots/settings_step9.png)
10.	In the sidebar on the left (via ![screenshot](screenshots/settings_menu.png)), select APIs and Services > Credentials again.
![screenshot](screenshots/settings_step10.png)
11.	Click on Create credentials -> OAuth client ID.
![screenshot](screenshots/settings_step11.png)
12.	Select Web Application and then enter a name (can be anything and does not really matter) and then click Create.
![screenshot](screenshots/settings_step12.png)
13.	Click OK to the confirmation page and then use the download button ![screenshot](screenshots/settings_download.png) to save your client_secrets.json file.
![screenshot](screenshots/settings_step13.png)
14.	Use the downloaded client_secrets#####.json file to upload into the plugin’s settings to authorize its access to your Google Drive as described in the Configuration section below.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/jneilliii/OctoPrint-GoogleDriveBackup/archive/master.zip

## Configuration

Once the Prerequisite steps above have been completed and you have downloaded your client_secrets.json file follow these steps to authorize the plugin to your newly created app.

1. Open OctoPrint's settings from the System menu at the top of the page and select Google Drive Backup in the left-hand navigation menu.
![screenshot](screenshots/configuration_step1.png)
2. Use the Browse button to select your downloaded client_secrets.json file and press the Upload button.
![screenshot](screenshots/configuration_step2.png)
3. An authentication URL will be generated and presented to you. Click that new URL to open a new window and authorize your custom Google app.
![screenshot](screenshots/configuration_step3.png)
4. Log in to your Google account you want to give Drive access to.
![screenshot](screenshots/configuration_step4.png)






