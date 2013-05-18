import json
import sys
def work(tweet_file):
    freq_tags= {}
    for line in tweet_file:
        tweet = json.loads(line)
        ENTITY = "entities"
        TAG = "hashtags"
        TEXT = "text"
        if ENTITY in tweet:
            if TAG in tweet[ENTITY]:
                hashtags = tweet[ENTITY][TAG]
                for tag in hashtags:
                    if TEXT in tag:
                        ft = tag[TEXT]
                        if ft in freq_tags:
                            freq_tags[ft] += 1.0
                        else:
                            freq_tags[ft] = 1.0
    for a, b in  sorted(freq_tags.iteritems(), key=lambda x:-x[1]) [:10]:
        print "%s %f" % (a, b)

def main():
    tweet_file = open(sys.argv[1])
    work(tweet_file)

if __name__ == "__main__":
    main()

