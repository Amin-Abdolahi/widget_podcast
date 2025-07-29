import vlc
import time
def get_file():
    test_url = "https://n0f.radiojar.com/cp13r2cpn3quv?rj-ttl=5"
    file_address = input("Enter file address or URL: ")
    if file_address == "":
        file_address = test_url
    return file_address

if __name__ == "__main__":
    file_address = get_file()

player = vlc.MediaPlayer(file_address)
player.play()

while True:
    command = input("\n1- Stop\n2- Refresh\n3- Volume\n4- Sleep timer\nYour choice: ")

    if command == "1":
        player.stop()
        break

    elif command == "2":
        player.play()

    elif command == "3":
        volume = int(input("Enter a number between 1 - 100 for volume: "))
        player.audio_set_volume(volume)

    elif command == "4":
        timer = int(input("Enter time in minutes: ")) * 60
        time.sleep(timer)
        player.stop()
        break

    else:
        print("Invalid command. Try again.")
        continue
    