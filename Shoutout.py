import win32com.client as win
speaker = win.Dispatch("SAPI.SpVoice")
 
people = input("enter name")
speaker.Speak(f'Shoutout to {people}')