# AI-Powered Telegram Chatbot

This project is a Telegram chatbot powered by an advanced language model hosted on LM Studio. The bot leverages AI capabilities to provide intelligent, conversational responses to user inputs. Developed as a versatile and interactive personal assistant, this chatbot is designed to handle general queries, offer assistance, and engage in meaningful conversations.

## Overview

The chatbot is built using the Telegram Bot API and integrates seamlessly with the LM Studio API, which serves as the backend for generating AI responses. The model used for this project is **TinyLlama-1.1b-Chat-V1.0**, a lightweight but powerful conversational model optimized for responsive and concise interactions.

### Key Features

- **Real-Time Conversations**: Engages with users in natural language and provides instant replies.
- **AI-Powered Responses**: Utilizes a fine-tuned language model to deliver context-aware and helpful answers.
- **Personalization**: Maintains a lightweight chat history to improve response relevance during ongoing conversations.
- **Modularity**: The code is modular, making it easy to maintain and extend with new features.
- **Logging**: Includes robust logging to monitor user interactions and detect any potential issues during execution.
- **Scalability**: Built to handle concurrent user messages efficiently using Telegram's asynchronous framework.

### Workflow

1. **User Interaction**: Users send messages to the bot on Telegram.
2. **Message Processing**: The bot forwards user input to the LM Studio server.
3. **AI Model Execution**: The LM Studio server processes the request using the **TinyLlama** model and generates a response.
4. **Reply Delivery**: The bot receives the AI-generated response and sends it back to the user.

### Chat History

The chatbot maintains a minimal chat history for contextual continuity. This ensures that responses remain coherent while keeping the server requests lightweight and efficient.

### Design Philosophy

This chatbot is designed with simplicity, flexibility, and performance in mind. The code employs a **class-based architecture** for improved readability and modularity. This structure makes it easy to extend the chatbot with new commands, models, or APIs in the future.

### Developer Note

This chatbot was developed by **Ayushi Jaimani** as a demonstration of AI integration in conversational applications. It showcases the synergy between modern natural language processing models and real-world chatbot frameworks like Telegram.

For further queries or contributions, feel free to reach out!
