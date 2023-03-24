from zipfile import ZipFile

file = "files\ING_U01_dialogo_-_Audios_frases.zip" #file path

with ZipFile(file, 'r') as zip:
    zip.printdir()
    print('Processing...')
    zip.extractall()
    print('Process completed!')