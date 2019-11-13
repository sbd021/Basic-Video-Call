import urllib2
import os
import shutil
import zipfile
import glob

RTC_SDK_URL="https://download.agora.io/sdk/release/Agora_Native_SDK_for_Windows(x86)_v2_9_1_FULL.zip?_ga=2.60902700.1683485253.1573617292-1291089117.1523340730"
print (RTC_SDK_URL)

def download(url, dest_file):
    username = "agoratest"
    password = "bestvoip"

    print("Start downloading %s ..." % url)
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    data = f.read()
    with open(dest_file, "wb") as code:
        code.write(data)
    print("Download finished. File path is: %s" % dest_file)

if RTC_SDK_URL == '0':
    pass
else:
    product_path = './products_sdk'
    if os.path.exists(product_path):
        shutil.rmtree(product_path)
    if os.path.exists('./sdk'):
        shutil.rmtree('./sdk')
    download(RTC_SDK_URL,'RTC_SDK.zip')
    zf = zipfile.ZipFile('./RTC_SDK.zip','r')
    zf.extractall('./products_sdk/tmp')
    shutil.copytree(glob.glob('./products_sdk/tmp/Agora*')[0] + '/sdk', './sdk')