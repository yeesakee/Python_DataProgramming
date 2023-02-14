# Name: Yeesa Kee, UWnetid: yeesakee
# Section: AE
# This program solves 3 problems give in Homework 3
# This includes inverting an image's colors, blurring an image by a given
# amount, and storing similarity between two images

import numpy as np


def invert_colors(img):
    """
    Returns a new numpy array with the colors of the given image inverted.

    Takes a 3-d numpy array
    """
    result = img.copy()
    result[:, :, 0] = 255 - img[:, :, 0]
    result[:, :, 1] = 255 - img[:, :, 1]
    result[:, :, 2] = 255 - img[:, :, 2]
    return result


def blur(img, size):
    """
    Returns a 2-d numpy array that represents a blurred version of the given
    image.

    Takes a 2-d numpy array and a patch size that determines how much the
    given image will be blurred.
    """
    height, width = img.shape
    result_height = height + 1 - size
    result_width = width + 1 - size
    result = np.zeros((result_height, result_width))

    for i in range(result_height):
        for j in range(result_width):
            curr = img[i:i+size, j:j+size]
            result[i, j] = np.mean(curr)
    return result.astype(np.uint8)


def template_match(img, template):
    """
    Returns a 2-d numpy array that stores the similarity between
    the two images given.
    """
    height, width = img.shape
    t_height, t_width = template.shape
    result_height = height + 1 - t_height
    result_width = width + 1 - t_width
    result = np.zeros((result_height, result_width))
    temp_total = template[:, :]
    temp_mean = np.mean(temp_total)

    for i in range(result_height):
        for j in range(result_width):
            img_total = img[i:i+t_height, j:j+t_width]
            img_mean = np.mean(img_total)
            result[i, j] = np.sum((img_total - img_mean) *
                                  (temp_total - temp_mean))
    return result
