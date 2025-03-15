import openai
import random

def rule_based_response(user_message):
    message = user_message.lower()
    
    # About You
    if 'who are you' in message or 'your name' in message:
        return "I'm Egwuatu Nonye Shiloh, an AI automation expert and full-stack Django developer."

    # Services
    elif 'services' in message or 'what do you offer' in message:
        return ("I offer web development (Django & TailwindCSS), AI chatbot creation, and automation solutions. "
                "Check out my Projects page for examples!")

    # Projects
    elif 'projects' in message or 'portfolio' in message:
        return "You can view my recent projects on the Projects page. Let me know if you have questions!"

    # Pricing
    elif 'price' in message or 'how much' in message or 'cost' in message:
        return "Pricing varies based on your needs. Please head over to my Contact page so we can discuss it!"

    # Hiring / Contact
    elif 'hire' in message or 'contact' in message or 'work with you' in message:
        return "I'd love to work with you! Please visit my Contact page to get started."

    # If none of the above, fallback to AI
    return None

def get_fallback_response():
    FALLBACK_RESPONSES = [
        "Hmm, I'm not sure how to answer that yet! Could you try rephrasing?",
        "That's a great question! I'll need some time to learn more about it.",
        "I didn't quite catch that. Can you ask me something else?"
    ]

    TECHNICAL_ERROR_MESSAGE = (
        "Oops! Something went wrong on my end. Please try again shortly or reach out via the Contact page!"
    )

    return (random.choice(FALLBACK_RESPONSES), TECHNICAL_ERROR_MESSAGE)

def detect_user_sentiment(user_message):
    message = user_message.lower()

    frustration_keywords = [
        "annoyed", "frustrated", "useless", "waste of time", "angry", "mad",
        "doesn't work", "not working", "hate", "stupid", "dumb", "nonsense"
    ]

    interest_keywords = [
        "amazing", "awesome", "impressive", "great", "cool", "love this",
        "want to hire you", "how can I work with you", "how much", "price", "cost"
    ]

    # Check for frustration
    for keyword in frustration_keywords:
        if keyword in message:
            return "frustrated"

    # Check for interest
    for keyword in interest_keywords:
        if keyword in message:
            return "interested"

    # No strong sentiment detected
    return None

def check_for_moderation(user_message):
    try:
        response = openai.Moderation.create(input=user_message)
        results = response["results"][0]

        # If flagged, return True and the categories flagged
        if results["flagged"]:
            categories = [cat for cat, flagged in results["categories"].items() if flagged]
            return True, categories

        return False, None
    except Exception as e:
        # In production, you'd log this
        print(f"Moderation API error: {e}")
        return False, None
