#File and Folder placement:::
# BASE FOLDER PWD MUST contain files "commandF.sh", "convert.py",
#"README.md", "pdf2txt.py", "make_report.py"
# All PDFs to be searched are in a folder of PWD called "PDFs"

counterPDF=1
counterTXT=1
counterDEL=1
STR=""
STR_noES=""
emptyspace=" "
pdfname=""
for file in $PWD/PDFs/*.pdf
do
  path=$PWD/
  pdfname="${file##*/}"
  echo "converting file "$pdfname
  extension=.txt
  outfile=$path$pdfname$extension
  python pdf2txt.py "$file" >> "$outfile"
  counterPDF=$((counterPDF+1))
done
for file in $PWD/*.txt
do
  pdfname="${file##*/}"
  echo "searching through "$pdfname

  name="$pdfname"
  STR_noES="$STR$name"
  STR="$STR_noES$emptyspace"
  counterTXT=$((counterTXT+1))
done
echo $STR_noES
python convert.py $STR_noES
python make_report.py
#rm *.txt
