import rawpy
import imageio

save_file = 'Downloaded_file'
save_file_processing = 'Proccessing_file'

def image_processing(file_name):
    file_type = file_name[file_name.rindex('.'):]
    if not file_type == '.dng':
        return False
    raw = rawpy.imread(save_file + '/' + file_name)
    rgb = raw.postprocess(use_auto_wb=True)
    file_name = file_name[:file_name.rindex('.')]
    imageio.imsave(save_file_processing + '/' + file_name + '.jpg', rgb)
    return save_file_processing + '/' + file_name + '.jpg'
    

