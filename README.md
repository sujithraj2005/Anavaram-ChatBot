# Annavaram Temple Chatbot 🏛️

An intelligent AI-powered chatbot that provides information about the Annavaram Temple using Retrieval-Augmented Generation (RAG) technology. The chatbot can answer questions about the temple by searching through a knowledge base PDF and generating contextual responses using Groq's Llama language model.

## 🌟 Features

- **Intelligent Q&A**: Ask questions about Annavaram Temple and get accurate, contextual answers
- **RAG Technology**: Combines document search with AI generation for reliable responses
- **Modern Web Interface**: Clean, responsive chat interface with temple-themed design
- **Real-time Interaction**: AJAX-powered chat without page refreshes
- **Vector Search**: Uses FAISS for efficient semantic search through temple information
- **PDF Knowledge Base**: Extracts and processes information from PDF documents

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **AI/ML**: LangChain, Groq API (Llama-3.3-70B), FAISS Vector Database
- **Frontend**: HTML, CSS, JavaScript (jQuery), Bootstrap
- **Document Processing**: PyPDF2
- **Vector Embeddings**: TF-IDF (scikit-learn)

## 📋 Prerequisites

- Python 3.7+
- Groq API Key (free tier available at https://console.groq.com)
- Internet connection for API calls

## 🚀 Installation

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd Annavaram_ChatBot
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Groq API Key**
   
   Create a `.env` file in the project root directory with your Groq API key:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```
   
   You can also set it via command line:
   ```bash
   # Windows:
   set GROQ_API_KEY=your_actual_groq_api_key_here
   
   # macOS/Linux:
   export GROQ_API_KEY=your_actual_groq_api_key_here
   ```

## 📁 Project Structure

```
Annavaram_ChatBot/
├── app.py                 # Main Flask application
├── annavaram.pdf         # Knowledge base document
├── true_python_file.py   # Testing script
├── templates/
│   └── chat.html         # Chat interface template
├── static/
│   ├── style.css         # Styling for the chat interface
│   └── doctor.jpeg       # Bot avatar image
├── venv/                 # Virtual environment
└── __pycache__/          # Python cache files
```

## 🎯 Usage

1. **Start the Application**
   ```bash
   python app.py
   ```

2. **Access the Chatbot**
   - Open your web browser
   - Navigate to `http://127.0.0.1:8080`
   - Start asking questions about Annavaram Temple!

3. **Example Questions**
   - "What are the different types of darshanas available?"
   - "Tell me about the history of Annavaram Temple"
   - "What are the temple timings?"
   - "How can I reach Annavaram Temple?"
   - "What festivals are celebrated at the temple?"

## 🔧 Configuration

### Changing Port
To run on a different port, modify `app.py`:
```python
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)  # Change port here
```

### Using Environment Variables for API Key
The application automatically loads the Groq API key from the `.env` file:
```python
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
```

## 🏗️ How It Works

1. **Document Processing**: The PDF document is processed and split into chunks (800 characters with 200 overlap)
2. **Vector Embeddings**: Text chunks are converted to vector embeddings using TF-IDF (300 features)
3. **Vector Storage**: FAISS creates a searchable database of document embeddings
4. **Query Processing**: User questions are converted to embeddings and matched with relevant chunks (top 3)
5. **Answer Generation**: Groq's Llama-3.3-70B model generates contextual answers based on retrieved information

## 🔍 API Endpoints

- `GET /` - Serves the chat interface
- `POST /get` - Processes chat messages and returns AI responses

## 🎨 Customization

### Styling
Modify `static/style.css` to customize:
- Colors and themes
- Chat bubble styles
- Typography
- Responsive breakpoints

### Content
Replace `annavaram.pdf` with your own PDF document to create a chatbot for different topics.

### Bot Avatar
Replace `static/doctor.jpeg` with your preferred bot avatar image.

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed: `pip install -r requirements.txt`

2. **GROQ_API_KEY Not Found**
   - Verify `.env` file exists in the project root
   - Check that `GROQ_API_KEY=your_key` is properly set
   - Ensure the API key is valid and active

3. **PDF Not Found**
   - Verify `annavaram.pdf` is in the project root
   - Check file permissions
   - Ensure the file path is correct

4. **Port Already in Use**
   - Change port in `app.py` (default is 8085)
   - Or kill existing processes using the port

## 📝 Development

### Testing
Use `true_python_file.py` to test the RAG functionality without running the web interface:
```bash
python true_python_file.py
```

### Adding New Features
- Modify `app.py` for backend changes
- Update `templates/chat.html` for frontend modifications
- Add new routes as needed

## 🔒 Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive information
- Consider rate limiting for production deployment
- Implement user authentication if needed

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues and questions:
- Check the troubleshooting section
- Create an isGroq API setup at https://console.groq.com

## 🙏 Acknowledgments

- Groq for the fast Llama language model
- LangChain for the RAG framework
- FAISS for efficient vector search
- scikit-learn for TF-IDF vectorization
- FAISS for efficient vector search
- Bootstrap for responsive design components

---

**Note**: Make sure to replace `<repository-url>` with your actual repository URL if you plan to host this on GitHub or similar platforms.