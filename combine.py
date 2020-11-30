import ffmpeg
import os
from pathlib import Path
from config import *

def get_video_paths(dirname):
    paths_sorted = sorted(Path(dirname).iterdir(), key=os.path.getmtime)
    return map(str, paths_sorted)

def create_intro():
    intro_image = ffmpeg.input(os.path.join(IMAGES_DIR, INTRO_IMAGE), f='image2', loop=1)
    intro_audio = ffmpeg.input(os.path.join(AUDIO_DIR, INTRO_AUDIO))

    out = ffmpeg.output(intro_image, intro_audio, INTRO_FILE, shortest=None, vcodec='libx264', acodec='aac', preset='medium')
    #print(out.compile())
    out.run(overwrite_output=True)

def join_video():
    paths = get_video_paths(VIDEO_DIR)
    streams = [ffmpeg.input(path) for path in paths]
    streams.insert(0, ffmpeg.input(INTRO_FILE))

    overlay_file = ffmpeg.input(os.path.join(IMAGES_DIR, WATERMARK_FILENAME))

    streams_av = []

    for s in streams:
        streams_av.append(s.video)
        streams_av.append(s.audio.filter("volume", VOLUME_INCREASE))

    (
        ffmpeg
        .concat(*streams_av, v=1, a=1)
        .overlay(overlay_file, **WATERMARK_POS)
        .output(OUTPUT_FILE, vsync=2)
        .run(overwrite_output=True)
    )

def main():
    create_intro()
    join_video()

if __name__ == "__main__":
    main()