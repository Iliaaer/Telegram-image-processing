import rawpy
import imageio

img = '3.dng'
raw = rawpy.imread(img)

rgb = raw.postprocess()
imageio.imsave('rgb2/default.jpg', rgb)
'''
https://letmaik.github.io/rawpy/api/
https://letmaik.github.io/rawpy/api/rawpy.Params.html#rawpy.Params
_init__(self, demosaic_algorithm=None, half_size=False, four_color_rgb=False, dcb_iterations=0, dcb_enhance=False, 
        fbdd_noise_reduction=None, noise_thr=None, median_filter_passes=0, use_camera_wb=False, use_auto_wb=False, 
        user_wb=None, output_color=None, output_bps=8, user_flip=None, user_black=None, user_sat=None, no_auto_bright=False, 
        auto_bright_thr=None, adjust_maximum_thr=0.75, bright=1.0, highlight_mode=None, exp_shift=None, exp_preserve_highlights=0.0, 
        no_auto_scale=False, gamma=None, chromatic_aberration=None, bad_pixels_path=None): # real signature unknown; restored from __doc__

Params.__init__(self, demosaic_algorithm=None, half_size=False, four_color_rgb=False, dcb_iterations=0,
                dcb_enhance=False, fbdd_noise_reduction=FBDDNoiseReductionMode.Off, noise_thr=None,
                median_filter_passes=0, use_camera_wb=False, use_auto_wb=False, user_wb=None,
                output_color=ColorSpace.sRGB, output_bps=8, user_flip=None, user_black=None, user_sat=None,
                no_auto_bright=False, auto_bright_thr=None, adjust_maximum_thr=0.75, bright=1.0,
                highlight_mode=HighlightMode.Clip, exp_shift=None, exp_preserve_highlights=0.0, no_auto_scale=False,
                gamma=None, chromatic_aberration=None, bad_pixels_path=None)
'''
# rgb = raw.postprocess(use_auto_wb=True)
# imageio.imsave('rgb2/default_use_auto_wb.jpg', rgb)
#
# rgb = raw.postprocess(use_camera_wb=True)
# imageio.imsave('rgb2/default_use_camera_wb.jpg', rgb)
#
# rgb = raw.postprocess(half_size=True)
# imageio.imsave('rgb2/default_half_size.jpg', rgb)
#
# rgb = raw.postprocess(four_color_rgb=True)
# imageio.imsave('rgb2/default_four_color_rgb.jpg', rgb)
#
# rgb = raw.postprocess(dcb_iterations=4)
# imageio.imsave('rgb2/default_dcb_iterations.jpg', rgb)
#
# rgb = raw.postprocess(dcb_enhance=True)
# imageio.imsave('rgb2/default_dcb_enhance.jpg', rgb)
#
# rgb = raw.postprocess(noise_thr=7.15)
# imageio.imsave('rgb2/default_noise_thr.jpg', rgb)
#
# rgb = raw.postprocess(median_filter_passes=13)
# imageio.imsave('rgb2/default_median_filter_passes.jpg', rgb)
#
# rgb = raw.postprocess(user_wb=[1, 1.25, 3.7, 5.75])
# imageio.imsave('rgb2/default_user_wb.jpg', rgb)
#
# rgb = raw.postprocess(output_bps=16)
# imageio.imsave('rgb2/default_output_bps16.jpg', rgb)
#
# rgb = raw.postprocess(user_black=-2)
# imageio.imsave('rgb2/default_user_black.jpg', rgb)
#
# rgb = raw.postprocess(user_sat=-2)
# imageio.imsave('rgb2/default_user_sat.jpg', rgb)
#
# rgb = raw.postprocess(no_auto_scale=True)
# imageio.imsave('rgb2/default_no_auto_scale.jpg', rgb)
#
# rgb = raw.postprocess(no_auto_bright=True)
# imageio.imsave('rgb2/default_no_auto_bright.jpg', rgb)
#
# rgb = raw.postprocess(auto_bright_thr=-0.2)
# imageio.imsave('rgb2/default_auto_bright_thr.jpg', rgb)
#
# rgb = raw.postprocess(adjust_maximum_thr=0.75)
# imageio.imsave('rgb2/default_adjust_maximum_thr.jpg', rgb)
#
# rgb = raw.postprocess(bright=0.75)
# imageio.imsave('rgb2/default_bright.jpg', rgb)
#
# rgb = raw.postprocess(exp_shift=0.75)
# imageio.imsave('rgb2/default_exp_shift.jpg', rgb)
#
# rgb = raw.postprocess(exp_preserve_highlights=0.75)
# imageio.imsave('rgb2/default_exp_preserve_highlights.jpg', rgb)



print('finish')