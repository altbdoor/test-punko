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

### Going further

- You can mix and match attributes in `source.csv`, or even add more attributes. Make sure the CSV headers are properly updated too.
- You can make your own images. As long as the CSV names map correctly to the images in `images/`, it will work.
- Go bigger, maybe 48px, 96px.
