from textblob import TextBlob

print("\nDV06AI00020\n")

def polarity_check(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"\n Sentiment Analysis:")
    print(f"Polarity Score: {polarity:.2f}")
    print(f"Subjectivity Score: {subjectivity:.2f}")
    print(f"Overall Sentiment: {sentiment}")

    return sentiment

if __name__ == "__main__":
    user_input = input("Enter text to analyze: ")
    polarity_check(user_input)
