# Wordle Game

## Overview  
This is an advanced word guessing game built using **Python** and **Streamlit**. The game randomly selects a meaningful English word of a specified length, and the player has to guess it within a limited number of chances. It gives real-time feedback on correct and misplaced letters, dynamically tracks the available letters after each guess, calculates the accuracy of the player's guesses, and offers a visually appealing Streamlit interface.

---

## Features
🎯 Random selection of a meaningful word of user-specified length.
✅ Feedback on correct and misplaced letters.
🔡 Dynamic display of available letters after each guess.
📊 Accuracy calculation based on correct letter positions.
🌐 Streamlit-based web UI for smooth, interactive gameplay.
🎨 Animated gradient background for enhanced aesthetics.

---

## Technologies Used
- **Python**
- **Streamlit**
- **NLTK (Natural Language Toolkit)**

---

## Installation & Setup

### 1️⃣ Clone the Repository:
```bash
git clone https://github.com/srivatsavdevarakonda/wordle_game
cd wordle_game
```

### 2️⃣ Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application:
```bash
streamlit run wordle.py
```

---

## How to Play

### 🔽 **Setup Phase:**
- Select the desired word length (e.g., 5-letter word).
- Choose the number of chances you want.
- The system randomly picks a meaningful word based on your settings.

### ▶️ **Gameplay Phase:**
- Enter a word matching the selected length.
- The system gives feedback:
  - ✅ Letters in the **correct position** are highlighted.
  - 🔄 Letters that are in the system's word but at the **wrong position** are shown.
  - 🚫 Letters that do **not exist** in the word are removed from the available alphabet list.
- Your **accuracy percentage** is calculated and shown after each guess.
- The game continues until:
  - You guess the correct word, OR
  - You run out of all available chances.

### 🏁 **End Phase:**
- The correct word and its meaning (fetched from WordNet) are displayed.
- Your final accuracy is displayed.
- You are given an option to **Play Again**.

---

## Enhancements
1. **Streamlit UI Integration:**  
   User-friendly, web-based interactive interface.
  
2. **Dynamic Letter Tracking:**  
   After every guess, available letters are dynamically updated and displayed, helping you eliminate unnecessary options.
  
3. **Accuracy Calculation:**  
   Tracks how close you are to guessing the correct word based on correct letter positions.

4. **Animated Gradient Background:**  
   Adds an attractive, smooth color-changing background for visual engagement.

---

## Future Improvements
1. **Multiplayer Mode:** Compete with friends in real-time.
2. **Difficulty Levels:** Introduce increasing word complexity and tougher levels.
3. **Leaderboard & Score Saving:** Integrate with a database to save scores, progress, and leaderboard rankings.

---

## Author
👤 **D SRIVATSAV**  
GitHub: [@srivatsavdevarakonda](https://github.com/srivatsavdevarakonda)

---

## License
This project is licensed under the **MIT License** - see the `LICENSE` file for details.

