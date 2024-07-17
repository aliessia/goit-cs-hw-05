import requests
from collections import Counter
import matplotlib.pyplot as plt
import re

def map_reduce(input_data, mapper, reducer):
    mapped = []
    for item in input_data:
        mapped.extend(mapper(item))
    grouped = {}
    for key, value in mapped:
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(value)
    reduced = []
    for key, values in grouped.items():
        reduced.append((key, reducer(values)))
    return reduced

def mapper(text):
    words = re.findall(r'\w+', text.lower())
    return [(word, 1) for word in words]

def reducer(values):
    return sum(values)

def visualize_top_words(word_counts, top_n=10):
    top_words = dict(Counter(dict(word_counts)).most_common(top_n))
    plt.bar(top_words.keys(), top_words.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top Words by Frequency')
    plt.show()

if __name__ == "__main__":
    url = 'https://www.gutenberg.org/files/64317/64317-0.txt'  
    response = requests.get(url)
    text = response.text

    word_counts = map_reduce([text], mapper, reducer)
    visualize_top_words(word_counts)
