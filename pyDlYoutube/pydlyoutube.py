import os

from pydltyoutubehelper import *

try:
    import PySimpleGUI as sg
except ImportError as __ex:
    print("Install PySimpleGUI. Exception:", str(__ex))
    exit(1)




def mainWindow():
    layout = [
        [sg.Text("Youtube URL:"), sg.InputText(default_text=getClipboardText(), size=(64,1), key="URL"),
         sg.Button("Paste Link", key="PASTEURL")],
        [sg.Text("Download Path:"), sg.InputText(default_text=getDesktopPath(), size=(64,1), key="DPATH"),
         sg.Button("Select Directory", key="SELECTDPATH")],
        [sg.Checkbox("Download and Embed Subtitle", default=True, key="EMBEDSRT")],
        [sg.Checkbox("Download Audio MP3", default=False, key="MP3"),
         sg.Checkbox("Download Audio MP4", default=True, key="MP4")],
        [sg.Button("Download", key="DOWNLOAD"), sg.Button("Update", key="UPDATE"), sg.Button("Exit", key="EXIT")]
    ]

    w = sg.Window(title="youtube-dl GUI",
                  layout=layout,
                  size=(700, 180))

    while True:
        event, values = w.read()

        if event == sg.WINDOW_CLOSED or event == "EXIT":
            print("DONE")
            break
        elif event == "UPDATE":
            print("Starting UPDATE...")
            execyoutubedl(["-U"])
            print("UPDATE completed.")
        elif event == "PASTEURL":
            w["URL"].update(value=getClipboardText())
        elif event == "SELECTDPATH":
            w["DPATH"].update(value = getDirName())
        elif event == "DOWNLOAD":
            url = values["URL"]
            path = values["DPATH"]

            args = list()
            if values["MP3"]:
                args.append("-f")
                args.append("bestaudio")
                args.append("-x")
                args.append("--audio-quality")
                args.append("0")
                args.append("--audio-format")
                args.append("mp3")
            if values["MP4"]:
                args.append("--recode-video")
                args.append("mp4")
            if values["EMBEDSRT"]:
                args.append("--write-sub")
                args.append("--embed-subs")

            args.append(url)

            currentpath = os.getcwd()
            os.chdir(path)
            execyoutubedl(args)
            os.chdir(currentpath)



    w.close()




def main():
    mainWindow()

   # print(getUserProfile())
   # print(getDesktopPath())
   # print(getCurrentPath())
   # os.chdir(getDesktopPath())
   #execyoutubedl([
   #                getClipboardText()])


if __name__ == "__main__":
    main()