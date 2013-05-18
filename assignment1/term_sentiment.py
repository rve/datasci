import json
import sys

def hw(sent_file, tweet_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    for line in tweet_file:
        score = 0
        tweet = json.loads(line)
        text_item = "text"
        if text_item in tweet:
            text = tweet[text_item]
            words = text.split()
            for word in words:
                if word in scores:
                    score += scores[word]
        print score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
