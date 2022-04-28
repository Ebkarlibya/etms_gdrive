## Etms Backup

Python Script to delete old files from specific Google Drive Folder

Setup:
- $ git clone https://github.com/Ebkarlibya/etms_gdrive
- $ cd etms_gdrive
- $ pip3 install -r requirements.txt

- open settings.yaml and set the following
- gdrive_folder_id 'some id' # the folder id which the script will work in
- trash_files_older_than_minutes 30 # files older than 30 minutes will be trashed
- python3 gdrive.py
- set cron job so the script work automatically once every day for example:
- $ crontab -e
- the following will run once every 6 hours, and set the correct path of etms_gdrive and python3
* */6 * * * cd /home/pop/Desktop/projects/gdrive-pg && /usr/bin/python3 gdrive.py



#### License

MIT