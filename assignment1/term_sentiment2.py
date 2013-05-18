import json
import sys

def hw(sent_file, tweet_file):
    new_words_score = {}
    new_words_freq = {}
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
            total_score = 0
            for word in words:
                if word in scores:
                    total_score += scores[word]
            for word in words:
                if word not in scores:
                    if word in new_words_score:
                        new_words_score[word] += total_score
                        new_words_freq[word] += 1
                    else:
                        new_words_score[word] = total_score
                        new_words_freq[word] = 1
    for item in new_words_score:
        new_words_score[item] /= new_words_freq[item]
        print "%s %d" % (item, new_words_score[item])

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
