# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.

import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PHRASES = ['fake news', 'maga', 'mainstream media', 'mexico',
           'obama', 'russia', 'trump', 'wall']

tweets = []
for year in range(2009, 2019):
    with open(f'master_{year}.json') as f:
        tweets.extend(json.load(f))
total = len(tweets)
print('total tweets:', total)


def message(tweet):
    return tweet.get('full_text') or tweet.get('text') or ''

messages = [message(t).lower() for t in tweets]

counts = {}
for phrase in PHRASES:
    counts[phrase] = sum(1 for m in messages if phrase in m)
    print(f'{phrase}: {counts[phrase]}')


percents = {}
for phrase in PHRASES:
    percents[phrase] = 100 * counts[phrase] / total


print()
print('|           phrase | percent of tweets |')
print('| ---------------- | ----------------- |')
for phrase in PHRASES:
    print(f'| {phrase:>16} | {percents[phrase]:05.2f}             |')


plt.figure(figsize=(8, 5))
plt.barh(PHRASES, [percents[p] for p in PHRASES])
plt.xlabel('Percent of tweets')
plt.ylabel('Phrase')
plt.title('Phrase frequency in Trump tweets')
plt.tight_layout()
plt.savefig('tweets.png')