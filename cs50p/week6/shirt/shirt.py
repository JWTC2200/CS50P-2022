import sys
from os import path
from PIL import Image, ImageOps



def main():
    arguments = len(sys.argv)
    if arguments < 3:
        sys.exit("Too few command-line arguments")
    if arguments > 3:
        sys.exit("Too many command-line arguments")
    ext1 = (sys.argv[1].split("."))[1].lower()
    ext2 = (sys.argv[2].split("."))[1].lower()
    extensions = ("jpg", "jpeg", "png")

    if ext1 not in extensions:
        sys.exit("Invalid input")
    if ext2 not in extensions:
        sys.exit("Invalid output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    if not path.exists(sys.argv[1]):
        sys.exit("Input does not exist")

    muppet = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    newmuppet = ImageOps.fit(muppet, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    newmuppet.paste(shirt, box=None, mask=shirt)
    newmuppet.save(sys.argv[2])




if __name__ == "__main__":
    main()