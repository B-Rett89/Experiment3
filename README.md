# Experiment3

A simple GUI application for generating short videos using AI. It accepts text,
image, or video prompts and relies on
[moviepy](https://zulko.github.io/moviepy/) to build clips directly from the
provided content. Text prompts are rendered into a video, images become short
clips, and optional text overlays can be added on top of existing videos.

## Setup

Install dependencies (Python 3.8 or later is recommended). The interface now uses
[QDarkStyle](https://github.com/ColinDuquesnoy/QDarkStyleSheet) to mimic the
look of Adobe applications:

```bash
pip install -r requirements.txt
```

Make sure [`ffmpeg`](https://ffmpeg.org/) is installed and available on your
system `PATH` as `moviepy` relies on it to encode videos.

Run the application:

```bash
python video_generator.py
```

Select the desired input type and optionally provide a source file. Enter a
prompt to overlay on the video and specify an output filename. Generated videos
are saved in the current working directory using the selected quality setting.

The window layout mirrors common Adobe video editors with a control panel on the
left and a preview panel on the right. A dark palette is applied automatically
for a professional look.

This application has been tested on Windows and Linux. Running it in a headless
environment may require additional Qt configuration such as installing the Qt
`xcb` plugin or setting `QT_QPA_PLATFORM=offscreen`.
