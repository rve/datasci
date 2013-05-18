import json
import sys

STATES = {
        'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California',
        'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
        'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas',
        'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan',
        'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National',
        'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico',
        'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico',
        'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
        'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia',
        'WY': 'Wyoming'
        }

def valid(tweet):
    if 'text' not in tweet:
        return {}
    if 'place' not in tweet or tweet['place'] is None:
        return {}
    place = tweet['place']
    return tweet if 'country_code' in place and place['country_code'] == 'US' else {}
def get_state(tweet):
    if 'user' not in tweet:
        state = ''
    else:
        state = tweet['user']['location'].split() if 'location' in tweet['user'] else ''
    ret = ''
    for i in state:
        if len(i) > 0 and i in STATES:
            ret = i
    return ret

def solve(sent_file, tweet_file):
    scores = {}
    ans = {} 
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    for line in tweet_file:
        score = 0
        tweet = valid(json.loads(line))
        if len(tweet) > 0 :
            state_name = get_state(tweet)
            if len(state_name) > 0:
                #print state_name
                #print score
                text = tweet['text']
                words = text.split()
                for word in words:
                    if word in scores:
                        score += scores[word]
                if state_name in ans:
                    ans[state_name] += score
                else:
                    ans[state_name] = score

    for a, b in  sorted(ans.iteritems(), key=lambda x:-x[1]) [0:1]:
        print a

def main():
    if len(sys.argv) == 3:
        sent_file = open(sys.argv[1])
        tweet_file = open(sys.argv[2])
    else:
        sent_file = open("./AFINN-111.txt")
        tweet_file = open("./out.data")
    solve(sent_file, tweet_file)

if __name__ == '__main__':
    main()
