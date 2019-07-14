
#Generates html report for searched keywords...
import os, sys, inspect
cmd_markdown = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"deps/markdown/")))
sys.path.append(cmd_markdown)
import markdown 		# Convert markdown to html
import codecs			# Markdown require UTF-8 encoding of the .md file
import time				# Print the date on the report
import re				# Regular expressions
from sets import Set	# We'll need the 'Set' object

txt_report = open("./output.txt", 'r')							# .txt version of the report from search.py
report = open("./report.md", 'w')								# .md version of the report to be written

# Title and Top Matter
report.write("#Search Report\n")							# title
date_string = time.strftime("%d/%m/%Y")						# date
report.write("Report generated: " + date_string + "\n")		# write the Date generated
report.write("Report generaged by: Doc_Tag\n")			# software name

# Summary of the Search
report.write("##Search Summary\n")
string_of_txt_report = txt_report.read()					# convert report to a single string for regex work
txt_report.close()
summary_list = re.findall(r'Keyword (\w+) found in file: (\S+) (\d+) times', string_of_txt_report)	# find tuples of (Keyword, filename, hits)

keywords = Set([])						# make a set of keyowords
for Tuple in summary_list:
	keywords.add(Tuple[0])

report.write("Search Keywords: \n\n")	# print out the keywords
for keyword in keywords:
	report.write("- *"+keyword+"* \n")
report.write("\n")

filenames = Set([])						# make a set of filenames
for Tuple in summary_list:
	filenames.add(Tuple[1])

report.write("Files searched: \n")		# print out the filenames
for filename in filenames:
	report.write("- *"+filename+"*\n")
report.write("\n")

# fine details
report.write("##Findings\n")
txt_report = open("output.txt", 'r')
result = []
section = []
for line in txt_report:					# structure the report as list of keyword hits starting with the keyword string
	if "Keyword" in line:
		if section != [] :
			result.append(section)
			section = []
			section.append(line)
		else:
			section.append(line)
	else:
		section.append(line)
else:
	result.append(section)
txt_report.close()

for filename in filenames:				# for each pdf filename:
	report.write("### Findings in " + filename + "\n")			# subtitle for filename
	for keyword in keywords:									# for each search keyword
		for hit in result:										# search through the hits
			if keyword in hit[0] and filename in hit[0]:		# if the hit is the right keyword and filename
				for line in hit:								# print all the lines of the hit to the markdown report
					if line == hit[0]:
						report.write(line)
					else:
						report.write(line)

report.close()

# convert to html
mdreport = open("./report.md", 'r')
markdown.markdownFromFile("./report.md", "report.html")
mdreport.close()

# doctor the html to make it prettier

Top = ("<head>"+
"<meta charset=\"utf-8\"/>" +
"<title>" +
"Doc_Tag search Report" +
"</title>" +
"<link href=\"http://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.1/styles/github.min.css\" rel=\"stylesheet\"/>" +
"<style type=\"text/css\">" +
"body{font:16px Helvetica,Arial,sans-serif;line-height:1.4;color:#333;word-wrap:break-word;background-color:#fff;padding:10px 15px}strong{font-weight:700}h1{font-size:2em;margin:.67em 0;text-align:center}h2{font-size:1.75em}h3{font-size:1.5em}h4{font-size:1.25em}h1,h2,h3,h4,h5,h6{font-weight:700;position:relative;margin-top:15px;margin-bottom:15px;line-height:1.1}h1,h2{border-bottom:1px solid #eee}hr{height:0;margin:15px 0;overflow:hidden;background:0 0;border:0;border-bottom:1px solid #ddd}a{color:#4183C4}a.absent{color:#c00}ol,ul{padding-left:15px;margin-left:5px}ol{list-style-type:lower-roman}table{padding:0}table tr{border-top:1px solid #ccc;background-color:#fff;margin:0;padding:0}table tr:nth-child(2n){background-color:#aaa}table tr th{font-weight:700;border:1px solid #ccc;text-align:left;margin:0;padding:6px 13px}table tr td{border:1px solid #ccc;text-align:left;margin:0;padding:6px 13px}table tr td :first-child,table tr th :first-child{margin-top:0}table tr td:last-child,table tr th :last-child{margin-bottom:0}img{max-width:100%}code{padding:0 5px;background-color:#d3d3d3}blockquote{padding: 0 15px;border-left:4px solid #ccc}" +
"</style>" +
"</head>" +
"<body>")

Bottom = "</body>"
crappy_report = open("report.html", 'r')
better_report = open("Doc_Tag_report.html", 'w')
crappy_string = crappy_report.read()
better_report.write(Top+crappy_string+Bottom)

crappy_report.close()
better_report.close()
