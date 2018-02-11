Caltech Pedestrian Dataset Converter
============================

# Requirements
(For extracting images from `.seq` files):
- Python 2.7 (Does not work with Python 3 for now)

(For parsing annotations from `.vbb` files)
- NumPy
- SciPy

(For creating videos with annotated pedestrians)
- OpenCV (with Python binding. Install using `pip install opencv-python`)

# Directory Structure
Have a based_dir with all unzipped files like this:
* base_dir
  * set00
  * set01
    * V000.seq
    * V001.seq
    * ...
    * V005.seq
  * set02
  * ...
  * set09
  * annotations
    * set00
    * set01
      * V000.vbb
      * V001.vbb
      * ...
      * V005.vbb
    * set02
    * ...
    * set09  

# Usage
* Step 1: Modify the `config.py` for your needs. You'll need to set source and destination directory paths. In case you only want to extract a few sets and not all of them, it can also be set here.
* Step 2: Execute `python scripts/convert_seqs.py` to extract images from `.seq` files
* Step 3: Execute `python scripts/convert_annotations.py` to extract annotations from `.vbb` files to a `.json` file
* Step 4: Execute `python scripts/draw_annotations.py` to dump labeled videos

According to [the official site](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/), `set06`~`set10` are for test dataset, while the rest are for training dataset.

(Total Number of bounding boxes: 346621)


