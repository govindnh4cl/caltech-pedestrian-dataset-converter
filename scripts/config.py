import os

class Config():
    def __init__(self):
        #  ------ User configurable parameters START -----
        # A list of all sets to be parsed
        self.sets = ['set00', 'set01', 'set02', 'set03', 'set04',
                     'set05', 'set06', 'set07', 'set08', 'set09', 'set10']

        # sets = ['set00', 'set01', 'set02', 'set03', 'set04', 'set05'] #train
        # sets = ['set06', 'set07', 'set08','set09', 'set10'] #test

        # print_names_only: If set, does not write files on disk. Just prints their names on console.
        # Used for generating a file containing the names of images relative to the
        # base path(without extension, but includes prefix e.g. 'set01/V000/' )
        self.print_names_only = False  # Default: False

        # Make interval 1 if want to print all file names
        # Used for generating 1x, 10x training/test set for caltech dataset
        if self.print_names_only:
            self.interval = 30

        # src_base_dir should have unzipped 'set00', 'set01' .. 'set09' and 'annotations' directories
        self.src_base_dir = 'path/to/unzipped/dataset/sets'
        # dst_base_dir must exist. Should be empty
        self.dst_base_dir = 'path/to/where/you/want/output/sets'

        #  ------ User configurable parameters END -----

        self.src_ann_dir = 'annotations'
        self.dst_ann_file = 'annotations.json'  # Output annotation file name

        ## Video dump parameters.
        # Directory where labelled video will be written. Will be created.
        self.video_dump_dir = 'video_dump'
        self.bbox_color = (0, 0, 255)  # (B, G, R)

        if self._test_config() is False:
            print('Configuration Failed. Correct values set in config.py')

    def _test_config(self):
        """
        Tests the validity of configuration
        :return: True if success. Else False
        """
        if not os.path.exists(self.src_base_dir):
            print('Source dir: {:s} does not exist.'.format(self.src_base_dir))
            return False

        if not os.path.exists(self.dst_base_dir):
            print('Destination dir: {:s} does not exist.'.format(self.dst_base_dir))
            return False

        return True