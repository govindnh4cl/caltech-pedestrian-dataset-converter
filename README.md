Caltech Pedestrian Dataset Converter
============================

# Requirements
(For extracting images from .seq files):
- Python 2.7 (Does not work with Python 3 for now)

(For getting annotations from .vbb files)
- NumPy
- SciPy

(For creating videos with annotated pedestrians)
- OpenCV (with Python binding. Install using <pip install opencv-python>)

# Configure
There is a configurable section at the top of each python script that requires the directory paths to be set up. Please edit them before executing the scripts.

# Caltech Pedestrian Dataset

```
$ bash shells/download.sh  # Downloads dataset
$ python scripts/convert_annotations.py  # Converts annotations in .vbb format to a json file
$ python scripts/convert_seqs.py  # Convert images in .seq to .jpg
$ python tests/test_plot_annotations.py  # Draws annotations on images and writes video
```

Each `.seq` movie is separated into `.png` images. Each image's filename is consisted of `{set**}_{V***}_{frame_num}.png`. According to [the official site](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/), `set06`~`set10` are for test dataset, while the rest are for training dataset.

(Number of objects: 346621)

# Output
Example output: Inside target directory: ```target_directory/set00/V006/*.jpg```
  
# Draw Bounding Boxes
This may be broken as for now. Will be fixing it soon.

