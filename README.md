# 🤖 Gemini AI Chatbot

The **Gemini AI Chatbot** is an interactive chatbot powered by **Google's Gemini 2.0 Pro API**, built with **Streamlit** in Python. This chatbot enables users to engage in intelligent conversations with a clean and modern UI.

## 🚀 Features
- **🔹 AI-powered responses** using Google's Gemini 2.0 Pro API.
- **🎨 Beautiful and user-friendly UI** designed with Streamlit.
- **⚡ Fast response time** for an interactive experience.
- **📝 Persistent chat history** for continuity in conversations.
- **🌐 Easy deployment** using GitHub Actions or Render.

## 📂 Project Structure
```
📦 Gemini-Chatbot
 ├── chatbot.py        # Main Streamlit chatbot script
 ├── requirements.txt  # List of dependencies
 ├── .env              # API key storage (not pushed to GitHub)
 ├── README.md         # Documentation
 ├── assets/           # Images and icons for UI
 ├── config.py         # Configuration settings
```

## 🛠️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Gemini-Chatbot.git
cd Gemini-Chatbot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Your API Key  
- Visit [Google AI Studio](https://ai.google.dev/) and generate an API Key.  
- Create a `.env` file in the project folder and add:
  ```
  API_KEY=your_gemini_api_key_here
  ```

### 4️⃣ Run the Chatbot
```bash
streamlit run chatbot.py
```
- Open the provided `localhost:8501` link in your browser.  
- Start chatting with Gemini AI!

## 🎨 User Interface Preview
> _*(Add a screenshot or GIF of your chatbot interface here!)*_

## 🖥️ Deployment
You can deploy this chatbot using **Render** or **GitHub Actions**.

### 📌 Deploy on Render:
1. Create an account on [Render](https://render.com/).
2. Connect your GitHub repository.
3. Set up environment variables (`API_KEY`).
4. Deploy the application!

### 📌 Deploy Using GitHub Actions:
1. Create a **workflow file** in `.github/workflows/`.
2. Add deployment steps to install dependencies and run the chatbot.
3. Commit and push to GitHub.
4. The chatbot will be deployed automatically.

## 🌟 Contributing
Contributions are welcome! To contribute:  
1. **Fork** this repository.  
2. **Create a new branch** (`git checkout -b feature-branch`).  
3. **Commit your changes** (`git commit -m "Added new feature"`).  
4. **Push to your branch** (`git push origin feature-branch`).  
5. **Submit a Pull Request**.

## ⚖️ License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

👨‍💻 Developed by **Atul Kumar**  