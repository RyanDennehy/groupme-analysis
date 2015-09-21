# groupme-analysis

A suite of functions to extract statistics about your GroupMe group chat

## Running the program

This program works with GroupMe data in JSON format, which is gathered through 
the GroupMe API. I used a tool called [groupme-tools](https://github.com/cdzombak/groupme-tools) 
by cdzombak on GitHub, which I highly recommend.

Simply enter `python3 groupme-analysis.py` and you will be prompted for the JSON file you wish to open. The program will then run any function you inserted into the program. At this point any functions you want to run must be inserted into main()

## Requirements

Works with Python 3.x, not 2.x

However, in its current form, this program could probably be edited to work with 
Python 2.x very easily
