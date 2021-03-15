import click
from plyer import notification
import time

@click.command()
@click.option('-t2150', is_flag=True)
@click.option('-t2200', is_flag=True)
@click.option('-timeout', type=int, default=5)
@click.option('-title', type=str, default='(non title)')
@click.option('-msg', type=str, default='(no message)')
def cli(t2150, t2200, timeout, title, msg):
    mynotify(t2150, t2200, timeout, title, msg)

def notify_2150(timeout=60):
    notification.notify(
        title = "<<!!! PC終了予告 !!!>>",
        message = "生活リズムを安定化させるために、22:00にはPC作業を終了しましょう",
        timeout = timeout
    )

def notify_2200(timeout=60):
    notification.notify(
        title = "<<!!! PC終了勧告 !!!>>",
        message = "22:00です。10分後にPCは強制終了します。\n作業を終了してください。",
        timeout = timeout
    )

def notify_msg(title="", msg="", timeout=60):
    notification.notify(
        title = title,
        message = msg,
        timeout = timeout
    )

def mynotify(t2150=False, t2200=False, timeout=10, title='(no title)', msg='(no message)'):

    if t2150:
        notify_2150(timeout=timeout)
    elif t2200:
        notify_2200(timeout=timeout)
    else:
        notify_msg(title=title, msg=msg, timeout=timeout)
