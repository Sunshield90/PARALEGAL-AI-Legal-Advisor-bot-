# PARALEGAL-AI-Legal-Advisor-bot-
ParaLegal: An AI-powered legal research assistant using RAG to answer questions from your case studies.

ParaLegal - AI Legal Assistant
Instant Legal Insight, Powered by AI.

ParaLegal is a full-stack application that leverages a local Large Language Model (LLM) and a Retrieval-Augmented Generation (RAG) pipeline to allow legal professionals and students to "chat" with their case files. Upload a PDF document and ask questions to get immediate, context-aware answers.

Features
Interactive Chat Interface: A clean, modern user interface for asking questions and receiving answers.
PDF Document Processing: Leverages PyPDFLoader to load and split legal documents for analysis.
Retrieval-Augmented Generation (RAG): Uses langchain to build a RAG pipeline, ensuring answers are grounded in the context of the provided document.
Local LLM Support: Powered by Ollama and the tinyllama model, allowing the entire application to run locally without external API calls.
Flexible Model Backend: The code is structured to easily switch between local models and the OpenAI API for more powerful models like GPT-3.5.
Voice Assistant: Includes a voice-to-text feature for hands-free interaction.

How It Works
The project uses a RAG architecture to provide accurate answers:
Load: A legal document (e.g., doc.pdf) is loaded and split into manageable chunks.
Embed & Store: The text chunks are converted into vector embeddings using OllamaEmbeddings and stored in an in-memory vector store (DocArrayInMemorySearch).
Retrieve: When you ask a question, the system retrieves the most relevant text chunks from the vector store.
Generate: The retrieved context and your original question are passed to a language model (tinyllama), which generates a coherent answer based only on the information provided.

Installation and Setup
Prerequisites
Python 3.8+
Git
Ollama for running the local LLM.
1. Clone the Repository
"git clone https://github.com/Sunshield90/PARALEGAL-AI.git"
"cd PARALEGAL-AI"
2. Install Dependencies
Install the required Python packages using the requirements.txt file.
"pip install -r requirements.txt"
3. Setup Your Local LLM
Make sure Ollama is installed and running.
Pull the tinyllama model by running the following command in your terminal:
"ollama run tinyllama"  (I have used tinyllama model, and if you want to use other model like llama:7b, llama:13b, etc; you can use it with changes to be done in code)
[4. OpenAI API Setup
If you wish to use OpenAI models, you will need to:
Create a file named .env in the project's root directory.
Add your OpenAI API key to the file like this:
" OPENAI_API_KEY="sk-your-openai-api-key" "
Change the MODEL variable in model.ipynb to an OpenAI model (e.g., "gpt-3.5-turbo")]

Running the Application
1. Start the Backend Server
The backend is powered by a FastAPI server. Run the following command from the project root:
"uvicorn main:app --reload"
The server will be running at http://127.0.0.1:8000.
2. Launch the Frontend
Simply open the frontend.html file in your web browser. The interface will connect to the backend server automatically.

How to Use
Replace the Document: You can replace the default doc.pdf file with any other legal PDF you wish to analyze. Make sure the new file is named doc.pdf or update the filename in model.ipynb.
Ask Questions: Use the chat interface to ask questions about the content of the PDF. The AI will provide answers based on the document's contents.
