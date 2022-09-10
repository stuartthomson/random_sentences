import tweepy

def one_time_auth():
    """
    Followed: https://docs.tweepy.org/en/latest/auth_tutorial.html
    """
    with open('./api_key.txt', 'r') as keyfile, open('./api_secret_key.txt', 'r') as secret_file:
        consumer_key = keyfile.read().strip()
        consumer_secret = secret_file.read().strip()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    try:
        redirect_url = auth.get_authorization_url()
        print(redirect_url)
    except tweepy.TweepError:
        print('Error! Failed to get request token.')

    # session.set('request_token', auth.request_token['oauth_token'])

    token = auth.request_token['oauth_token']

    verifier = input('Verifier:')

    # token = session.get('request_token')
    # session.delete('request_token')
    auth.request_token = { 'oauth_token' : token,
                            'oauth_token_secret' : verifier }

    try:
        print(auth.get_access_token(verifier))
    except tweepy.TweepError as err:
        print('Error! Failed to get access token.')
        print(err)

def tweet(sentence: str):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(KEY, SECRET)
    api = tweepy.API(auth)
    api.update_status(sentence)
