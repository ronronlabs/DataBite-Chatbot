# DataBite Chatbot

DataBite is a web-based chatbot that simplifies data science and analytics terms with ~100-word explanations, like a dictionary for beginners. Built with Python, Streamlit, and Hugging Face's Inference API, it promotes **Data Democratization** by making complex concepts accessible to all.

## Features
- Answers questions about data science, analytics, and risk (e.g., "What is a neural network?").
- Explains terms in simple, 10-year-old-friendly language.

## Example
- **Q**: "What is a neural network?"
- **A**: "A neural network is like a computer brain. It learns from examples to do things like recognize pictures or predict numbers."
- **Q**: "What is an algorithm?"
- **A**: "An algorithm is like a recipe for your favorite cake. It’s a set of steps a computer follows to solve a problem."

## Setup
1. Clone the repo: `git clone https://github.com/pegasuschild/DataBite-Chatbot.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables:
   - `HF_TOKEN`: Hugging Face API key (get from [huggingface.co](https://huggingface.co)).
   - `NGROK_TOKEN`: Ngrok authtoken (get from [dashboard.ngrok.com](https://dashboard.ngrok.com)).
4. Run the app: `streamlit run chatbot_streamlit.py`
5. Open the ngrok URL (e.g., `https://xxxx.ngrok-free.app`).

## Technologies
- Python 3.11
- Streamlit
- Hugging Face Inference API (Mixtral-8x7B model)
- FuzzyWuzzy (for question matching)
- Ngrok (for web hosting)

## About
Built by Daniel Young as a portfolio project to showcase Python and Streamlit skills in rapid prototyping for data science education.

## License
MIT License - feel free to use and modify the code!
