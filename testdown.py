import os
import hashlib
from sentmail import mailsent
from downfiles import download_from_url
import login


if __name__ == '__main__':

    ac = login.logincair()

    url = "https://cair.cambricon.com/sharecloud-boot/file/tarball_download?id=NVp1OTU3MlI1TGlBNXB5ZkxuSndiUT09&editionId=78ed2ef67a612c34024883b154bf3367&accessToken=%s"%(ac)
    download_from_url(url, "国网一期.rpm")
    file_name = "国网一期.rpm"

    with open(file_name, 'rb') as fp:
        data = fp.read()
    file_sha1 = hashlib.sha1(data).hexdigest()
    # print(file_sha1)
    if file_sha1 == "9f6085daef6d106ac16f016b4995c7d68d211e92":
        print("文件下载正常")
        subjects = "文件下载正常"
        contents = "文件下载正常"
        os.remove(os.path.join(file_name))
        mailsent(subjects=subjects,contents=contents)
    else:
        print('文件下载不正常，sha1:%s' %file_sha1)
        subjects = "文件下载不正常"
        contents = "文件下载不正常"
        os.rename(file_name,file_sha1)
        mailsent(subjects=subjects,contents=contents)
