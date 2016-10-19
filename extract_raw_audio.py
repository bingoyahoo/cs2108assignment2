#!/usr/bin/env python
"""
This script is used to extract the audio of the 3000 given microclips in the dataset.
The resultant .wav files are stored in the specified audio_storing_dir .
"""
from preprocessing.extract_audio import getAudioClip
from preprocessing.extract_frame import getKeyFrames
import argparse
import glob
import cv2
import os 
import cPickle as pickle

if __name__ == '__main__':
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-d", "--dataset", required = False, default="dataset_vine/vine/training/video/",
		help = "Path to the directory that contains the videos clips to be indexed")
	ap.add_argument("-a", "--audio_storing_dir", required = False, default="dataset_vine/vine/training/audio/",
		help = "Path to where the extracted audio will be stored")
	args = vars(ap.parse_args())
	error_file = open("errors.txt", "w")

	count = 0
	# Create folder
	try:
		os.makedirs(args["audio_storing_dir"])
	except OSError:
		if not os.path.isdir(args["audio_storing_dir"]):
			raise

	# Preprocessing: use glob to grab the videos paths and loop over them
	for video_path in glob.glob(args["dataset"] + "*.mp4"):
		count += 1
		print count

		video_id_with_ext = video_path[video_path.rfind("/") + 1:] #eg 1001.mp4
		video_id = video_id_with_ext.replace(".mp4", "") # e.g 1001
		audio_storing_path = args["audio_storing_dir"] + video_id + ".wav"  #e.g 1001.wav

		#1. Extract Audio Clips
		try:
			getAudioClip(video_path, audio_storing_path)
		except:
			error_file.write(video_path + "\n")

	# close the Errors file
	error_file.close()