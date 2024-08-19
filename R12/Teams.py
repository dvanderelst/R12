import pymsteams
import socket

hook = 'https://mailuc.webhook.office.com/webhookb2/55adf49a-9297-4a28-8a9e-55fdb65c6f79@f5222e6c-5fc6-48eb-8f03-73db18203b63/IncomingWebhook/84fba3e337ba4e2db042b92c83c55f95/9ab44a34-692e-4b52-b075-fd492cb004aa'

def get_computer_name():
    try:
        hostname = socket.gethostname()
        return hostname
    except Exception as e:
        return f"An error occurred: {e}"


def send(body, title=''):
    title = str(title)
    computer = get_computer_name()
    if title == '': title = computer + ' says:'
    myTeamsMessage = pymsteams.connectorcard(hook)
    myTeamsMessage.title(title)
    myTeamsMessage.text(body)
    myTeamsMessage.send()
