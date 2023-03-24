import math
import speedtest

def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mbps"


wifi = speedtest.Speedtest()

print('Getting download speed...')
download_speed = wifi.download()
print('Getting upload speed...')
upload_speed = wifi.upload()

print('Download:', bytes_to_mb(download_speed))
print('Upload:', bytes_to_mb(upload_speed))