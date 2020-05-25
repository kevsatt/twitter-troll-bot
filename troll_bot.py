import tweepy
import spacy
from twilio.rest import Client


def send_text(message):
    """ sends me a text message whenever a tweet is sent or an error occurs """
    twilio_cli = Client(twilio_account_sid, twilio_auth_token)
    twilio_cli.messages.create(body=f'{message}', from_=twilio_number, to=cell_number)
    print('Text sent.')
    return 'Text sent.'


def from_creator(status):
    """ check if the creator of the tweet is the original creator. This is to prevent an endless loop of replies.
    The bot would reply to itself without this check too. """
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True


def initiate_twitter_stream(twitter_id):
    try:
        print('Stream has started')
        stream.filter(follow=[twitter_id])
    except Exception as e:
        message = f'Tweet stream stopped. Exception: {e}'
        send_text(message)
    finally:
        print('Stream disconnecting.')
        stream.disconnect()


class MyStreamListener(tweepy.StreamListener):
    """ Stream listener class that overrides tweepy's streamlistener so that we can make it call functions when it
    receives data. """

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, current_tweet):
        """ upon the user tweeting, this function will run and find the subject of the tweet and reply with {subject}
        is for squares! What a zinger. spicy. """
        if from_creator(current_tweet):
            # filter to make the subject not be any of these words
            filter_ = ['I', 'i', 'it', ' IT', 'It']
            doc = nlp(current_tweet.text)
            subjects = [chunk.text.upper() for chunk in doc.noun_chunks if chunk.text not in filter_]

            # have a blanket best subject be 'YOU' in the case that the subject returns empty due to the filter
            best_subject = 'YOU'
            max_len_subject = -1
            for subject in subjects:
                if '@' not in subject:
                    if len(subject) > max_len_subject:
                        max_len_subject = len(subject)
                        best_subject = subject

            # reply is sent here
            tweet_to_send = f'@{current_tweet.user.screen_name} {best_subject} is for squares!'
            api.update_status(tweet_to_send,
                              in_reply_to_status_id=current_tweet.id)
            message = f'NutsOnChinbot tweeted: {tweet_to_send}'
            print(message)
            send_text(message)
            return message
        else:
            pass

    def on_error(self, status):
        """ records whenever an error occurs then calls send_text function to send me a text message """
        message = f'Error detected on NutsOnChinBot: {status}'
        print(message)
        send_text(message)
        return message


# Create a Twitter developer account and enter your credentials here. You will need to apply for an account
CONSUMER_KEY = YOUR_API_KEY
CONSUMER_SECRET = YOUR_API_SECRET
ACCESS_KEY = YOUR_ACCESS_TOKEN
ACCESS_SECRET = YOUR_ACCESS_SECRET

# Enter your Twilio credentials here to get text notifications when the bot starts watching for tweets,
# replies, or has an error. Number example: +19999999999
twilio_account_sid = YOUR_TWILIO_ACCOUNT_SID
twilio_auth_token = YOUR_TWILIO_AUTH_TOKEN
twilio_number = YOUR_TWILIO_NUMBER
cell_number = YOUR_CELL_NUMBER

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
nlp = spacy.load('en_core_web_sm')

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)

# use https://tweeterid.com/ to find twitter id of user you want to trololol. Example Twitter ID is @realDonaldTrump's
twitter_id_to_troll = '25073877'

initiate_twitter_stream()
