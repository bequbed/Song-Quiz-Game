import random

class SongQuiz:
    def __init__(self, songs):
        self.songs = songs
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Song Quiz!!")

        while self.songs:
            current_song = random.choice(self.songs)
            self.play_song(current_song)
            user_guess = input("Guess the song title: ").strip().lower()

            if user_guess == current_song.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {current_song}\n")

            self.songs.remove(current_song)

        print(f"Quiz completed! Your final score is {self.score}/{len(songs)}.")

    def play_song(self, song):
        print(f"Now playing: {song}")

# Example usage:
if __name__ == "__main__":
    song_list = ["Song A", "Song B", "Song C", "Song D", "Song E"]
    quiz = SongQuiz(song_list)
    quiz.start_quiz()
