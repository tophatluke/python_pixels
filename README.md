# python_pixels
Dumping pixel data of images

Simple scripts hacked together for dumping pixel data.

# Requirements
`pip install pillow`

# How to use

Modify the script to take in whatever file you want. Output goes to standard output, so use a redirect to put it into a file.

## Each row of pixels is a record

### Python 2
`py2_redgreen_rows.py > somefile.csv`

### Python 3
`py3_redgreen_rows.py > somefile.csv`

## One record for each pixel
Each record has "X, Y, I" format. X and Y for pixel location, I for ...intensity (?) PIL says the test files only had an "I" channel. :)

### Python 2
`py2_xyi.py > somefile.csv`

### Python 3
`py3_xyi.py > somefile.csv`
