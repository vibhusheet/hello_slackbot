## Outline
This is a hello slackbot

- we can schedule to send a message to each user in '#general' group at 12:00pm of the user's timezones

## how to test

### pre-requisites

1. setup env
    (use pipenv)

        # you can use these commands:
        python -m pip install pipenv
        # install dependencies:
        pipenv install
        # start the shell
        pipenv shell

2. ngrok
    use [ngrok](https://ngrok.com/docs) to host the webserver for receiving messages

        ./ngrok http 5000 # or which ever port flask is using
    copy the ngrok url as we will require it later. It should be something like 'https://f2867781.ngrok.io'

3. enviornment variables -
    go to the [Slack's legacy tokens](https://api.slack.com/custom-integrations/legacy-tokens) and copy the token for your workspace and 
    assign the variable in your env

        export SLACK_TOKEN='<legacy_token>'

    go to the [Slack Outgoing webhooks page](https://api.slack.com/outgoing-webhooks) and click on "outgoing webhook integration"
    select the channel as #general, paste the ngrok url here inside the URL field. Copy the token generated and assign that to a variable in your env

        export SLACK_WEBHOOK_SECRET = '<generated_outgoing_webhook_token>'

### run

run using - "python app.py"

You can set your timezone in your profile options and then run the program..
