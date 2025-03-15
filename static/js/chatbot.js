document.addEventListener('DOMContentLoaded', () => {
    const chatBtn = document.getElementById('chat-btn');
    const chatbox = document.getElementById('chatbox');
    const closeChat = document.getElementById('close-chat');
    const sendBtn = document.getElementById('send-btn');
    const chatInput = document.getElementById('chat-input');
    const chatLog = document.getElementById('chat-log');

    chatBtn?.addEventListener('click', () => {
        if (chatbox.classList.contains('hidden')) {
            openChatbox();
        } else {
            closeChatbox();
        }
    });

    closeChat?.addEventListener('click', () => {
        closeChatbox();
    });

    sendBtn?.addEventListener('click', async () => {
        const userMessage = chatInput.value.trim();
        if (!userMessage) return;

        chatLog.innerHTML += `<div class="text-right"><strong>You:</strong> ${userMessage}</div>`;
        chatInput.value = '';

        try {
            const response = await fetch('/chatbot/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();

            if (data.reply) {
                chatLog.innerHTML += `<div class="text-left"><strong>AI:</strong> ${data.reply}</div>`;
            } else if (data.error) {
                chatLog.innerHTML += `<div class="text-left text-red-500"><strong>Error:</strong> ${data.error}</div>`;
            }

            chatLog.scrollTop = chatLog.scrollHeight;
        } catch (error) {
            chatLog.innerHTML += `<div class="text-left text-red-500"><strong>Error:</strong> Unable to connect.</div>`;
        }
    });

    function openChatbox() {
        chatbox.classList.remove('hidden', 'scale-95', 'opacity-0');
        chatbox.classList.add('scale-100', 'opacity-100');
    }

    function closeChatbox() {
        chatbox.classList.remove('scale-100', 'opacity-100');
        chatbox.classList.add('scale-95', 'opacity-0');

        chatbox.addEventListener('transitionend', function handler() {
            chatbox.classList.add('hidden');
            chatbox.removeEventListener('transitionend', handler);
        });
    }

    function getCookie(name) {
        const cookieValue = document.cookie.split('; ').find(row => row.startsWith(name + '='));
        return cookieValue ? decodeURIComponent(cookieValue.split('=')[1]) : null;
    }
});
