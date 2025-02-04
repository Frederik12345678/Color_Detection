import math



def rgb_to_hsl(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    max_val, min_val = max(r, g, b), min(r, g, b)
    l = (max_val + min_val) / 2

    if max_val == min_val:
        h = s = 0  # achromatic
    else:
        d = max_val - min_val
        s = d / (2 - max_val - min_val) if l > 0.5 else d / (max_val + min_val)

        if max_val == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_val == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4

        h /= 6

    return h, s, l


def rgb_to_hue(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    max_val, min_val = max(r, g, b), min(r, g, b)
    d = max_val - min_val

    if d == 0:
        h = 0  # Achromatic (gray)
    elif max_val == r:
        h = (g - b) / d % 6
    elif max_val == g:
        h = (b - r) / d + 2
    else:  # max_val == b
        h = (r - g) / d + 4

    h = (h * 60) % 360  # Convert to degrees

    return h

def rgb_to_hsv_saturation(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    max_val, min_val = max(r, g, b), min(r, g, b)
    v = max_val  # HSV.V (Value)
    d = max_val - min_val

    s = 0 if v == 0 else (d / v) * 100  # Convert to percentage

    return s



def crop_center(image, crop_size=(80, 80)):
    h, w = image.shape[:2]
    crop_h, crop_w = crop_size

    # Calculate the center coordinates
    start_x = (w - crop_w) // 2
    start_y = (h - crop_h) // 2

    # Crop the image
    cropped_image = image[start_y:start_y + crop_h, start_x:start_x + crop_w]
    
    return cropped_image