
from tkinter.messagebox import showinfo
import cv2
import tkinter as tk
from tkinter import filedialog as fd

def select_video():

    filetypes = (
        ("Video file", "*mov *mp4 *avi"),
        ("All files", "*.")
    )

    path = fd.askopenfilename(
       title="Sélectionnez un fichier",
       initialdir = "/" ,
       filetypes = filetypes)

    return path


def open_video(path):

    if not path:
        return None

    video = cv2.VideoCapture(path)

    if (video.isOpened()):
        print("Video ouverte avec succès")
    else:
        print("Erreur lors de l'ouverture de la vidéo")
        return None

    fps, frame_count, height, width = get_video_info(video)

    video_error = video_validate(fps, frame_count, height, width)

    if video_error is not None:
         print(video_error)
         video.release()
         return None
  

    return video

def get_video_info(video):

    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))

    return fps, frame_count, height, width



def video_validate(fps, frame_count, height, width):

    if fps < 120:
        return "La fréquence d'images (fps) est insuffisante"

    if height < 720:
        return "La résolution de la vidéo est trop faible"

    if frame_count <= 0:
        return "La vidéo est trop courte"

    if width <= 0:
        return "Vidéo invalide" 

    return None






