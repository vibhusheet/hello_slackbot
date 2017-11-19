"""
A hello slack chatbot
"""

# from modules import recievefunctions as recieve
from modules import infofunctions as info
from modules import sendfunctions as send


def main():
    """
    This is where everything is put together
    """
    channels = info.list_channels()
    if channels:
        for c in channels:
            if c['name'] == 'general':
                user_detail = info.list_users()
                for u_id, u_details in user_detail.items():
                    text = "Hello {}! Its 12:00 in tz - {}".format(u_details['name'], u_details['tz'])
                    send.add_scheduled_message(c['id'], u_details['tz'], text)
                    # send.send_message(c['id'], (text+" -- Test"))
        print("--------")
    else:
        print('Unable to authenticate')
    send.initiate_scheduler_thread()
    exec(open('./modules/recievefunctions.py').read())


if __name__ == '__main__':
    main()
