from textblob import TextBlob

# Intent keywords
intent_keywords = {
    "billing dispute": ["charged twice", "duplicate charge", "wrong bill", "overcharged"],
    "account inquiry": ["account", "login", "password", "access"],
    "payment issue": ["payment failed", "transaction failed", "card declined"],
    "technical support": ["not working", "error", "bug", "technical issue"],
    "service complaint": ["bad service", "unacceptable", "complaint"]
}

# Topic keywords
topic_keywords = {
    "credit card charges": ["charged", "transaction", "credit card"],
    "account access issues": ["login", "password", "access"],
    "subscription cancellation": ["cancel", "unsubscribe"],
    "service outage": ["down", "not working", "offline"]
}

# Escalation phrases
escalation_phrases = [
    "speak to manager",
    "not resolved",
    "unacceptable",
    "fix immediately",
    "very frustrated"
]


def detect_intent(text):
    text = text.lower()

    for intent, words in intent_keywords.items():
        for word in words:
            if word in text:
                return intent

    return "account inquiry"


def detect_topic(text):
    text = text.lower()

    for topic, words in topic_keywords.items():
        for word in words:
            if word in text:
                return topic

    return "general inquiry"


def detect_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity == 0:
        return "neutral"
    else:
        return "negative"


def detect_escalation(text):
    text = text.lower()

    for phrase in escalation_phrases:
        if phrase in text:
            return "high"

    return "low"


def analyze_conversation(conversation):

    intent = detect_intent(conversation)
    topic = detect_topic(conversation)
    sentiment = detect_sentiment(conversation)
    escalation = detect_escalation(conversation)

    return {
        "intent": intent,
        "topic": topic,
        "sentiment": sentiment,
        "escalation_risk": escalation
    }