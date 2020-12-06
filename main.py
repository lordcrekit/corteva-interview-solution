#!python


import argparse
from   src.converter import converter


def main():
    '''
    Main method, executes program
    '''

    def get_args():
        '''
        Gets arguments from commandline.

        Arguments consist of input sources, output destination, and missed files (error) destination.
        '''
        parser = argparse.ArgumentParser(description='Convert users from csv to json format, as described by schema.')
        parser.add_argument('--input',  nargs='+', required=True,               help='One or more csv files of users.')
        parser.add_argument('--output',            required=True,               help='Output file destination.')
        parser.add_argument('--missed',                           default=None, help='Directory for any missed values.')

        return parser.parse_args()

    args = get_args()
    conv = converter()
    conv.convert(args.input, args.output, args.missed)


if __name__ == '__main__':
    main()
