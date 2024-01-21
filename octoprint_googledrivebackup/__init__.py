# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin


class GoogledrivebackupPlugin(octoprint.plugin.SettingsPlugin,
							  octoprint.plugin.AssetPlugin,
							  octoprint.plugin.TemplatePlugin,
							  octoprint.plugin.EventHandlerPlugin,
							  octoprint.plugin.SimpleApiPlugin):

	##~~ SettingsPlugin mixin

	def __init__(self):
		super().__init__()
		self.gauth = None

	def get_settings_defaults(self):
		return dict(
			cert_saved=False,
			cert_authorized=False,
			installed_version=self._plugin_version,
			strip_timestamp=False,
			upload_folder="",
		)

	##~~ SimpleApiPlugin mixin

	def get_api_commands(self):
		return dict(gen_secret=["json_data"], authorize=["auth_code"])

	def on_api_command(self, command, data):
		from octoprint.server import user_permission
		import flask
		if not user_permission.can():
			return flask.make_response("Insufficient rights", 403)

		from pydrive2.auth import GoogleAuth
		config_file = "{}/client_secrets.json".format(self.get_plugin_data_folder())
		credentials_file = "{}/credentials.json".format(self.get_plugin_data_folder())
		if not self.gauth:
			self.gauth = GoogleAuth()

		if command == "gen_secret":
			import json
			# write out our client_secrets.json file
			with open(config_file, "w") as f:
				f.write(json.dumps(data["json_data"]))
			self._settings.set(["cert_saved"], True)
			self._settings.save()

			self.gauth.LoadClientConfigFile(config_file)
			self.gauth.GetFlow()
			self.gauth.flow.params.update({'access_type': 'offline'})
			self.gauth.flow.params.update({'approval_prompt': 'force'})
			auth_url = self.gauth.GetAuthUrl()
			return flask.jsonify(dict(cert_saved=True, url=auth_url))

		if command == "authorize":
			self._logger.info("Attempting to authorize Google App")
			if not self.gauth:
				return flask.jsonify(dict(authorized=False))
			# Try to load saved client credentials
			self.gauth.Auth(data["auth_code"])
			self.gauth.SaveCredentialsFile(credentials_file)
			self._settings.set(["cert_authorized"], True)
			self._settings.save()
			return flask.jsonify(dict(authorized=True))

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/googledrivebackup.js"]
		)

	##~~ EventHandlerPlugin mixin

	def on_event(self, event, payload):
		if event == "plugin_backup_backup_created" and self._settings.get_boolean(["cert_authorized"]):
			self._logger.info("{} created, will now attempt to upload to Google Drive".format(payload["path"]))
			from pydrive2.drive import GoogleDrive
			from pydrive2.auth import GoogleAuth
			try:
				credentials_file = "{}/credentials.json".format(self.get_plugin_data_folder())
				folder_id = None
				gauth = GoogleAuth()
				gauth.LoadCredentialsFile(credentials_file)
				if gauth.credentials is None:
					self._logger.error("not authorized")
					self._settings.set(["cert_authorized"], False)
					self._settings.save()
					return
				elif gauth.access_token_expired:
					gauth.Refresh()
				else:
					gauth.Authorize()
				gauth.SaveCredentialsFile(credentials_file)
				drive = GoogleDrive(gauth)
				filename = payload["name"]
				if self._settings.get_boolean(["strip_timestamp"]):
					import re
					filename = re.sub(r"((-[0-9]+)+\.zip$)", ".zip", filename)
				if not self._settings.get(["upload_folder"]) == "":
					folder_id = self.create_remote_folder(drive, self._settings.get(["upload_folder"]))
				file_list = drive.ListFile({'q': f"title='{filename}' and trashed=false and '{folder_id or 'root'}' in parents"}).GetList()
				if len(file_list) == 1:
					f = file_list[0]
				else:
					file_metadata = {"title": filename}
					if folder_id:
						file_metadata["parents"] = [{"id": folder_id}]
					f = drive.CreateFile(file_metadata)
				f.SetContentFile(payload["path"])
				f.Upload()
				f = None
			except Exception as e:
				self._plugin_manager.send_plugin_message(self._identifier, {"error": str(e)})

	def create_remote_folder(self, drive, folder_name):
		last_id = None
		temp = folder_name.split("/")
		for item in temp:
			lookup = (drive.ListFile({'q': f"mimeType='application/vnd.google-apps.folder' and trashed=false and title='{item}' and '{last_id or 'root'}' in parents"}).GetList())

			if len(lookup) > 0:
				last_id = lookup[0]["id"]
			else:
				file_metadata = {
					"title": item,
					"mimeType": "application/vnd.google-apps.folder"
				}

				if last_id:
					file_metadata["parents"] = [{"id": last_id}]

				file0 = drive.CreateFile(file_metadata)
				file0.Upload()
				last_id = file0["id"]
		return last_id

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			googledrivebackup=dict(
				displayName="Google Drive Backup",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-GoogleDriveBackup",
				current=self._plugin_version,
				stable_branch=dict(
					name="Stable",
					branch="master",
					comittish=["master"]
				),
				prerelease_branches=[
					dict(
						name="Release Candidate",
						branch="rc",
						comittish=["rc", "master"]
					)
				],
				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-GoogleDriveBackup/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Google Drive Backup"
__plugin_pythoncompat__ = ">=3,<4"


def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = GoogledrivebackupPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
