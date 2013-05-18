import sys
import json
def hw(tweet_file):
    freq = {}
    total_freq = 0 
    for line in tweet_file:
        tweet = json.loads(line)
        TEXT = "text"
        if TEXT in tweet:
            text = tweet[TEXT]
            words = text.split()
            for word in words:
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
                total_freq += 1

    for f in freq:
        if total_freq == 0:
            print 0
        else:
            print "%s %f" % (f.encode('utf-8'),freq[f] / (total_freq + 0.0))


def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == "__main__":
    main()
