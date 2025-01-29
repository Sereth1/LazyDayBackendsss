from django.db import models
from .video_games import VideoGame
from .board_games import BoardGames

class Games(models.Model):
    GAME_TYPES = [
        ('VIDEO', 'Video Game'),
        ('BOARD', 'Board Game'),
    ]

    game_type = models.CharField(max_length=10, choices=GAME_TYPES)  # Choose "VIDEO" or "BOARD"
    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE, null=True, blank=True)
    board_game = models.ForeignKey(BoardGames, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        """Ensures only one of video_game or board_game is set."""
        if self.game_type == "VIDEO":
            self.board_game = None 
        elif self.game_type == "BOARD":
            self.video_game = None  
        super().save(*args, **kwargs)  

    def __str__(self):
        """Displays the name of the selected game."""
        if self.game_type == "VIDEO" and self.video_game:
            return f"Video Game: {self.video_game.name}"
        elif self.game_type == "BOARD" and self.board_game:
            return f"Board Game: {self.board_game.name}"
        return "Invalid Game Entry"
