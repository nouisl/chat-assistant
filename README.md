# Chat Assistant
Simple chat assistant with OpenAI API


## Project Setup Instructions

This project uses Flask, a Python web framework, to create a chat application with OpenAI's GPT-3.5-turbo-1106 model. The chat interface is created using HTML and AJAX.


### Prerequisites

- Python 3.6 or higher
- Flask
- Flask-CORS (if you're running the server and client on different domains)


### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the required Python packages using pip:

```bash
pip install flask flask-cors openai python-dotenv
```
4. Create a .env file in the project directory and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```
Replace your_api_key_here with your actual OpenAI API key.


### Running the Application

1. Start the Flask server:

```bash
python server.py
```

The server will start and listen for requests on `localhost:5000`.

2. Open `index.html` in your web browser:

You can do this by navigating to the file in your file explorer and double-clicking it, or by entering the file path in your web browser's address bar.

And that's it! You should now be able to chat with the GPT-3.5-turbo-1106 model through the chat interface in your web browser. Enjoy! 😊
