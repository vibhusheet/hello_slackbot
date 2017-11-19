import time
import os
import threading
import schedule
import arrow
from slackclient import SlackClient


slack_token = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(slack_token)


def send_message(channel_id, message):
    """
    Sends a message to a slack channel
    :channel_id
    :message
    """
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='scribetestbot',
        icon_emoji=':robot_face:'
        )


def add_scheduled_message(channel_id, timezone, text):
    """
    Schedules a text to be sent to a channel at 12:00 of that timezone
    :channel_id
    :timezone
    :text
    """
    foreign_time = arrow.get(tzinfo=timezone).replace(hour=12, minute=0, second=0, microsecond=0, tzinfo=timezone)
    local_time = foreign_time.to('Asia/Kolkata')
    local_time = local_time.format('H:mm')
    schedule.every().day.at(local_time).do(send_message, channel_id, text)
    log = "message scheduled - text '{}' at local-'{}'".format(text, local_time)
    print(log)


def run_job():
    """
    Runs the jobs in the Scheduler
    """
    while 1:
        schedule.run_pending()
        time.sleep(60)


def initiate_scheduler_thread():
    """
    A separate thread to run the jobs in the background
    """
    scheduler_thread = threading.Thread(target=run_job)
    scheduler_thread.daemon = True
    print("scheduler_thread_initiated")
    scheduler_thread.start()
    # scheduler_thread.run()


if __name__ == '__main__':
    print("hello from sendfunctions.py")
    add_scheduled_message('C7ZE7LV96', 'Europe/Berlin', 'hi its 12:00 at Europe/Berlin')
    run_job()
