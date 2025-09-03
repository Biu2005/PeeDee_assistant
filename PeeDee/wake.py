import pyttsx3 as tts 
import speech_recognition as sr 
import ttspeak
import expression
import time
WAKE_WORD = "xin chào"
GREETING = "Hi,pi đi nghe nè"
def listen_for_wake_word():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        ttspeak.text_to_speak("Hệ thống đang chờ từ kích hoạt...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Điều chỉnh cho tiếng ồn xung quanh

        while True:
            try:
                print("Lắng nghe...")
               # ttspeak.text_to_speak("tôi đang lắng nghe")
                audio = recognizer.listen(source)

                text1 = recognizer.recognize_google(audio, language="vi-VN").lower()
                print(f"Bạn đã nói: {text1}")

                if WAKE_WORD in text1:
                    print("Từ kích hoạt được phát hiện!")
                    ttspeak.text_to_speak(GREETING)
                    expression.wakeup()
                    time.sleep(1)
                    break

            except sr.UnknownValueError:
                print("Không hiểu giọng nói, vui lòng thử lại.")
            except sr.RequestError as e:
                print(f"Lỗi kết nối đến dịch vụ nhận diện giọng nói: {e}")
                break
