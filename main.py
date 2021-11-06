import time

from src.config import Config
from src.loop import Loop

from pathlib import Path

if __name__ == "__main__":
    config = Config()

    users = []
    for u in config.users:
        last_image = None
        last_image_path = Path(__file__).resolve().parent / ('last_image_'+u)
        if last_image_path.exists():
            with open(last_image_path, 'r') as f:
                last_image = f.read().strip()

        last_story = None
        last_story_path = Path(__file__).resolve().parent / ('last_story_'+u)
        if last_story_path.exists():
            with open(last_story_path, 'r') as f:
                last_story = f.read().strip()

        users.append(Loop(config, u, last_image, last_story))

    while True:
        for user in users:
            user.run()
        time.sleep(config.delay)
