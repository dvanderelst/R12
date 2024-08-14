import socket
from pyBat.pushbullet import Pushbullet
ACCESS_TOKEN = 'o.2UJD0Zltzw8gdtWP0zNDxSRAvtjUBba9'

def get_computer_name():
    try:
        hostname = socket.gethostname()
        return hostname
    except Exception as e:
        return f"An error occurred: {e}"


def send(body='', title=''):
    computer = get_computer_name()
    pb = Pushbullet(ACCESS_TOKEN)
    title = str(title)
    if title == '': title = computer + ' says:'
    push = pb.push_note(title, body)
    return push


