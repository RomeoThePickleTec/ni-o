import re

def separate(line, typ, exp):
    purple = r"\bint\b|\bfloat\b|\bdouble\b|\bbool\b|\bstring\b|\bvoid\b"
    green = r"\b#include\b|\breturn\b"
    yellow = r"\bwhile\b|\bfor\b"
    blue = r"\bprivate\b|\bpublic\b|\bprotected\b"
    orange = r"\bif\b|\belse\b"
    
    exps = [purple, green, yellow, blue, orange]
    types = ["data-type", "include", "loop", "class-type", "conditional"]
    output = []

    split = re.split(exp, line)
    found = re.findall(exp, line)

#    if (typ == "data-type"):
#        for i in range(len(found)):
#            if(split[i].strip() == ''):
#                val = found.pop(0)
#                print(val)
#                output.append(f"<div class='{typ}'>{val}</div>")
#                if (split[i+1].split(" ") == ""):
     #               var = split[i+1].split(" ")[1]
    #            else:
   #                 var = split[i+1].split(" ")[0]
  #              out = f"<div class='variable'>{var}</div>"
 #               output.append(out)
#    else:
    for i in range(len(found)): 
        if(split[i].strip() == '' or split[i].strip() == '#'):
            if (typ == "data-type"):
                split[i+1] = f"<span class='variable'>{split[i+1].split(' ')[1]}</span>" + ' '.join(split[i+1].split(' ')[2:])
            val = found.pop(0)
            out = f"<span class='{typ}'>{val}</span>"
            split[i] = out


    html = " ".join(output)
    remain = " ".join(split)
    return html, remain, line 



def toHTML(line):
    purple = r"\bint\b|\bfloat\b|\bdouble\b|\bbool\b|\bstring\b|\bvoid\b"
    green = r"\binclude\b|\breturn\b"
    yellow = r"\bwhile\b|\bfor\b"
    blue = r"\bprivate\b|\bpublic\b|\bprotected\b"
    orange = r"\bif\b|\belse\b"
    
    exps = [purple, green, yellow, blue, orange]
    types = ["data-type", "include", "loop", "class-type", "conditional"]
    output = []
    for i in range(5):
        val, line, xd = separate(line, types[i], exps[i])
        output.append(val)
        
    return xd
    
    

def regEx(line):
    #Variables are colored red
    add = toHTML(line)

    txt = f"<div className='line'>" + add + "</div>"
    return txt



def readFile(file):
    text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reto 2</title>
    <link rel="stylesheet" href="act2.css">
</head>
<body>




"""
    out = open("result.html", "w")
    out.write(text)
    f = open(file)
    for line in f:
        #reads each line from the file and calls for another function to append to HTML
        out.write(regEx(line))

    out.write("</body>")
    out.write("</html>")
    f.close()
    out.close()

def main():
    readFile("program.txt")
    print("Executed the program")

if __name__ == '__main__':
    main()