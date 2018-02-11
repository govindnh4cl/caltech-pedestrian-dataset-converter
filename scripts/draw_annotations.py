from __future__ import print_function
import os
import re
import json
import glob
import cv2 as cv
from collections import defaultdict

from config import Config

"""
This script dumps the labeled video to disk.
The images and annotatios must have already been extracted (using
convert_seqs.py and convert_annotations.py before running this)
"""
if __name__ == '__main__':
    cfg = Config()

    # Read annotations from json file
    ann_file = os.path.join(cfg.dst_base_dir, cfg.dst_ann_file)
    annotations = json.load(open(ann_file))

    out_dir = os.path.join(cfg.dst_base_dir, cfg.video_dump_dir)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)


    img_fns = defaultdict(dict)
    all_bboxes = 0
    for set_name in sorted(cfg.sets):
        set_dir = os.path.join(cfg.dst_base_dir, set_name)

        if not os.path.exists(set_dir):
            print('Didn\'t find input images in set: {:s}. Skipping video dump of this set'.format(set_dir))
            continue

        if set_name not in annotations.keys():
            print('Warning: Annotations for Set: {:s} not found in {:s}. Skipping video dump of this set'.
                  format(set_name, ann_file))
            continue

        for video_name in sorted(os.listdir(set_dir)):
            n_bboxs = 0
            n_frames = 0
            out_video = os.path.join(out_dir, '{:s}_{:s}.avi'.format(set_name, video_name))
            print('Writing video: {:s} '.format(out_video), end='')
            wri = cv.VideoWriter(out_video,
                cv.VideoWriter_fourcc(*'XVID'), 30, (640, 480))

            vid_dir = os.path.join(set_dir, video_name)
            img_names = sorted(os.listdir(vid_dir), key=lambda x: int(x.split('.')[0]))

            for img_name in img_names:  # Loop over all frames
                img_path = os.path.join(vid_dir, img_name)
                if not os.path.exists(img_path):
                    print('Warning: Image: {:s} does not exist. Skipping.'.format(img_path))
                    continue

                ann_idx = int(img_name.split('.')[0]) - 1  # Annotations indices start at 0
                img = cv.imread(img_path)
                if img is not None:
                    if str(ann_idx) in annotations[set_name][video_name]['frames']:
                        data = annotations[set_name][video_name]['frames'][str(ann_idx)]
                        for datum in data:
                            x, y, w, h = [int(v) for v in datum['pos']]
                            cv.rectangle(img, (x, y), (x + w, y + h), cfg.bbox_color, 1)
                            n_bboxs += 1
                    wri.write(img)
                else:
                    print('Warning: OpenCV couldn\'t read Image: {:s}. Skipping this frame.'.format(img_path))
                    continue

                n_frames += 1

            wri.release()
            all_bboxes += n_bboxs
            print('Set: {:s} Video: {:s} #Frames: {:d} #Bboxes: {:d}'.format(set_name, video_name, n_frames, n_bboxs))

    print('Total #Bbooxes: {:d}', all_bboxes)
