from twython import Twython
import csv

CONSUMER_KEY = 'EzAaie69a45LtuqMlWU4IMbTD'
CONSUMER_SECRET = '9UquCIwwKqaqKAtWlliQbd7p5a8mGwPKlQ1LFlZRqV8hx2TmGI'
ACCESS_TOKEN = '839155832155701248-ZuYNTxlQQGfUMwuVQey48vC0logs1ku'
ACCESS_TOKEN_SECRET = 'WN4kIzIUrYu8ueURgNJ1py7l8p9fkZvut2cGRQRIdQ3WR'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='Trump', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['Trump', result['text'].encode('utf-8'), url]]
        a.writerows((text))
