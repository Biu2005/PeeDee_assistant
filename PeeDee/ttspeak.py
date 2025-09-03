from gtts import gTTS
import pygame
import os
def text_to_speak(text):
    tts = gTTS(text=text, lang='vi')
    file_path = "sound.mp3"
    tts.save(file_path)

    # Sử dụng pygame để phát âm thanh
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Đợi cho đến khi phát xong
    while pygame.mixer.music.get_busy():
        continue
    
    # Xóa tệp sau khi phát
    pygame.mixer.music.unload()
    os.remove(file_path)