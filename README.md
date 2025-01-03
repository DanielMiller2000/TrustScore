# AI-Powered Virtual Study Buddy

**Smart AI Study Assistant for Effective Learning**
![BOOKBANNER](https://github.com/user-attachments/assets/bcd794d8-97c5-43a3-a47e-e364f15afea1)

Welcome to **AI-Powered Virtual Study Buddy**, a tool designed to make studying easier, faster, and more effective. Whether you're preparing for exams, mastering new topics, or just organizing your notes, this AI-driven assistant helps you stay ahead with summaries, flashcards, and an interactive study chat.

---

## Key Features

- **AI Summarizer**
  - Converts lengthy texts into clear, concise summaries for faster review.

- **Flashcard Generator**
  - Creates personalized flashcards to help you memorize key concepts.

- **Study Chat Assistant**
  - Provides instant explanations, quizzes, and concept reviews based on your needs.

- **Progress Tracker**
  - Monitors study sessions and suggests areas for improvement.

- **Custom Learning Paths**
  - Adapts to individual learning styles and focuses on weak areas.

---

## How It Works

1. **Upload Your Material:**  
   Import notes, articles, or PDFs.
2. **AI Processing:**  
   The AI analyzes content, identifies key points, and generates summaries and flashcards.
3. **Engage with the AI Chat:**  
   Ask questions, test your knowledge, and get clarifications instantly.
4. **Track Your Progress:**  
   Monitor performance and focus on areas where improvement is needed.

---

## Technologies Used

- **AI Frameworks:** GPT, TensorFlow, PyTorch.
- **Backend:** Python and Flask.
- **Frontend:** React for the user interface.
- **Database:** PostgreSQL for storing progress and user data.

---

## Installation

1. Clone the repository:
   ```bash
   # Create a directory for the project and navigate to it
   mkdir StudyBuddyAI_Project
   cd StudyBuddyAI_Project

   git clone https://github.com/yourusername/StudyBuddyAI.git

   cd StudyBuddyAI

   python3 -m venv venv

   source venv/bin/activate  # For MacOS/Linux

   pip install --upgrade pip
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip freeze | grep transformers
   pip freeze | grep sklearn

   python -c "import transformers; print(transformers.__version__)"
   python -c "import sklearn; print(sklearn.__version__)"

   pip install ipython pylint autopep8
   ```
3. Run the project:
   ```bash
   python --version
   python app.py
   tail -f logs/app.log  # Assuming logs are saved in a 'logs' folder
   curl -X POST -H "Content-Type: application/json" -d '{"text":"This is a test input"}' http://127.0.0.1:5000/summarize
   ```

---

## Contributing

We welcome contributions from the community! Fork the repository, create pull requests, or submit issues to help improve the platform.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

- **GitHub:** [Study Buddy Repository](https://github.com/DanielMiller2000/AI-StudyBuddy)
- **Email:** Support@studybuddy.com  
- **Twitter:** [@StudyBuddyAI](https://twitter.com/StudyBuddyAI)  

---

**Learn smarter. Study better. Your AI-powered buddy for success.**
