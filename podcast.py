#!/usr/bin/python
import sys
import getopt
import ftplib
import os
import eyed3

# receive the file via script arguments
def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'podcast.py -i <inputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'podcast.py -i <inputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg

if __name__ == "__main__":
   main(sys.argv[1:])

# Parse the filename, which will tell you the program.
# (e.g. ctc == Christ the Center, rmr == Reformed Media Review, pc == Proclaiming Christ, pft == Philosophy for Theologians)
# We could store the list of codes and corresponding program names in a config file.


# Check for episode information (title, description, etc.) through Wordpress API. You can search by filename, e.g. for ctc450.mp3, find a post named ctc450
# These credentials should be stored in a separate config file.


# then ID3 tag the file / This could be improved with some sort of templates or configuration files defining the fields for each program.
audiofile = eyed3.load(inputfile) # load file sent through the command line arg
audiofile.tag.artist = u"Reformed Forum"
audiofile.tag.album = u"Program Name"
audiofile.tag.album_artist = u"Reformed Forum"
audiofile.tag.title = u"title here"
audiofile.tag.track_num = 1

audiofile.tag.save()


# If there is no Wordpress post, check to see if there is an ID3 tag in this file.


# If there is a title and description in an existing ID3 tag, then create a Wordpress post using the Wordpress API.


# Upload the file to the FTP server for our podcast host. Store these credentials and remote path in a separate config file.
ftp = ftplib.FTP("xx.xx.xx.xx")
ftp.login("UID", "PSW")
ftp.cwd("/remote/path/to/put/file")
os.chdir(r"/local/path/to/file")
myfile = open(inputfile, 'r') # maybe 'rb' instead of 'r'
ftp.storlines('STOR ' + inputfile, myfile)
myfile.close()

# Insert a new record into reformed.media. This system provides the download links and tracks basic stats for downloads. These credentials should also be stored in a separate config file.
 # filename
 # duration
 # mime type