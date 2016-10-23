# USAGE: python index.py --dataset dataset --index index.csv
from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2


if __name__ == '__main__':
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-d", "--dataset", required = False, default='../frames',
                help = "Path to the directory that contains the images to be indexed")
        ap.add_argument("-i", "--index", required = False, default='index_color_hist.csv',
                help = "Path to where the computed index will be stored")
        args = vars(ap.parse_args())

        # initialize the color descriptor
        cd = ColorDescriptor((8, 12, 3))

        # open the output index file for writing
        output = open(args["index"], "w")

                # use glob to grab the image paths and loop over them
        for imagePath in glob.glob("frames/*.jpg"):
                # extract the image ID (i.e. the unique filename) from the image
                # path and load the image itself
                imageID = imagePath[7:]
                image = cv2.imread(imagePath)
                if image== None:
                        continue
                # describe the image
                features = cd.describe(image)

                # write the features to file
                features = [str(f) for f in features]
                output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()


# # Go to /../ImageData/train/train_text_tags.txt
# train_tags_path = os.path.join(os.path.dirname(__file__), "..", "ImageData", "train", FILE_TRAIN_INDEX)
