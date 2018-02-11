from __future__ import print_function
import os

from config import Config


def open_save(cfg, set_name, indir, outdir, video_name):
    video_file = os.path.join(indir, video_name)
    with open(video_file,'rb') as f:  # read .seq file
        string = str(f.read())

    # split .seq file into segment with the image prefix
    splitstring = '\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46'
    strlist=string.split(splitstring)

    # deal with file segment, every segment is an image except the first one 
    # Skip the first one, which is filled with .seq header
    n_frames = 0
    for idx, img in enumerate(strlist[1:]):
        filename = str(idx + 1) + '.jpg' 
        filenamewithpath=os.path.join(outdir, video_name.split('.')[0], filename)
        if cfg.print_names_only:
            if (idx % cfg.interval) == 0:
                print(os.path.join(set_name, video_name.split('.')[0], filename.split('.')[0]))
        else:
            with open(filenamewithpath,'wb+') as i:
                print('\rWriting image: {:s}'.format(filenamewithpath), end='     ')
                i.write(splitstring + img)
                n_frames += 1

    if not cfg.print_names_only:
        print(' #Frames: {:d}'.format(n_frames))
    return

if __name__== '__main__':
    cfg = Config()

    for set_name in sorted(cfg.sets):
        set_in_dir = os.path.join(cfg.src_base_dir, set_name)
        if os.path.exists(set_in_dir):
            set_out_dir = os.path.join(cfg.dst_base_dir, set_name)
            if not os.path.exists(set_out_dir):
                os.mkdir(set_out_dir)
        else:
            print('Didn\'t find input directory: {:s} for input. Skipping this set.'.format(set_in_dir))
            continue

        for video_name in sorted(os.listdir(set_in_dir)):
            if video_name.endswith(".seq"):
                video_out_dir = os.path.join(set_out_dir, video_name.split('.')[0])
                if not os.path.exists(video_out_dir):
                    os.mkdir(video_out_dir)
                open_save(cfg, set_name, set_in_dir, set_out_dir, video_name)

