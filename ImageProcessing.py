import rawpy
import imageio

def image_processing(raw, name, temp):
    rgb = raw.postprocess(use_auto_wb=True)
    imageio.imsave('photo/' + name + str(temp) + '.jpg', rgb)
    return rgb

