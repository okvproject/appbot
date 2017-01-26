import dropbox
from config import dropb_token

dropb_app_key = '8ey1xdtbzrhjc3m'
dropb_app_secret = '7i5tvpifn9whf84'


client = dropbox.client.DropboxClient(dropb_token)

def upload():
    f = open('inf.xlsx', 'rb')
    client.file_delete('/active_inf.xlsx')
    client.put_file('/active_inf.xlsx', f)

