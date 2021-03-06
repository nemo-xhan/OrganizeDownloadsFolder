#! python
# OrganizeDownload - Oraganize your download folder
import os


def moveFile(path, folderName, file):
    dst = os.path.join(path,folderName)
    if not(os.path.exists(dst)):
        os.mkdir(dst)
    try:
        os.rename(file, dst)
    except FileExistsError:
        fileName    = os.path.basename(file)
        name, ext   = os.path.splitext(fileName)
        name       += 'New'
        fileName    = name + ext
        dst         = os.path.join(dst, fileName)
        os.rename(file, dst)
        
    print(f'{file} --> {dst}')

Home = os.environ.get('HOMEPATH')
Downloads = os.path.join(Home, 'Downloads')


if not os.path.exists(Downloads):
    print('Sorry! for some reason script could not find your Download folder')
    exit(127)

os.chdir(Downloads)

pictures    = ('jpeg', 'jpg', 'png', 'gif')
vidoes      = ('mkv', 'avi', 'mp4', 'ts')
compressed  = ('zip', 'rar', '7z')
music       = ('mp3', 'wav')
document    = ('doc', 'xls', 'pdf', 'docx', 'txt')
programs    = ('exe', 'bat', 'msi')

for file in os.listdir():
    if os.path.isfile(file):
        file = os.path.realpath(file)
        path,fileName = os.path.split(file)
        if file.endswith(pictures):
            moveFile(path, 'Pictures', file)

        elif file.endswith(compressed):
            moveFile(path, 'Compressed', file)

        elif file.endswith(vidoes):
            moveFile(path, 'Vidoes', file)

        elif file.endswith(music):
            moveFile(path, 'Music', file)

        elif file.endswith(document):
            moveFile(path, 'Documents', file)

        elif file.endswith(programs):
            moveFile(path, 'Programs', file)

        else:
            moveFile(path, 'Others', file)
    