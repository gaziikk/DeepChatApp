# chat_service.py
import requests
from config import Config

class ChatService:
    """
    Класс для взаимодействия с API чат-бота DeepSeek AI через OpenRouter\n

    Класс предоставляет метод для отправки сообщения от пользователя и получения ответа от модели.\n
    Обрабатывает возможные ошибки при взаимодействии с API.
    """
    @staticmethod
    def send_message(user_message: str) -> str:
        """
        Отправляет сообщение пользователя в API DeepSeek AI и возвращает ответ от Deepseek-R1.

        Args:
            user_message (str): Сообщение пользователя, которое нужно отправить чат-боту.

        Returns:
            str: Ответ модели DeepSeek AI в случае успешного запроса.
                 Строка с описанием ошибки в случае проблем с API или других исключений.

        Raises:
            requests.exceptions.HTTPError:  Если HTTP-запрос завершился с кодом ошибки (4xx или 5xx).
            Exception: При возникновении любой другой ошибки (проблемы с сетью, JSON-декодированием, и т.д.)

        Example:
        ```python
            response = ChatService.send_message("Привет! Как у тебя дела?")
            print(response)
        ```
            Выведет ответ чат-бота или сообщение об ошибке
        """
        try:
            headers = {
                "Authorization": f"Bearer {Config.API_KEY.strip()}",
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "DeepChatApp",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": Config.MODEL,
                "messages": [
                    {"role": "user", "content": user_message}
                ]
            }
            
            response = requests.post(
                Config.API_URL,
                headers=headers,
                json=data,
                timeout=10
            )
            response.raise_for_status()
            
            return response.json()['choices'][0]['message']['content']
            
        except requests.exceptions.HTTPError as err:
            return f"Ошибка API: {err.response.text}"
        except Exception as ex:
            return f"Ошибка: {str(ex)}"