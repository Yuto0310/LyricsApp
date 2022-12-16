import subprocess
def getInfo():
    nameOfTrack = subprocess.run(['osascript', '-e', 'tell application "Spotify" to get name of current track'], capture_output=True, text=True).stdout
    artistOfTrack = subprocess.run(['osascript', '-e', 'tell application "Spotify" to get artist of current track'], capture_output=True, text=True).stdout
    return (nameOfTrack, artistOfTrack)
