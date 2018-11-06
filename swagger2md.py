#!/usr/bin/env python3

# Author : Joachim Kruithof

import sys

from swagger2md.swagger_to_dict import sw_to_md

def main():

    file_in = sys.argv[1]
    file_out = sys.argv[2]

    sw_to_md(file_in, file_out)


if __name__ == "__main__":
    main()
