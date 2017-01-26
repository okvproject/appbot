import dropbox

app_key = '8ey1xdtbzrhjc3m'
app_secret = '7i5tvpifn9whf84'

client = dropbox.client.DropboxClient('y7PKY1KUfqAAAAAAAAAAF4ETdvTcTfLf4iIolDSi-s7jOYlICsldj0k5y4w9hB7W')

def upload(file):
    f = open('working-draft.txt', 'rb')
    response = client.put_file('/magnum.txt', f)

