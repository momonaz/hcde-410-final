# Import necessary libraries
import pandas as pd
import nltk
import gender_guesser.detector as gender
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from gensim import corpora
from gensim.models import LdaModel
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Download required NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Step 1: Data Preprocessing

# Load dataset (replace with the actual file path for your corpus)
df = pd.read_csv('wikipedia_talk_corpus.csv')

# Tokenize text and clean it
df['tokens'] = df['text'].apply(nltk.word_tokenize)

# Remove stopwords and non-alphabetical tokens
stop_words = set(nltk.corpus.stopwords.words('english'))
df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word.isalpha() and word.lower() not in stop_words])

# Step 2: Gender Classification

# Initialize gender detector
d = gender.Detector()

# Function to detect gender from username (or other heuristic methods)
def get_gender(name):
    return d.get_gender(name)

# Apply gender classification to the 'username' column (adjust if needed)
df['gender'] = df['username'].apply(get_gender)

# Step 3: Sentiment Analysis

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    sentiment_score = sid.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return 'positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis to the 'text' column
df['sentiment'] = df['text'].apply(get_sentiment)

# Step 4: Statistical Analysis (Chi-Squared Test)

# Create a contingency table to check sentiment distribution by gender
contingency_table = pd.crosstab(df['gender'], df['sentiment'])

# Perform chi-squared test
chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)
print(f'Chi2: {chi2}, p-value: {p_val}')

# Step 5: Topic Categorization (LDA)

# Prepare the corpus for LDA (Topic Modeling)
dictionary = corpora.Dictionary(df['tokens'])
corpus = [dictionary.doc2bow(text) for text in df['tokens']]

# Apply LDA to extract topics
lda_model = LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

# Print the topics
print("Topics identified by LDA:")
for topic in lda_model.print_topics():
    print(topic)

# Step 6: Visualization

# 1. Sentiment distribution by gender
sns.countplot(x='sentiment', hue='gender', data=df)
plt.title('Sentiment Distribution by Gender')
plt.show()

# 2. Topic modeling visualization (bar chart for the top topics)
topics = lda_model.show_topics(formatted=False)
topic_words = [', '.join([word[0] for word in topic[1]]) for topic in topics]
topic_probs = [topic[0] for topic in topics]

plt.bar(topic_probs, topic_probs)
plt.xticks(topic_probs, topic_words, rotation=90)
plt.title('Topic Modeling - Top 5 Topics')
plt.xlabel('Topic')
plt.ylabel('Probability')
plt.show()

# 3. Sentiment distribution by topic
sns.countplot(x='sentiment', hue='gender', data=df)
plt.title('Sentiment Distribution Across Topics')
plt.show()


