import csv
import pathlib
from PIL import Image

# a function to convert the name inside csv to the filenames. seems to be
# a basic lowercase and space strip conversion.
def csv_name_to_filename(name: str) -> str:
    name = name.lower()
    name = name.replace(" ", "")
    return name


with open("source.csv") as source_file:
    # read the source csv file
    csvr = csv.reader(source_file)

    # create the dist folder if it does not exist
    pathlib.Path("./dist").mkdir(exist_ok=True)

    # we will need to save the max number of attributes
    max_attrs = 0

    # iterate through the csv lines
    for line, row in enumerate(csvr):
        # the first line is ignored, since it is the header
        if line == 0:
            max_attrs = len(row)
            continue

        base = csv_name_to_filename(row[0])
        attr_list = []

        # try to get all the attributes for the line
        for idx in range(1, max_attrs):
            if idx < len(row):
                attr_list.append(csv_name_to_filename(row[idx]))

        print(f"Generating with [{base}], [{'], ['.join(attr_list)}]")

        # open the base image
        base_img = Image.open(f"images/{base}.png")

        # and if there are attributes, we paste the image on top of base
        # https://stackoverflow.com/a/5324782
        for attr in attr_list:
            attr_img = Image.open(f"images/{attr}.png")
            base_img.paste(attr_img, (0, 0), attr_img.convert("RGBA"))

        # save the image, and also a 4x size, because 24px is so small
        base_img.save(f"dist/{line:04}.png")

        base_img.resize((base_img.width * 4, base_img.height * 4), Image.NEAREST).save(
            f"dist/{line:04}_x4.png"
        )
