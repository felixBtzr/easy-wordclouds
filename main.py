from collections import Counter
import fitz  # PyMuPDF
import re  # Reguläre Ausdrücke
import nltk  # natural language toolkit
from nltk.corpus import stopwords  # Stoppwörter ignorieren
import matplotlib.pyplot as plt  # zum Vorbereiten der Wordclouds
from wordcloud import WordCloud  # wordclouds

# Lade die NLTK-Stoppwörter
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('german'))

# Füge Zahlen von 1 bis 100 als Stoppwörter hinzu
stopwords_with_numbers = [str(i) for i in range(0, 2025)]
stop_words.update(stopwords_with_numbers)


def extract_text_from_pdf(pdf_path):
    """
    Extrahiert den gesamten Text aus einer PDF-Datei.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text


def get_most_common_words(text, num_common=50):
    """
    Zählt die häufigsten Wörter im Text.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    most_common_words = word_count.most_common(num_common)
    common_words = {word for word, _ in most_common_words}
    return common_words


def count_words(text, custom_stopwords):
    """
    Zählt die Wörter im Text, ausgenommen der Stoppwörter, und sortiert sie nach Häufigkeit.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    words = [word for word in words if word not in custom_stopwords]
    word_count = Counter(words)
    filtered_word_count = {word: count for word, count in word_count.items() if count > 1}
    sorted_word_count = sorted(filtered_word_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_word_count


def create_wordcloud(word_freq, title):
    """
    Erstellt und zeigt eine Wortwolke basierend auf den Wortfrequenzen.
    """
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(word_freq))
    plt.figure(figsize=(10, 5), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.title(title)
    plt.show()


def process_pdf(pdf_path, additional_stopwords=None):
    """
    Hauptfunktion, die die PDF-Datei verarbeitet und eine Wortwolke erstellt.
    """
    if additional_stopwords is None:
        additional_stopwords = []

    # Extrahiere den Text aus der PDF
    text = extract_text_from_pdf(pdf_path)

    # Extrahiere häufige Stoppwörter aus der PDF-Datei
    custom_stopwords = get_most_common_words(text)
    custom_stopwords.update(additional_stopwords)

    # Füge die extrahierten Stoppwörter zu den NLTK-Stoppwörtern hinzu
    all_stopwords = stop_words.union(custom_stopwords)

    # Zähle die Wörter im Text, ohne Stoppwörter
    word_frequencies = count_words(text, all_stopwords)

    # Ausgabe der Wörter und ihrer Häufigkeit
    for word, frequency in word_frequencies:
        print(f'{word}: {frequency}')

    # Erstelle eine Wortwolke
    create_wordcloud(word_frequencies, "Wortwolke ohne Stoppwörter")


# Beispielnutzung
pdf_path = 'Kaiserslautern.pdf'

# Wenn keine zusätzlichen Stoppwörter angegeben sind, wird die Liste leer sein
additional_stopwords = ['org', 'm', 'befindet', 'etwa', 'wurden', 'isbn', 'sogenannte', '000', 'html', 'web', 'http', 'zudem']

process_pdf(pdf_path, additional_stopwords)
