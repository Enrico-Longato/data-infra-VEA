#write a python class for extraction and visualization
#  AP_WD; AP_BEAM_TIME; AP_IMAGE_PIXEL_SIZE; AP_HOLDER_HEIGHT, AP_BEAM_CURRENT, AP_HOLDER_DIAMETER
import json
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class Visualizer():

    features = ['AP_WD', 
            'AP_BEAM_TIME', 
            'AP_IMAGE_PIXEL_SIZE', 
            'AP_HOLDER_HEIGHT', 
            'AP_BEAM_CURRENT', 
            'AP_HOLDER_DIAMETER']


    def __init__(self, json_file, image_file):
        self.json_file = json_file
        self.image_file = image_file


    def load_metadata(self):
        '''
        Load the metadata
        '''
        print(f"Loading metadata from file {self.json_file}")
        try:
            with open(self.json_file, 'r') as f:
                data = json.load(f)
                f.close()
        except:
            print(f"Could not read file: {self.json_file}")
            return
        
        self.metadata = data
    

    def print_features(self, features=features):
        '''
        Print the features from the loaded metadata
        '''
        
        if hasattr(self, 'metadata'):
            d = {f:self.metadata[f] for f in features}
            table = pd.DataFrame.from_dict(d, orient='index')
            print(table)
        else:
            raise Exception("No metadata loaded. Metadata must be load before")



    def plot_image(self, how='pillow'):
        '''
        Plots the image
        '''
        try:
            im = Image.open(self.image_file) 
        except:
            print(f"Could not read file: {self.image_file}")  
            return

        imarray = np.array(im) 
        if how=='pillow':
            im.show()
        elif how=='matplotlib':
            plt.imshow(imarray)
            plt.show()
        else:
            raise Exception("how must be either pillow or matplotlib")
        
    



