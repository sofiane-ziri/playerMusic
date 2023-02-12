import os
import pygame
import tkinter as tk
from tkinter import filedialog, Frame, Button, Label, Entry, Scale
from PIL import Image

# Charger les images play, resume, stop, pause
play_img = Image.open("img/play.png")
resume_img = Image.open("img/resume.png")
stop_img = Image.open("img/stop.png")
pause_img = Image.open("img/pause.png")
next_img = Image.open("img/next.png")
previous_img = Image.open("img/previous.png")

imgs = [play_img, resume_img, stop_img, pause_img, next_img, previous_img ]
resized_imgs = []

# Redimensionner les images
for img in imgs:
    resized_img = img.resize((200, 100), Image.ANTIALIAS)
    resized_imgs.append(resized_img)

# Enregistrer les images redimensionnées
resized_imgs[0].save("resized_play.png")
resized_imgs[1].save("resized_resume.png")
resized_imgs[2].save("resized_stop.png")
resized_imgs[3].save("resized_pause.png")
resized_imgs[4].save("resized_next.png")
resized_imgs[5].save("resized_previous.png")

root = tk.Tk()
root.geometry("500x500")
root.configure(bg="#282828")
root.title("Spotify-like Music Player")


def play_music():
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def resume_music():
    pygame.mixer.music.unpause()


def stop_music():
    pygame.mixer.music.stop()


def set_volume(val):
    pygame.mixer.music.set_volume(float(val) / 100)

def previous_song():
    global current_song_index
    current_song_index -= 1
    if current_song_index < 0:
        current_song_index = len(songs) - 1
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

def next_song():
    global current_song_index
    current_song_index += 1
    if current_song_index == len(songs):
        current_song_index = 0
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()


music_folder = "music"
songs = [os.path.join(music_folder, song) for song in os.listdir(music_folder)]
current_song_index = 0

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(songs[current_song_index])
# Create control frame
control_frame = Frame(root, bg="#282828")
control_frame.pack(pady=20)

# Create previous button
previous_img = tk.PhotoImage(file="resized_previous.png")
previous_button = Button(control_frame, image=previous_img,
                     bg="#282828", command=previous_song)
previous_button.pack(side="left", padx=10)
# Create play button
play_img = tk.PhotoImage(file="resized_play.png")
play_button = Button(control_frame, image=play_img,
                     bg="#282828", command=play_music)
play_button.pack(side="left", padx=10)

# Create pause button
pause_img = tk.PhotoImage(file="resized_pause.png")
pause_button = Button(control_frame, image=pause_img,
                      bg="#282828", command=pause_music)
pause_button.pack(side="left", padx=10)

# Create resume button
resume_img = tk.PhotoImage(file="resized_resume.png")
resume_button = Button(control_frame, image=resume_img,
                       bg="#282828", command=resume_music)
resume_button.pack(side="left", padx=10)

# Create stop button
stop_img = tk.PhotoImage(file="resized_stop.png")
stop_button = Button(control_frame, image=stop_img,
                     bg="#282828", command=stop_music)
stop_button.pack(side="left", padx=10)


# Create next button
next_img = tk.PhotoImage(file="resized_next.png")
next_button = Button(control_frame, image=next_img,
                     bg="#282828", command=next_song)
next_button.pack(side="left", padx=10)


# Create volume scale
volume_frame = Frame(root, bg="#282828")
volume_frame.pack(pady=20)

volume_label = Label(volume_frame, text="Volume", bg="#282828", fg="white")
volume_label.pack(side="left")

volume_scale = Scale(volume_frame, from_=0, to=100, orient="horizontal",
                     command=set_volume, bg="#282828", fg="white")
volume_scale.set(50)
volume_scale.pack(side="left")


root.mainloop()



