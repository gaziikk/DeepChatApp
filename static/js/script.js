const chatDiv = document.getElementById('chat');
const form = document.querySelector('.chat-input-container');
const input = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const typingIndicator = document.getElementById('typing-indicator');

function addMessage(sender, message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    const now = new Date();
    const timeString = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    messageDiv.innerHTML = `
                ${message}
                <span class="message-time">${timeString}</span>
            `;

    chatDiv.appendChild(messageDiv);
    chatDiv.scrollTop = chatDiv.scrollHeight;
}

async function sendMessage() {
    const message = input.value.trim();
    if (!message) return;

    addMessage('user', message);
    input.value = '';

    typingIndicator.style.display = 'block';
    chatDiv.scrollTop = chatDiv.scrollHeight;

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `message=${encodeURIComponent(message)}`
        });

        typingIndicator.style.display = 'none';

        if (!response.ok) {
            throw new Error('Ошибка сервера');
        }

        const data = await response.json();

        addMessage('bot', data.message);

    } catch (error) {
        typingIndicator.style.display = 'none';
        addMessage('bot', `<span style="color: #e74c3c;">Ошибка: ${error.message}</span>`);
        console.error('Ошибка:', error);
    }
}

sendBtn.addEventListener('click', sendMessage);
input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
input.focus();