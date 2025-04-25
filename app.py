from flask import Flask, request, jsonify, render_template
from chat_service import ChatService

app = Flask(__name__)

@app.route('/')
def home():
    """Главная страница с чатом"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_handler():
    """
    Обработчик чат-запросов
    Принимает сообщение и возвращает ответ от API
    """
    user_message = request.form.get('message')
    
    if not user_message or not user_message.strip():
        return jsonify({"error": "Сообщение не может быть пустым"}), 400
    
    bot_response = ChatService.send_message(user_message)
    return jsonify({"message": bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)