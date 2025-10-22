from visualizer_module import Visualizer
import os

dir_output = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output'))
dir_imgs = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'imgs'))
json_file = os.path.join(dir_output,"image_cleaned_test.json")
img_file = os.path.join(dir_imgs,"12_50_vero_09.tif")

# initialize object
img = Visualizer(json_file, img_file)
# load metadata
img.load_metadata()
# print extracted feactures
img.print_features()
# plot the image
i = img.plot_image()

