names = list()
while(name:=input("enter name for shoutout: "))!="quit":
    names.append(name)

import win32com.client as a
speaker = a.Dispatch("SAPI.SpVoice")
for name in names:
    speaker.speak(f"shoutout to {name}")

