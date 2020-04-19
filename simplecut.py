#!/usr/bin/env python3

import ffmpeg
import argparse

parser = argparse.ArgumentParser(description='Cut a video file')
parser.add_argument('-i', action='store', dest='in_file')
parser.add_argument('-o', action='store', dest='out_file')
parser.add_argument('-s', action='store', dest='start_time', type=int)
parser.add_argument('-d', action='store', dest='duration', type=int)

def trim(in_file, out_file, start_time, duration):
    in_file = ffmpeg.input(in_file)
    (
        ffmpeg
        .trim(
            in_file, 
            start=start_time,
            duration=duration
        )
        .output(out_file)
        .run(quiet=True)
    )

args = parser.parse_args()
trim(args.in_file, args.out_file, args.start_time, args.duration)

