import sys
from file_manager import FileManager
from image_converter import ImageConverter

print("Start image converter")

source_path = sys.argv[1]
target_path = sys.argv[2]
size = int(sys.argv[3])

print("Source path:" + source_path + " Target path: "+target_path+" Size: "+ str(size))

manager = FileManager(source_path, target_path)
converter = ImageConverter(size)

if(manager.is_source_exists()):
    if(not manager.is_target_exists()):
        
        manager.create_target()
        print("Target created")
        
    for image in manager.get_all_images():
         img = converter.open_image(image.full_path)
         
         converter.resize(img)
         manager.save_image(img, image)
else:
    print("Source not exists")
    
print("End image converter")