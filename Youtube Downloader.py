from pytube import YouTube

link = input('Enter the video link: ')    
print('Connecting...')

try:
    yt = YouTube(link)
    title = yt.title
except:
    print('Connection Error!')

save_path = input('Enter the path to download: ')

print('Downloading ' + title + "...")
stream = yt.streams.first()
stream.download(save_path)
print('Download complete')