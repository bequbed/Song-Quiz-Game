import random
import time

class SongQuiz:
    def __init__(self, songs, difficulty_levels):
        self.songs = songs
        self.difficulty_levels = difficulty_levels
        self.score = 0
        self.high_score = 0

    def start_quiz(self):
        print("Welcome to the Song Quiz!")

        while True:
            # Select a random song and difficulty level
            current_song = random.choice(self.songs)
            current_difficulty = self.difficulty_levels[current_song]

            # Display the current score and high score
            print(f"\nScore: {self.score} | High Score: {self.high_score}")

            # Display the current song and difficulty level
            print(f"\nNow playing: {current_song} (Difficulty: {current_difficulty})")

            # Start the timer for each question
            start_time = time.time()
            user_guess = input("Guess the song title: ").strip().lower()
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)

            # Check the user's guess and update the score
            if user_guess == current_song.lower() and time_taken <= current_difficulty:
                print(f"Correct! You guessed it in {time_taken} seconds.\n")
                self.score += current_difficulty
            else:
                print(f"Wrong! The correct answer is {current_song}\n")
                self.score = 0  # Reset the score for a wrong answer

            # Update the high score if needed
            if self.score > self.high_score:
                self.high_score = self.score

            # Ask if the user wants to play again
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing! Your final score is:", self.high_score)
                break

    # ... (Other methods remain the same)

# Example usage:
if __name__ == "__main__":
    song_difficulty = {"Song A": 3, "Song B": 2, "Song C": 1, "Song D": 3, "Song E": 2}
    song_list = list(song_difficulty.keys())

    quiz = SongQuiz(song_list, song_difficulty)
    quiz.start_quiz()

