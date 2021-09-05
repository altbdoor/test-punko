# test-punko

Small test on generating something something punko, because I am interested in the programming logic that goes behind it.

### Setup

1. Please install [Python 3.x](https://www.python.org/)
    1. Make sure "Add Python to PATH" is checked!
    1. You can check if Python is correctly installed by opening a CMD, and issuing `python --version`
1. Clone the project, or download the ZIP of the project
1. `cd` to the project path
1. Setup the [virtual environment](https://docs.python.org/3/tutorial/venv.html) for the project
    1. Run `python -m venv venv`
        1. Still new to this `venv` stuff, so I used `venv` since its the standard name, feel free to change it, e.g., `python -m venv nice-folder-name`
    1. Activate the virtual environment
        1. Windows: `venv\Scripts\activate.bat`
        1. Unix/MacOS: `source venv/bin/activate`
1. Install the dependencies with `pip install -r requirements.txt`
1. Run the script with `python generate.py`
1. The generated images will be in `dist/` folder

### Credits

- Original base images and CSV from https://github.com/cryptopunksnotdead/punks.starter

### Arguments

```
$ python generate.py --help | fold -sw 80
usage: generate.py [-h] [--csv_path CSV_PATH] [--images_path IMAGES_PATH]
                   [--dist_path DIST_PATH] [--extra_size EXTRA_SIZE]

Compiles PNG images with layers specified in a CSV file. Somewhat suitable for
generating pixel art punko.

optional arguments:
  -h, --help            show this help message and exit
  --csv_path CSV_PATH   Path to source CSV file. Defaults to "./source.csv".
  --images_path IMAGES_PATH
                        Path to the directory containing the images. Defaults
to "./images/".
  --dist_path DIST_PATH
                        Path to the directory where the generated images will
be saved. Will be automatically created if it does not exist. Defaults to
"./dist/".
  --extra_size EXTRA_SIZE
                        The factor that an extra, generated image should be
enlarged by. Usually the generated images are small, and another 2x or 4x
larger image helps to see things better. A factor of 0 disables generating the
extra image. Defaults to 0.
```

### Going further

- You can mix and match attributes in `source.csv`, or even add more attributes. Make sure the CSV headers are properly updated too.
- You can make your own images. As long as the CSV names map correctly to the images in `images/`, it will work.
- Go bigger, maybe 48px, 96px.
