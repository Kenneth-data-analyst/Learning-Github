# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from pytube import YouTube
import ffmpeg
import speech_recognition as sr

def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"Download progress: {percentage_of_completion:.2f}%")

# 下载YouTube视频并显示进度
yt = YouTube("https://www.youtube.com/watch?v=jk4YXh8SiN4&t=924s", on_progress_callback=progress_func)
stream = yt.streams.filter(only_audio=True).first()
stream.download(filename="video.mp4")

# 使用ffmpeg提取音频
input_video = "video.mp4"
output_audio = "audio.wav"
ffmpeg.input(input_video).output(output_audio).run()

# 语音识别
recognizer = sr.Recognizer()
audio_file = sr.AudioFile(output_audio)

with audio_file as source:
    audio_data = recognizer.record(source)

text = recognizer.recognize_google(audio_data)

# 保存文本到文件
with open("transcription.txt", "w") as file:
    file.write(text)
