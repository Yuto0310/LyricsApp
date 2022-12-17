import subprocess
def getInfo():
    nameOfTrack = subprocess.run(['osascript', '-e', 'tell application "Spotify" to get name of current track'], capture_output=True, text=True).stdout
    artistOfTrack = subprocess.run(['osascript', '-e', 'tell application "Spotify" to get artist of current track'], capture_output=True, text=True).stdout
    return (nameOfTrack, artistOfTrack)

def confirmRunning():
    runningBool = subprocess.run(['osascript', '-e', 'if application "Spotify" is running then return true'], capture_output=True,
                   text=True).stdout
    if runningBool == 'true\n':
        return True
    else:
        return False
