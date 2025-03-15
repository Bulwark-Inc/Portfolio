import json
import asyncio
from django.http import HttpResponse
from openai import AsyncOpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
from django.conf import settings
from .bot import chatbot, check_for_moderation
from .utilities import rule_based_response, get_fallback_response, detect_user_sentiment

# Initialize the OpenAI client with your API key
client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')

        if not user_message:
            return JsonResponse({'error': 'No message provided'}, status=400)
        
        # Firstly, Check for harmful content first!
        flagged, categories = asyncio.run(check_for_moderation(user_message))
        if flagged:
            return JsonResponse({
                'reply': f"Sorry, I can't respond to that. The message was flagged for: {', '.join(categories)}."
            }, status=400)
        
        # Secondly, detect sentiment
        sentiment = detect_user_sentiment(user_message)

        if sentiment == "frustrated":
            return JsonResponse({
                'reply': "I'm really sorry about that! Can you let me know what's not working? You can also reach me directly on the Contact page so I can help you faster."
            })

        if sentiment == "interested":
            return JsonResponse({
                'reply': "Thank you! 😊 If you're interested in working together, feel free to visit my Contact page or send me an email at shilohe.ai@gmail.com!"
            })
        
        # Thirdly, try rule-based
        reply = rule_based_response(user_message)
        if reply:
            return JsonResponse({'reply': reply})
        
        try:
            # Retrieve conversation history and set default system message
            chat_history = request.session.get('chat_history', [])
            system_message = {
                "role": "system",
                "content": "You are Shiloh's assistant. If users ask about working together, pricing, or services, direct them to the Contact page: /contact or email shilohe.ai@gmail.com"
            }

            chat_history.append({"role": "user", "content": user_message})
            recent_history = chat_history[-5:]
            messages = [system_message] + recent_history
            messages.append({"role": "user", "content": user_message})
            
            response = asyncio.run(chatbot(user_message, messages))

            if not response or len(response.strip()) == 0:
                response = get_fallback_response()[0]
            
            # Append bot response to chat history
            chat_history.append({"role": "assistant", "content": response})
            request.session['chat_history'] = chat_history

            # Save chat history using sync_to_async
            ChatMessage.objects.create(
                user_message=user_message,
                bot_response=response
            )

            return HttpResponse(json.dumps({'reply': response}), content_type='application/json')
        except Exception as e:
            return HttpResponse(json.dumps({get_fallback_response()[1]}), content_type='application/json', status=500)

    return HttpResponse(json.dumps({'error': 'Invalid request method'}), content_type='application/json', status=405)