import os.path
import filetype
from file import File

class FileManager:
    def __init__(self, source_path, target_path):
        self.source_path = source_path
        self.target_path = target_path

    def is_source_exists(self):
        return os.path.exists(self.source_path)

    def is_target_exists(self):
        return os.path.exists(self.target_path)

    def create_target(self):
        os.mkdir(self.target_path)
            
    def get_all_images(self):
        images = []
        root_path_dirs = os.path.normpath(self.source_path).split(os.path.sep)
        
        for (dir_path, _, file_names) in os.walk(self.source_path):
            for file_name in file_names:
                
                full_path = os.path.join(dir_path,file_name)
                
                if(filetype.is_image(full_path)):
                    
                    image_path_dirs = os.path.normpath(dir_path).split(os.path.sep)
                    dirs = set(image_path_dirs) - set(root_path_dirs)        
                    
                    images.append(File(file_name, full_path,dirs))
        return images

    def save_image(self,image, file):
        file_name = os.path.splitext(file.file_name)[0]
        target_dir = os.path.join(self.target_path,*file.dirs)
        
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)

        image.save(os.path.join(target_dir, file_name + ".webp"))
        image.save(os.path.join(target_dir, file_name + ".png"))
