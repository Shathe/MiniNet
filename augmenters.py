from imgaug import augmenters as iaa
import imgaug as ia
import cv2
import random



def get_augmenter(name, c_val=255, vertical_flip=True):
    if name:
        alot = lambda aug: iaa.Sometimes(0.75, aug)
        alw = lambda aug: iaa.Sometimes(1, aug)
        sometimes = lambda aug: iaa.Sometimes(0.3, aug)
        few = lambda aug: iaa.Sometimes(0.10, aug)

        if 'classification' in name:
            scale = random.uniform(0.87, 1.25)

            seq_rgb = iaa.Sequential([

                iaa.Fliplr(0.50),  # horizontally flip 50% of the images
                iaa.Flipud(0.05),  # vertically flip 50% of the images
                sometimes(iaa.Add((-10, 10))),
                sometimes(iaa.Multiply((0.95, 1.10), per_channel=False)),
                sometimes(iaa.GaussianBlur(sigma=(0, 0.10))),
                sometimes(iaa.ContrastNormalization((0.90, 1.15))),
                alot(iaa.Affine(
                    scale={"x": (scale), "y": (scale)},
                    # scale images to 80-120% of their size, individually per axis
                    translate_percent={"x": (-0.25, 0.25), "y": (-0.2, 0.20)},
                    # translate by -20 to +20 percent (per axis)
                    rotate=(-20, 20),  # rotate by -45 to +45 degrees
                    order=1,  #bilinear interpolation (fast)
                    cval=0,
                    mode="reflect" # `edge`, `wrap`, `reflect` or `symmetric`
                    # cval=(0, 255),  # if mode is constant, use a cval between 0 and 255
                    # mode=ia.ALL  # use any of scikit-image's warping modes (see 2nd image from the top for examples)
                ))])
            return seq_rgb

        if 'segmentation' in name:
            value_flip = round(random.random())
            if value_flip>0.5:
                value_flip=1
            else:
                value_flip=0

            value_flip2 = round(random.random())
            if value_flip2>0.5:
                value_flip2=1
            else:
                value_flip2=0



            value_add = int(random.uniform(-12,12))
            value_Multiply = random.uniform(0.97, 1.05)
            value_GaussianBlur = random.uniform(0.0,0.10)
            ContrastNormalization = random.uniform(0.93, 1.13)
            scale = random.uniform(0.50,2)
            value_x2 = random.uniform(-0.3, 0.3)
            value_y2 = random.uniform(-0.10, 0.10)
            val_rotate = random.uniform(-5,5)


            seq_image = iaa.Sequential([
                iaa.Fliplr(value_flip),  # horizontally flip 50% of the images
                # iaa.Flipud(value_flip2),  # vertically flip 50% of the images
                iaa.Affine(
                    scale={"x": (scale), "y": (scale)},
                    # scale images to 80-120% of their size, individually per axis
                    translate_percent={"x": (value_x2), "y": (value_y2)},
                    # translate by -20 to +20 percent (per axis)
                    #rotate=(val_rotate),  # rotate by -45 to +45 degrees
                    order=1,  #bilinear interpolation (fast)
                    cval=c_val,
                    mode="reflect",

                    # `edge`, `wrap`, `reflect` or `symmetric`
                    # cval=c_val,  # if mode is constant, use a cval between 0 and 255
                    # mode=ia.ALL  # use any of scikit-image's warping modes (see 2nd image from the top for examples)

                )])


            seq_image2 = iaa.Sequential([
                sometimes(iaa.Add(value_add)),
                # sometimes(iaa.Multiply(value_Multiply, per_channel=False)),
                sometimes(iaa.GaussianBlur(sigma=(value_GaussianBlur, value_GaussianBlur))),
                sometimes(iaa.ContrastNormalization(ContrastNormalization))])



            seq_label = iaa.Sequential([
                iaa.Fliplr(value_flip),  # horizontally flip 50% of the images
                # iaa.Flipud(value_flip2),  # vertically flip 50% of the images
                iaa.Affine(
                    scale={"x": (scale), "y": (scale)},
                    # scale images to 80-120% of their size, individually per axis
                    translate_percent={"x": (value_x2), "y": (value_y2)},
                    # translate by -20 to +20 percent (per axis)
                    #rotate=(val_rotate),  # rotate by -45 to +45 degrees
                    order=0,  #bilinear interpolation (fast)
                    cval=c_val,
                    mode="constant" # `edge`, `wrap`, `reflect` or `symmetric`
                    # cval=(0, 255),  # if mode is constant, use a cval between 0 and 255
                    # mode=ia.ALL  # use any of scikit-image's warping modes (see 2nd image from the top for examples)
                )])



            seq_mask = iaa.Sequential([
                iaa.Fliplr(value_flip),  # horizontally flip 50% of the images
                # iaa.Flipud(value_flip2),  # vertically flip 50% of the images
                iaa.Affine(
                    scale={"x": (scale), "y": (scale)},
                    # scale images to 80-120% of their size, individually per axis
                    translate_percent={"x": (value_x2), "y": (value_y2)},
                    # translate by -20 to +20 percent (per axis)
                    #rotate=(val_rotate),  # rotate by -45 to +45 degrees
                    order=0,  #bilinear interpolation (fast)
                    cval=0,
                    mode="constant" # `edge`, `wrap`, `reflect` or `symmetric`
                    # cval=c_val,  # if mode is constant, use a cval between 0 and 255
                    # mode=ia.ALL  # use any of scikit-image's warping modes (see 2nd image from the top for examples)
                )])


            return seq_image2,  seq_image, seq_label, seq_mask

    else:
        return None
