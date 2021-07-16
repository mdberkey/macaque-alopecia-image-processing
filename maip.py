import os
from PIL import Image, ImageOps, ImageEnhance


def get_image_paths(img_dir=os.path.join('images', 'input')):
    """
    Gets the path of every image in the directory
    :param img_dir: directory of images
    :return: list of image paths
    """
    img_paths = []
    for img in os.listdir(img_dir):
        img_paths.append(os.path.join(img_dir, img))

    return img_paths

def convert_to_png(img):
    return img.putalpha(255)

def greyscale_image(img):
    return ImageOps.grayscale(img)


def contrast_image(img, factor):
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(factor)
    return img


def threshold_crop_image(img):
    thresh = img.point(lambda p: p < 130 and 225)
    box = thresh.getbbox()
    print(box)
    #crop = thresh.crop(box)
    img = img.crop(box)
    return img



if __name__ == '__main__':
    img_paths = get_image_paths()
    for path in reversed(img_paths):
        img = Image.open(path)
        png = convert_to_png(img)
        img = greyscale_image(img)
        img = contrast_image(img, 2.5)
        img = threshold_crop_image(img)
        img.show()
        img.close()
        break

