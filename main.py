#from semmeta import json_cleaner_module,  metadata_extractor_module,  visualizer_module
from semmeta.metadata_extractor_module import SEMMetaData
#from metadata_extractor_module import SEMMetaData

image = "./imgs/LIL test_defect02.tif"
def main(image):
    test_extractor_module = SEMMetaData()
    img = test_extractor_module.OpenCheckImage(image)
    #
    image_metadata, image_tags= test_extractor_module.ImageMetadata(img)
    List = test_extractor_module.GetInsMetadata()
    semdict = test_extractor_module.InsMetaDict(List)
    # Write SEM Metadata to JSON File
    test_extractor_module.WriteSEMJson("./output/test_file.json", semdict)
    
    
        
if __name__ == "__main__":
    main(image)
