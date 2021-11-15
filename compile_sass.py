#! /usr/bin/env python3.9
# coding: utf-8

import sys
import os
# pip install libsass
import sass


def compile_one(sass_path=None):
    """Compiles the sass file given into a css file using
    the same name"""
    with open(sass_path, "r") as sass_file:
        sass_code = sass_file.read()
    css_code = sass.compile(string=sass_code)
    css_path = sass_path[:-4]+"css"

    with open(css_path, "w") as css_file:
        css_file.write(css_code)
    print(f"compiled: {css_path}")


def compile_all(directory=None):
    """Compiles all the sass files in the given directory"""
    print(directory)
    sass_files = [
        f for f in os.listdir(directory) if os.path.isfile(
            os.path.join(directory, f)) and f.endswith('.sass')]
    for file in sass_files:
        compile_one(file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sass_path = sys.argv[1]
        compile_one(sass_path)
    if len(sys.argv) < 2:
        cwd = os.getcwd()
        compile_all(cwd)
