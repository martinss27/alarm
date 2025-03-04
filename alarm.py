import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = r"C:\Users\leoal\Desktop\python_projects\alarm_project\my_music.mp3"


    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)


        if current_time == alarm_time:
            print("\nWAKE UP!")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # Espera a música terminar
                time.sleep(1)
            break 

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)