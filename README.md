# wordle_game

**Overview** 

This is a word guessing game built using Python and Streamlit. The game randomly selects a meaningful word of a specified length, and the user has to guess it within a limited number of chances. The game provides feedback on correct and misplaced letters, tracks available letters dynamically, and calculates the accuracy of the player's guesses.

**Features**
1. Random selection of a meaningful word of user-specified length.
2. Feedback on correct and misplaced letters.
3. Dynamic display of available letters after each guess.
4. Streamlit-based UI for an interactive gaming experience.
5. Animated gradient background for enhanced visual appeal.

**Technologies Used**
1. Python
2. Streamlit
3. NLTK (Natural Language Toolkit)

**Installation and Setup**
Clone the repository: 
git clone https://github.com/srivatsavdevarakonda/wordle_game
cd wordle_game

**Install dependencies:**
1. pip install -r requirements.txt
2. Run the application:
   streamlit run wordle.py

**Game Logic**
  1. **Setup Phase:**
    The user selects the word length and number of chances.
    The system picks a random meaningful word of the specified length.
  2. **Gameplay Phase:**
    The user enters a word of the specified length.
    Feedback is provided on correct and misplaced letters.
    Available letters are dynamically updated based on the user’s guesses.
    The game continues until the user guesses correctly or runs out of chances.
  3. **End Phase:**
    The correct word and its meaning are displayed.
    The accuracy of the player’s guesses is calculated and shown.
    The user is given an option to play again.

**Enhancements**
1. Streamlit UI Integration: The game is now interactive with real-time feedback.
2. Dynamic Letter Tracking: Available letters are updated dynamically to assist the user.
3. Accuracy Tracking: Displays how close the user is to guessing the correct word.
4. Gradient Background Animation: Enhances the UI aesthetics.

**Future Improvements**
1. Multiplayer mode.
2. Difficulty levels with increasing word complexity.
3. Integration with a database to track user progress.

**Contributors**

D SRIVATSAV (@srivatsavdevarakonda)

**License**

This project is licensed under the MIT License - see the LICENSE file for details.
