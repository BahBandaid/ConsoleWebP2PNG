from PIL import Image
import os
fp = input("Enter directory to convert: ")
for file_item in os.listdir(fp):
    if ".webp" in file_item:
        final_path = "{0}\\{1}".format(fp, file_item)
        im = Image.open(final_path).convert("RGB")
        im.save(final_path.replace(".webp", ".png"), "png")