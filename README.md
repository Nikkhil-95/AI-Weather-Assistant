# 🌤️ AI Weather Assistant

An AI-powered command-line chatbot that can provide **live weather information for any location** using an LLM with tool calling and the OpenWeatherMap API.

The chatbot understands the user's request, decides when the weather tool is needed, fetches the current weather, and then generates a natural-language response.

---

## 🚀 Features

* 🤖 AI-powered conversational interface
* 🌤️ Get current weather for any location
* 🔧 Uses **LLM tool calling** to access the weather function
* 🌍 Supports different locations and cities
* 💬 Maintains conversation history during the session
* 🔐 Uses environment variables for API keys
* 🖥️ Runs directly from the terminal

---

## 🛠️ Technologies Used

* **Python**
* **LangChain**
* **LangChain Groq**
* **Groq LLM**
* **OpenWeatherMap API**
* **python-dotenv**
* **Rich**

---

## 🧠 How It Works

The chatbot follows this basic workflow:

```text
User
  ↓
User Query
  ↓
Groq LLM
  ↓
Does the query require weather information?
  ↓
Tool Call → get_weather()
  ↓
OpenWeatherMap API
  ↓
Weather Result
  ↓
LLM
  ↓
Final Response
  ↓
User
```

The important concept in this project is **LLM Tool Calling**.

The LLM can decide that it needs external information and call the `get_weather()` tool to retrieve the current weather.

---

## 📂 Project Structure

```text
AI-Weather-Assistant/
│
├── weather_chatbot.py
├── .env
├── .gitignore
└── README.md
```

> **Note:** The `.env` file should never be uploaded to GitHub because it contains API keys.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <https://github.com/Nikkhil-95/AI-Weather-Assistant.git>
```

### 2. Navigate to the project directory

```bash
cd AI-Weather-Assistant
```

### 3. Install the required packages

```bash
pip install rich python-dotenv langchain-groq langchain-community pyowm
```

---

## 🔑 Environment Variables

Create a `.env` file in the project directory.

Add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
```

Replace the values with your actual API keys.

### ⚠️ Important

Never commit your `.env` file to GitHub.

Add the following to `.gitignore`:

```text
.env
```

---

## ▶️ Run the Project

Run the Python file:

```bash
python weather_chatbot.py
```

You will see:

```text
========================================
       🌤️ AI Weather Assistant
========================================
Get live weather information for any location.
Type 'exit' to end the chat.
========================================
```

You can then ask questions such as:

```text
User: What is the weather in Delhi?
```

The AI will use the weather tool to retrieve the current weather information.

To exit:

```text
User: exit
```

---

## 🔧 Weather Tool

The project defines a custom LangChain tool:

```python
@tool
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    """
    return weather.run(location)
```

This function connects the LLM with the OpenWeatherMap weather service.

The LLM can call this tool when the user's question requires current weather information.

---

## 💡 Key Concepts Learned

This project helped me practice several important concepts:

* Environment variables
* API integration
* LangChain
* LLM tool calling
* Custom LangChain tools
* Chat history
* `HumanMessage`
* `AIMessage`
* `ToolMessage`
* LLM responses
* Python functions
* While loops
* Exception-free tool execution flow
* Command-line chatbot development

---

## 🔮 Future Improvements

Possible improvements for future versions:

* Add weather forecasts
* Add temperature conversion
* Handle invalid locations
* Add better error handling
* Add conversation memory
* Support multiple tools
* Add a graphical user interface
* Improve the chatbot's response formatting
* Add more real-world APIs

---

## 👨‍💻 Author

**Nikhil**

This project was created as part of my learning journey in **Python, Generative AI, LLMs, LangChain, and AI Agent development**.


