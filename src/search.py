import sys

temp_keyword = ""

enter_keyword = raw_input("Enter your keywords: ")
temp_keyword = temp_keyword + enter_keyword + " "
keyword = temp_keyword.split()


def search (keyword):
    out = open('output.txt', 'w')
    #Search through every inputted pdf
    for pdf_loop in range (1,len(sys.argv)):
        f = open(sys.argv[pdf_loop], 'r')
        text = f.read().lower().split()
        if len(text) < 100:
            out.write("ERROR: \nFile \"" + sys.argv[pdf_loop] + "\" is either suspiciously brief or cannot be read! \nPlease also check this one manually.\n")

        #Search through every inputted keyword
        for keyword_loop in range (0, len(keyword)):
            counter = 0
            where_appear = []
            appear = False

            #Search through individual pdf's text
            for i in range(0, len(text)):
                if text[i] == keyword[keyword_loop].lower():
                    counter = counter + 1
                    where_appear.append(i)
                    appear = True
            out.write("Keyword " + keyword[keyword_loop].upper() + " found in file: " + sys.argv[pdf_loop] + " " + str(counter) + " times \n \n")
            if appear == True:
                #out.write("Keyword " + keyword[keyword_loop].upper() + " found in file: " + sys.argv[pdf_loop] + " " + str(counter) + " times \n \n")
                #Start creating summary
                for i in range(0,len(where_appear)):
                    try:
                        if where_appear[i] < 16:
                            out.write("\"",)
                            for j in range (0,30):
                                out.write(text[j] + " ",)
                            out.write("\"",)
                        elif where_appear[i] > len(text)-15:
                            out.write("\"",)
                            for j in range (len(text) - 30, len(text)):
                                out.write(text[j] + " ",)
                            out.write("\"",)
                        else:
                            out.write("\"",)
                            for j in range (-15,15):
                                if text[where_appear[i] + j] == keyword[keyword_loop]:
                                    out.write(keyword[keyword_loop].upper() + " ")
                                else:
                                    out.write(text[where_appear[i] + j] + " ",)
                            out.write("\"",)
                        out.write("\n")
                    except IndexError:
                        for j in range (0,len(text)):
                            if text[where_appear[i] + j] == keyword[keyword_loop]:
                                out.write(keyword[keyword_loop].upper() + " ")
                            else:
                                out.write(text[where_appear[j]] + " ",)
                        out.write("\"",)
                    out.write("\n")
                    appear = False
search(keyword)
