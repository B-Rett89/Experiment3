# Experiment3

A simple GUI for generating videos using AI. Supports text, image, or video prompts.
The application now uses [moviepy](https://zulko.github.io/moviepy/) to build
short clips directly from the provided content. For text prompts a video with
the text is generated. Images are converted into a short clip and optional text
overlays can be added to existing videos.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure `ffmpeg` is installed and available in your system path as
`moviepy` relies on it for encoding videos.

Run the application:

```bash
python video_generator.py
```

Select the desired input type and optionally provide a source file. Enter a
prompt to overlay on the video and specify an output filename. Generated videos
will be saved using the selected quality setting.

This has been tested on Windows and Linux.
