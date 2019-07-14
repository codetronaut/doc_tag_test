
import os
import sys
import glob
import string

# Create a directory for converted text files
txt_directory = "Texts"				
if not os.path.exists(txt_directory):
	os.makedirs(txt_directory)

# Check if PDF directory exists
if os.path.isdir("PDFs") == False:
	print "There is no PDFs directory, must create PDFs directory and populate with desired pdf files"

# For each file in the PDF directory run PDF-to-txt.py and direct stdout to txt file

for pdf in glob.glob("./PDFs/*.pdf"):
	ofilename = string.replace(pdf, "PDFs", "Texts")
	ofilename = string.replace(ofilename, ".pdf", ".txt")
	print "Converting ", pdf, "to plain text for analysis"
	os.system("python ./src/PDF-to-txt.py \"" + pdf + "\" >> \"" + ofilename+"\"")
	
# Search each plain text file for keywords and generate plain txt report

argv = ""
arg_list = glob.glob("./Texts/*.txt")
for arg in arg_list:
	argv += "\""+arg+"\" "

os.system("python ./src/search.py "+argv) 	

# Convert plain text report to html

os.system("python ./src/html_report.py")

# Clean up after your self

os.system("rm -r ./Texts/")
os.system("rm report.md")
os.system("rm output.txt")
