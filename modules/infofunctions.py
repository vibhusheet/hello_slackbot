import os
from slackclient import SlackClient

slack_token = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(slack_token)


def list_channels():
    """
    Returns list of channels from the slack workspace
    """
    rv = None
    channels_call = slack_client.api_call("channels.list")
    if channels_call['ok']:
        rv = channels_call['channels']
    return rv


def channel_info(channel_id):
    """
    Returns the info of a particular channel
    :channel_id
    """
    rv = None
    info = slack_client.api_call("channels.info", channel=channel_id)
    if info['ok']:
        rv = info['channel']
    return rv


def list_users():
    """
    Returns a list of members from the slack workspace
    """
    rv = None
    users_call = slack_client.api_call("users.list")
    if users_call['ok']:
        rv = {}
        for m in users_call['members']:
            if m['name'] != 'slackbot':
                rv[m['id']] = {'name' : m['name'], 'tz' : m['tz'], 'tz_label' : m['tz_label'], 'tz_offset' : m['tz_offset'], 'is_bot' : m['is_bot']}
    return rv


def user_info(user_id):
    """
    Returns the info for a particular user
    :user_id
    """
    rv = None
    info = slack_client.api_call("users.info", user=user_id)
    if info['ok']:
        rv = info['user']
    return rv

if __name__ == '__main__':
    print("hello from infofunctions.py")
