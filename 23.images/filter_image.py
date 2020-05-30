import argparse
import sys
from PIL import Image, ImageFilter

parser = argparse.ArgumentParser()

parser.add_argument('-i', "--image", required=True, type=str,
                    help='path to the image to be filtered')
parser.add_argument('-f', "--filter", required=True, type=str, choices=["BoxBlur", "GaussianBlur", "ModeFilter"],
                    help='type of filter to use (BoxBlur, GaussianBlur, ModeFilter)')
parser.add_argument('-r', "--radius", required=False, type=int,
                    help='blur radius, default 1 for BoxBlur, 2 for GaussianBlur, and 3 for ModeFilter')

args = parser.parse_args()

img = Image.open(args.image)
if args.filter == "BoxBlur":
    if args.radius is None:
        img.filter(ImageFilter.BoxBlur(1)).show()
    else:
        img.filter(ImageFilter.BoxBlur(args.radius)).show()

elif args.filter == "GaussianBlur":
    if args.radius is None:
        img.filter(ImageFilter.GaussianBlur()).show()
    else:
        img.filter(ImageFilter.GaussianBlur(args.radius)).show()

elif args.filter == "ModeFilter":
    if args.radius is None:
        img.filter(ImageFilter.ModeFilter()).show()
    else:
        img.filter(ImageFilter.ModeFilter(args.radius)).show()
        
else:
    print("There is no such filter")
    img.show()
