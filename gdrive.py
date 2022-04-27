import os
from datetime import datetime
from dateutil.parser import parse
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()

# Try to load saved client credentials
# gauth.LoadCredentialsFile(os.path.join(os.path.abspath("."), "mycreds.txt"))
# gauth.LoadClientConfigFile(os.path.join(os.path.abspath("."), "client_secrets.json"))

if gauth.credentials is None:
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})

    gauth.LocalWebserverAuth()

elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt") 

drive = GoogleDrive(gauth)

settings = drive.auth.attr['settings']


def main():
    _id = settings['gdrive_folder_id']
    files = drive.ListFile({
        'q': f"'{_id}' in parents and trashed=false"
    }).GetList()

    for file in files:
        if (datetime.now() - parse(file["createdDate"]).replace(tzinfo=None)
            ).seconds / 60 > settings['trash_files_older_than']:
            drive.CreateFile({"id": file["id"]})
            file.Trash()
            print(f"delete: {file['title']}")

def get_folder_id(folder_name):
    files = drive.ListFile({
        'q': "'root' in parents and trashed=false"
    }).GetList()
    for file in files:
        if file['title'] == settings['gdrive_work_folder']:
            return file['id']
    return


if __name__ == "__main__":
    main()