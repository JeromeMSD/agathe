# agathe
[![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](python.org)

Small python script to calculate white pixels proportion in an image from a black and a white reference images.

## Requirements

> [!WARNING]
> You need **python3** and **pip** to run this script.
> 
> You can install pip with `python3 -m ensurepip --upgrade` or `sudo apt install python3-pip`

```bash
pip install cv2
pip install numpy
```

## Use

The script compare using two methods : 

* Basic comparison where threshold is `127`.
* Comparison where each image are preprocess using `cv2.threshold()` function.
  ```python
  (retVal, newInput) = cv2.threshold(input_image, 130, 255, cv2.THRESH_BINARY)
  (retVal, newBlack) = cv2.threshold(black_reference, 130, 255, cv2.THRESH_BINARY)
  (retVal, newWhite) = cv2.threshold(white_reference, 130, 255, cv2.THRESH_BINARY)
  ```
> [!NOTE]
> Images will be displayed before the proportion calculation, press `space` to close each of them.

### Compare your own images

Using path to images (`input`, `black reference` and `white reference`).
```bash
python3 agathe.py <path-to-image-to-test> <path-to-black-reference-image> <path-to-white-reference-image>
```

---

### Default mode

There is three images in this repostory to test the script. To use them you can use the `default` mode

```sh
python3 agathe.py default
```

**default mode's result**
```sh
Use default configuration...

white pixels:
 input: 119634, white_ref: 656610, black_ref: 3004

White pixels proportion: 17.844083438646525%

white pixels:
 input: 113566, white_ref: 642682, black_ref: 2925

White pixels proportion (using threshold): 17.294222650162485%
```
