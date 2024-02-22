import cv2
import numpy as np
import sys

class textcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def find_white_proportion(image_path, black_reference_path, white_reference_path):
    # Load images
    input_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    black_reference = cv2.imread(black_reference_path, cv2.IMREAD_GRAYSCALE)
    white_reference = cv2.imread(white_reference_path, cv2.IMREAD_GRAYSCALE)

    cv2.imshow("Input", input_image)
    cv2.waitKey(0)
    cv2.imshow("Black Ref.", black_reference)
    cv2.waitKey(0)
    cv2.imshow("White Ref.", white_reference)
    cv2.waitKey(0)

    prop_input = np.sum(input_image > 127)
    prop_white = np.sum(white_reference > 127)
    prop_black = np.sum(black_reference > 127)

    print(f"white pixels:\n input: {prop_input}, white_ref: {prop_white}, black_ref: {prop_black}\n")

    return (( prop_input - prop_black ) * 100 ) / (prop_white - prop_black)

def find_white_proportion_using_threshold(image_path, black_reference_path, white_reference_path):
    # Load images
    input_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    black_reference = cv2.imread(black_reference_path, cv2.IMREAD_GRAYSCALE)
    white_reference = cv2.imread(white_reference_path, cv2.IMREAD_GRAYSCALE)

    (retVal, newInput) = cv2.threshold(input_image, 130, 255, cv2.THRESH_BINARY)
    (retVal, newBlack) = cv2.threshold(black_reference, 130, 255, cv2.THRESH_BINARY)
    (retVal, newWhite) = cv2.threshold(white_reference, 130, 255, cv2.THRESH_BINARY)

    cv2.imshow("test Ref.", newInput)
    cv2.waitKey(0)
    cv2.imshow("test Ref.", newBlack)
    cv2.waitKey(0)
    cv2.imshow("test Ref.", newWhite)
    cv2.waitKey(0)

    prop_input = np.sum(newInput > 127)
    prop_white = np.sum(newWhite > 127)
    prop_black = np.sum(newBlack > 127)

    print(f"white pixels:\n input: {prop_input}, white_ref: {prop_white}, black_ref: {prop_black}\n")

    return (( prop_input - prop_black ) * 100 ) / (prop_white - prop_black)


if __name__ == '__main__':
    if len(sys.argv) != 4 and len(sys.argv) != 2:
        print("\n--------------------------\n Wrong number of argument\n--------------------------\n\nuse: \n\n python3 agathe.py <path-to-image-to-test> <path-to-black-reference-image> <path-to-white-reference-image> \n\nor use default configuration with: \n\n python3 agathe.py default")
        exit(1)

    if len(sys.argv) == 2 and sys.argv[1] != 'default':
        print("\n--------------------------\n Wrong default argument\n--------------------------\n\nuse:\n\n python3 agathe.py default")
        exit(1)

    if sys.argv[1] == 'default':
        # Default usage
        print("Use default configuration...\n")
        image_path = 'input_image.jpg'
        black_reference_path = 'black_reference.jpg'
        white_reference_path = 'white_reference.jpg'
    else: 
        image_path = sys.argv[1]
        black_reference_path = sys.argv[2]
        white_reference_path = sys.argv[3]
    
    white_proportion = find_white_proportion(image_path, black_reference_path, white_reference_path)
    result_color=textcolors.OKGREEN
    if white_proportion > 10.0:
        result_color=textcolors.WARNING
        if white_proportion > 30.0:
            result_color=textcolors.FAIL
    print(f"{result_color}White pixels proportion: {textcolors.BOLD}{white_proportion}%\033[0m\n")
    

    white_proportion = find_white_proportion_using_threshold(image_path, black_reference_path, white_reference_path)
    result_color=textcolors.OKGREEN
    if white_proportion > 10.0:
        result_color=textcolors.WARNING
        if white_proportion > 30.0:
            result_color=textcolors.FAIL
    print(f"{result_color}White pixels proportion (using threshold): {textcolors.BOLD}{white_proportion}%\033[0m\n")
