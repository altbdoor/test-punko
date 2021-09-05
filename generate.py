#!/bin/usr/env python

import argparse
import csv
from pathlib import Path
from PIL import Image


# a function to convert the name inside csv to the filenames. seems to be
# a basic lowercase and space strip conversion.
def csv_name_to_filename(name: str) -> str:
    name = name.lower()
    name = name.replace(" ", "")
    return name


def run_generate(csv_path: Path, images_path: Path, dist_path: Path, extra_size: int):
    with open(csv_path) as source_file:
        # read the source csv file
        csvr = csv.reader(source_file)

        # create the dist folder if it does not exist
        dist_path.mkdir(exist_ok=True)

        # iterate through the csv lines
        for line, row in enumerate(csvr):
            # the first line is ignored, since it is the header
            if line == 0:
                continue

            # get the base filename
            base = csv_name_to_filename(row[0])

            # get all the attributes for the base
            attr_list = [csv_name_to_filename(attr) for attr in row[1:]]

            print(f"Generating with [{base}] and, [{'], ['.join(attr_list)}]")

            # open the base image
            base_img = Image.open(images_path.joinpath(f"{base}.png"))

            # and if there are attributes, we paste the image on top of base
            # https://stackoverflow.com/a/5324782
            for attr in attr_list:
                attr_img = Image.open(images_path.joinpath(f"{attr}.png"))
                base_img.paste(attr_img, (0, 0), attr_img.convert("RGBA"))

            # save the image, and also an extra size
            base_img.save(dist_path.joinpath(f"{line:04}.png"))

            if extra_size > 0:
                base_img.resize(
                    (base_img.width * extra_size, base_img.height * extra_size),
                    Image.NEAREST,
                ).save(dist_path.joinpath(f"{line:04}_x{extra_size}.png"))


# ========================================


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Compiles PNG images with layers specified in a CSV file. "
            "Somewhat suitable for generating pixel art punko."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    def arg_check_path(path_type: str):
        def _check_path(text: str) -> Path:
            path = Path(text)

            if path_type == "dir" and path.exists() and path.is_dir():
                return path
            elif path_type == "file" and path.exists() and path.is_file():
                return path
            else:
                raise argparse.ArgumentTypeError(f"{text} is an invalid path")

        return _check_path

    parser.add_argument(
        "--csv_path",
        type=arg_check_path("file"),
        default="./source.csv",
        help=("Path to source CSV file. " 'Defaults to "./source.csv".'),
    )

    parser.add_argument(
        "--images_path",
        type=arg_check_path("dir"),
        default="./images/",
        help=(
            "Path to the directory containing the images. " 'Defaults to "./images/".'
        ),
    )

    def arg_check_dist(text: str) -> Path:
        return Path(text)

    parser.add_argument(
        "--dist_path",
        type=arg_check_dist,
        default="./dist/",
        help=(
            "Path to the directory where the generated images will be saved. "
            "Will be automatically created if it does not exist. "
            'Defaults to "./dist/".'
        ),
    )

    parser.add_argument(
        "--extra_size",
        type=int,
        default=0,
        help=(
            "The factor that an extra, generated image should be enlarged by. "
            "Usually the generated images are small, and another 2x or 4x larger image helps to see things better. "
            "A factor of 0 disables generating the extra image. "
            "Defaults to 0."
        ),
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    args = vars(args)

    run_generate(**args)
