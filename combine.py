import ffmpeg
import os
from pathlib import Path
from config import *

def get_video_paths(dirname):
    paths_sorted = sorted((x for x in Path(dirname).iterdir() if not x.is_dir()), key=os.path.getmtime)
    return list(map(str, paths_sorted))

def create_intro():
    intro_image = ffmpeg.input(INTRO_IMAGE, f='image2', loop=1)
    intro_audio = ffmpeg.input(INTRO_AUDIO)

    out = ffmpeg.output(intro_image, intro_audio, INTRO_FILE, shortest=None, vcodec='libx264', acodec='aac', preset='medium')
    #print(out.compile())
    out.run(overwrite_output=True)

def join_video():
    paths = get_video_paths(VIDEO_SRC_DIR)

    if ADD_ADS_VIDEO:
        paths += get_video_paths(VIDEO_ADS_DIR)
    
    if ADD_END_VIDEO:
        paths += get_video_paths(VIDEO_END_DIR)
        
    streams = [ffmpeg.input(path) for path in paths]
    streams.insert(0, ffmpeg.input(INTRO_FILE))

    overlay_file = ffmpeg.input(WATERMARK_FILENAME)

    streams_av = []

    for s in streams:
        streams_av.append(s.video)
        streams_av.append(s.audio.filter("volume", VOLUME_INCREASE))

    (
        ffmpeg
        .concat(*streams_av, v=1, a=1)
        .overlay(overlay_file, **WATERMARK_POS)
        .output(OUTPUT_FILE, vsync=0, preset='faster')
        .run(overwrite_output=True)
    )

def main():
    if CREATE_INTRO:
        create_intro()

    join_video()

if __name__ == "__main__":
    main()