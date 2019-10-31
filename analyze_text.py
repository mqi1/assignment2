import random
import string


def remove_yang_words(filename):
    '''
    read a file to create a dictionary that takes words as keys and occurrences as values. 
    if a word from the file is part of the list 'Yang_Words' it will not be appended onto the dictionary, else, it will. 
    '''
    hist = {}
    Yang_Words = ['Yang','yang','Andrew','andrew','yanggang','YangGang','Yanggang', 'yanggang2020', 'YangGang2020', 'Yanggang2020', 'AndrewYang', 'YangGang', 'I'
    , 'Yang2020']
    fyle = open(filename)
    for line in fyle:
        for word in line.split():
            if word not in Yang_Words:
                word = word.lower()
                hist[word]=hist.get(word,0)+1
    return hist


def total_words(hist):
    '''
    return the number of total words in the histogram
    '''
    return sum(hist.values())


def different_words(hist):
    '''
    return the number of different words in the histogram
    '''
    i = 0
    for word in hist.items():
        i+= 1
    return i
    print(different_words(hist))


def most_common(hist, excluding_stopwords=True):
    '''
    exclude any words that appear on the stopwords txt file out of the the frequency count.
    Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    '''
    exclude_list = remove_yang_words('stopwords.txt')
    new = []
    for word, frequency in hist.items():
        if excluding_stopwords:
            if word not in exclude_list:
                new.append((frequency, word))
        else:
            new.append((frequency, word))
    new.sort()
    new.reverse()
    return new


def print_most_common(hist, num=10):
    '''
    print the most common words that appeared more than 10 times
    '''
    common_wordlist = most_common(hist)
    print (common_wordlist[:num])


def main():
    hist = remove_yang_words('tweetslist_final.txt')
    print('Total number of words:', total_words(hist))
    print('Average number of words per tweet:', total_words(hist)/1000)
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:50]:
        print(word, '\t', freq)


if __name__ == '__main__':
    main()