"""
Initializes a dynip environment.  Creates batch scripts and config files.
"""
import sys
import os
import shutil
import argparse

def main():
    """
    Main entry point of init for console

    Expents sys.arg[1] to be the path to place the template files
    """

    parser = argparse.ArgumentParser(description='Set up configuration for a DynIP client/server pair')
    parser.add_argument('path', metavar='path', type=str, nargs=1,
            help='The path to store the DynIP configuration files')
    args = parser.parse_args()
    
    # Determine the path to this script
    this_dir, this_filename = os.path.split(__file__)

    # Copy example.conf from this folder to the target path
    source_path = os.path.join(this_dir, 'example.conf')
    target_path = args.path[0]
    print("Copying from {0} to {1}".format(source_path, target_path))
    shutil.copy2(source_path, target_path)


if __name__ == "__main__":
    sys.exit(main())
