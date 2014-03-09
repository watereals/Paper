
import urllib2

def haokan(size):
    if( size < 4096 ):
        return 4, 'KB'
    elif(size > 1048576):
        return size/1048576+1, 'MB'
    else:
        return size/1024+1, 'KB'

def down_file(url, dir=None, file_name=None):
    print("Downloading file(URL): %s" % url)
    if not dir.endswith("/"):
        dir += "/"                          # if not, append a '/' to directory path
    if file_name==None:
        file_name = url.split('/')[-1]      # get filename from url
    saveName = dir+file_name                # set save file name
    
    try:
        webFile = urllib2.urlopen(url, None, 10)  # url, data(want to send to server) and timeout
    except urllib2.URLError as e:
        print("Download failed: %s" % e)
        return False
    
    out = open(saveName, 'wb')
    httpInfo = webFile.info()                   # get http header infomation
    print("Size of requested file: %s%s" % (haokan(int(httpInfo.getheaders("Content-Length")[0]))))
    while True:
        buffer = webFile.read(8192)
        if not buffer:
            break
        out.write(buffer)
    out.close()
    print("Download success.")
    return True
