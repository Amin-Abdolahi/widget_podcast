import threading
import vlc
import time
import os

def get_file():
    """Get file path or URL from user input with a default test stream"""
    test_url = "https://n0f.radiojar.com/cp13r2cpn3quv?rj-ttl=5"
    file_address = input("Enter file path/stream URL: ")
    return file_address if file_address else test_url

def show_title(player, file_address):
    """Display the playing media's title or filename"""
    if os.path.exists(file_address):
        # For local files
        print(f"Now playing: {os.path.basename(file_address)}")
    else:
        # For online streams
        media = player.get_media()
        media.parse()  # Parse metadata
        time.sleep(2)  # Wait for metadata to load
        title = media.get_meta(vlc.Meta.Title)
        print(f"Now playing: {title}" if title else "Online stream (no title available)")


def stop_after(timer, player):
    time.sleep(timer)
    player.stop()
    print("Sleep timer: Playback stopped.")


if __name__ == "__main__":
    file_address = get_file()
    try:
        player = vlc.MediaPlayer(file_address)
        print("Connecting... (please wait 3 seconds)")
        time.sleep(3)
        player.play()
        print("Playback started.")
        show_title(player, file_address)
    except Exception as e:
        print(f"Error occurred: {e}")

while True:
    command = input(f"\n\n1- Stop\n2- Refresh\n3- Volume\n4- Sleep timer\n5- Skip\nYour choice: ")
    if command == "1":
        player.stop()
        print("Playback stopped.")
        break

    elif command == "2":
        player.stop()
        time.sleep(1)
        player.play()
        print("Playback restarted.")

    elif command == "3":
        volume = int(input("Enter a number between 1 - 100 for volume: "))
        if 0 <= volume <= 100 :
            player.audio_set_volume(volume)
            print(f"Volume set to {volume}")
        else:
            print("Invalid volume. Please enter a number between 1 and 100.")

    elif command == "4":
            timer = int(input("Enter time in minutes: ")) * 60
            threading.Thread(target=stop_after, args=(timer, player)).start()
            print(f"Sleep timer set for {timer//60} minutes.")

    elif command == "5":
        sec = int(input("Skip seconds (+/-): "))
        player.set_time(player.get_time() + sec * 1000)

    else:
        print("Invalid command. Try again.")
        continue
    