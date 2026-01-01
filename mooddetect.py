#making an mood detector ai
def mood_detector(text):
    text = text.lower()

    happy_words = ["happy", "great", "awesome","good","love"]
    sad_words = ["sad", "cry", "upset", "depressed"]
    angry_words = ["angry", "hate", "mad", "irritate"]

    for word in happy_words:
        if(word in text):
            return "🤪happy mood"
    for word in sad_words:
        if(word in text):
            return "😒sad mood"
    for word in angry_words:
        if(word in text):
            return "🤨angry mood"
    
    
sentence = input("type something   ")
result = mood_detector(sentence)
print("AI thing your mood is", result)

        