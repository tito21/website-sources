import argparse

class DefaultArguments(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="Yet another static site generator",
                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        self.add_argument('--draft', action='store_true',
                          help="Include posts with the draft tag")
        self.add_argument('--serve', action='store_true',
                          help="Locally serve generated site on port 8000")
        self.add_argument('--site-root', default=None, type=str,
                          help="Name of the site (overwrites settings in \
                                `config.yml`). If option `--serve` is passed \
                                this option has no effect")