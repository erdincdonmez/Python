import keyboard

def on_key_event(event):
    # if event.name == 'up' or event.name == 'down' or event.name == 'left' or event.name == 'right':
        print(f"Girilen yön tuşu: {event.name}")

keyboard.on_release(on_key_event)

keyboard.wait('esc')  # Programın çalışmasını sonlandırmak için "esc" tuşuna basın