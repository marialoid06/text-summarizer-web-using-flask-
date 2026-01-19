import nltk
from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download everything needed (newer NLTK requires punkt_tab too)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


app = Flask(__name__)

def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))

    # Calculate word frequencies
    word_frequencies = {}
    for word in word_tokenize(text):
        if word.lower() not in stop_words and word.isalnum():
            word_frequencies[word.lower()] = word_frequencies.get(word.lower(), 0) + 1

    # Normalize frequencies
    max_freq = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    # Score sentences
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    # Pick top sentences
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = " ".join(summarized_sentences)
    return summary if summary else "Text is too short to summarize."

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        summary = summarize_text(text)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
