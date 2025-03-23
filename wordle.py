import streamlit as st
import nltk
import random
from nltk.corpus import words, wordnet

# Download required NLTK data
try:
    nltk.data.find('corpora/words')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('words')
    nltk.download('wordnet')

# Cache word list for better performance
@st.cache_data
def get_word_list():
    return set(word.lower() for word in words.words())

def get_meaningful_word(length):
    """Get a random meaningful word of the specified length."""
    valid_words = [word.lower() for word in words.words() if len(word) == length]
    meaningful_words = [word for word in valid_words if wordnet.synsets(word)]
    
    if meaningful_words:
        return random.choice(meaningful_words)
    else:
        return None

def is_valid_word(word):
    """Check if the word is in the dictionary."""
    word_list = get_word_list()
    return word.lower() in word_list

def provide_feedback(system_word, user_word):
    """Provide feedback based on user guess."""
    correct_position = []
    wrong_position = []
    
    system_word_list = list(system_word)
    
    for i, char in enumerate(user_word):
        if i < len(system_word):
            if char == system_word[i]:
                correct_position.append(char)
                system_word_list[i] = None
            elif char in system_word_list:
                wrong_position.append(char)
                system_word_list[system_word_list.index(char)] = None
    
    return correct_position, wrong_position

def get_word_meaning(word):
    """Fetch and return the meaning of the word using WordNet."""
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    return "No meaning found in the dictionary."

def calculate_accuracy(word_length, guesses_made, correct_letters_history):
    """Calculate player's accuracy based on correct letter positions."""
    total_possible = word_length * len(guesses_made)
    total_correct = sum(len(correct) for correct in correct_letters_history)
    return (total_correct / total_possible) * 100 if total_possible > 0 else 0

# Initialize session state
if 'game_stage' not in st.session_state:
    st.session_state.game_stage = 'setup'
if 'system_word' not in st.session_state:
    st.session_state.system_word = None
if 'guesses' not in st.session_state:
    st.session_state.guesses = []
if 'correct_letters_history' not in st.session_state:
    st.session_state.correct_letters_history = []
if 'used_letters' not in st.session_state:
    st.session_state.used_letters = set()
if 'incorrect_letters' not in st.session_state:
    st.session_state.incorrect_letters = set()

# App title
st.title("Word Guessing Game 🎮")

# Game Setup Stage
if st.session_state.game_stage == 'setup':
    st.write("### Game Setup")
    with st.form("game_setup"):
        word_length = st.slider("Choose word length:", 3, 8, 5)
        max_chances = st.slider("Choose number of chances:", 1, 10, 6)
        submitted = st.form_submit_button("Start Game")
        
        if submitted:
            st.session_state.word_length = word_length
            st.session_state.max_chances = max_chances
            st.session_state.system_word = get_meaningful_word(word_length)
            st.session_state.chances_used = 0
            st.session_state.guesses = []
            st.session_state.correct_letters_history = []
            st.session_state.used_letters = set()
            st.session_state.incorrect_letters = set()
            
            if st.session_state.system_word:
                st.session_state.game_stage = 'play'
            else:
                st.error(f"No meaningful words found of length {word_length}. Please try another length.")

# Game Play Stage
elif st.session_state.game_stage == 'play':
    # Display game status
    st.write(f"### Word length: {st.session_state.word_length}")
    st.write(f"### Chances remaining: {st.session_state.max_chances - st.session_state.chances_used}")
    
    # Display alphabet with used letters crossed out
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols = st.columns(13)
    
    for i, letter in enumerate(alphabet):
        col_index = i % 13
        letter_lower = letter.lower()
        
        if letter_lower in st.session_state.incorrect_letters:
            cols[col_index].markdown(f"<s style='color:red'>{letter}</s>", unsafe_allow_html=True)
        elif letter_lower in st.session_state.used_letters:
            cols[col_index].markdown(f"<span style='color:green'>{letter}</span>", unsafe_allow_html=True)
        else:
            cols[col_index].markdown(f"{letter}")
    
    # Input for user guess
    user_guess = st.text_input(
        "Enter your guess:",
        key="guess_input",
        max_chars=st.session_state.word_length
    ).lower()
    
    if st.button("Submit Guess"):
        if not user_guess.isalpha():
            st.error("Please enter only alphabetic characters.")
        elif len(user_guess) != st.session_state.word_length:
            st.error(f"Please enter exactly {st.session_state.word_length} letters.")
        elif not is_valid_word(user_guess):
            st.error("Word not in word-list. Please try again.")
        else:
            correct_pos, wrong_pos = provide_feedback(st.session_state.system_word, user_guess)
            st.session_state.guesses.append(user_guess)
            st.session_state.correct_letters_history.append(correct_pos)
            st.session_state.chances_used += 1
            
            # Update used letters
            for letter in user_guess:
                st.session_state.used_letters.add(letter)
                
            # Update incorrect letters
            incorrect_letters = [letter for letter in user_guess 
                               if letter not in st.session_state.system_word]
            for letter in incorrect_letters:
                st.session_state.incorrect_letters.add(letter)
            
            # Display feedback for current guess
            if correct_pos:
                st.write(f"Letters in correct position: {', '.join(correct_pos)}")
            if wrong_pos:
                st.write(f"Letters in wrong position: {', '.join(wrong_pos)}")
            if not correct_pos and not wrong_pos:
                st.write("No matching letters.")
            
            # Check win/lose conditions
            if user_guess == st.session_state.system_word:
                st.success("🎉 Congratulations! You guessed the correct word!")
                st.session_state.game_stage = 'end'
            elif st.session_state.chances_used >= st.session_state.max_chances:
                st.error(f"Game Over! The word was '{st.session_state.system_word}'")
                st.session_state.game_stage = 'end'
    
    # Display guess history with colored feedback
    if st.session_state.guesses:
        st.write("### Previous Guesses")
        for idx, guess in enumerate(st.session_state.guesses):
            displayed_guess = ""
            for i, char in enumerate(guess):
                if char == st.session_state.system_word[i]:
                    # Correct position - green
                    displayed_guess += f"<span style='color:green; font-weight:bold'>{char.upper()}</span>"
                elif char in st.session_state.system_word:
                    # Wrong position - orange
                    displayed_guess += f"<span style='color:orange'>{char.upper()}</span>"
                else:
                    # Not in word - normal
                    displayed_guess += f"{char.upper()}"
            
            st.markdown(f"• {displayed_guess}", unsafe_allow_html=True)

# Game End Stage
elif st.session_state.game_stage == 'end':
    # Calculate and display accuracy
    accuracy = calculate_accuracy(
        st.session_state.word_length,
        st.session_state.guesses,
        st.session_state.correct_letters_history
    )
    
    st.write("### Game Summary")
    st.write(f"Word: **{st.session_state.system_word.upper()}**")
    st.write(f"Meaning: *{get_word_meaning(st.session_state.system_word)}*")
    st.write(f"Accuracy: **{accuracy:.1f}%**")
    st.write(f"Guesses used: {len(st.session_state.guesses)} out of {st.session_state.max_chances}")
    
    # Display final alphabet status
    st.write("### Alphabet Status")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols = st.columns(13)
    
    for i, letter in enumerate(alphabet):
        col_index = i % 13
        letter_lower = letter.lower()
        
        if letter_lower in st.session_state.incorrect_letters:
            cols[col_index].markdown(f"<s style='color:red'>{letter}</s>", unsafe_allow_html=True)
        elif letter_lower in st.session_state.used_letters:
            cols[col_index].markdown(f"<span style='color:green'>{letter}</span>", unsafe_allow_html=True)
        else:
            cols[col_index].markdown(f"{letter}")
    
    if st.button("Play Again"):
        st.session_state.game_stage = 'setup'
        st.experimental_rerun()