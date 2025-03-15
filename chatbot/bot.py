from openai import AsyncOpenAI
from django.conf import settings

# Initialize the OpenAI client with your API key
client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def chatbot(user_input, messages):
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200,
            temperature=0.9,
            top_p=1.0,
        )
        # Return the generated response
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Handle errors gracefully
        return f"Sorry, I couldn't process that request right now: {e}"
    
async def check_for_moderation(user_message):
    try:
        response = await client.moderations.create(
            model="omni-moderation-latest",
            input=user_message,
        )
        
        # Access the first result
        first_result = response.results[0]

        # If flagged, extract categories
        if first_result.flagged:
            categories = [cat for cat, flagged in first_result.categories if flagged]
            return True, categories

        # If not flagged
        return False, None

    except Exception as e:
        # Log or handle the error
        print(f"Moderation API error: {e}")
        return False, None
