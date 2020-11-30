import os

VIDEO_DIR = 'video'
AUDIO_DIR = 'audio'
IMAGES_DIR = 'images'
VOLUME_INCREASE = 10

WATERMARK_FILENAME = os.path.join(IMAGES_DIR, 'docode-watermark.png')

VIDEO_SRC_DIR = os.path.join(VIDEO_DIR, 'src')
VIDEO_INTRO_DIR = os.path.join(VIDEO_DIR, 'intro')
VIDEO_END_DIR = os.path.join(VIDEO_DIR, 'end')

INTRO_IMAGE = os.path.join(IMAGES_DIR, 'intro.png')
INTRO_AUDIO = os.path.join(AUDIO_DIR, 'intro.wav')

WATERMARK_POS = { 'x': 1540, 'y': 1015 }

CREATE_INTRO = True  # from image and audio file

INTRO_FILE = os.path.join(VIDEO_INTRO_DIR, 'intro.mp4')
OUTPUT_FILE = 'out.mp4'
