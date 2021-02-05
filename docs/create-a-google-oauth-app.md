# Create a Google OAuth App

1. Login to the [Google Developers Console](https://cloud.google.com/console)   


   ![screenshot](.gitbook/assets/settings_step1.png)

2. Create a new project giving it a name of your choice.   


   ![screenshot](.gitbook/assets/settings_step2.png)

3. In the sidebar on the left \(via ![screenshot](.gitbook/assets/settings_menu.png)\), select **APIs and Services** &gt; **Dashboard** then at the top of the page click the button to `Enable APIS and Services`.   


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

14. Click `OK` to the confirmation page and then use the download button ![screenshot](screenshots/settings_download.png) to save your client\_secrets\#\#\#\#\#.json file.   


    ![screenshot](.gitbook/assets/settings_step13.png)

15. Use the downloaded client\_secrets\#\#\#\#\#.json file to upload into the plugin’s settings to authorize its access to your Google Drive as described in the Configuration section below.

