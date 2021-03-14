from plyer import notification
import sys
import argparse

import time

def notify_2150(in_timeout=60):
    notification.notify(
        title = "<<!!! PC終了予告 !!!>>",
        message = "生活リズムを安定化させるために、22:00にはPC作業を終了しましょう",
        timeout = in_timeout
    )

def notify_2200(in_timeout=60):
    notification.notify(
        title = "<<!!! PC終了勧告 !!!>>",
        message = "22:00です。10分後にPCは強制終了します。\n作業を終了してください。",
        timeout = in_timeout
    )

def notify_msg(in_title="", in_msg="", in_timeout=60):
    notification.notify(
        title = in_title,
        message = in_msg,
        timeout = in_timeout
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Windows Notify Program")
    parser.add_argument("-t2150", action="store_true", help="21:50 PC shutdown notice.")
    parser.add_argument("-t2200", action="store_true", help="22:00 PC shutdown notice.")
    parser.add_argument("-title", type=str, default="(no title)", help="Windows notification title.")
    parser.add_argument("-msg", type=str, default="(no message)", help="Windows notification message.")
    parser.add_argument("-timeout", type=int, default=30, help="Windows notification timeout.")

    args = parser.parse_args()

    #debug
    #print(f'SYSTEM PLATFORM: {sys.platform}')
    #time.sleep(10)

    if args.t2150:
        notify_2150(in_timeout=args.timeout)
    elif args.t2200:
        notify_2200(in_timeout=args.timeout)
    else:
        notify_msg(in_title=args.title, in_msg=args.msg, in_timeout=args.timeout)

    sys.exit(0)