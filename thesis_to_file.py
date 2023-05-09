import os

output_filename = "full_thesis.txt"

filenames = [os.path.join(dp, f) for dp, dn, fns in os.walk("sections") for f in fns if os.path.splitext(f)[1] == '.tex']
filenames.append("main.tex")

outfile = open(output_filename, "w")
for fn in filenames:
    print("Processing file: " + fn)
    with open(fn) as f:
        outfile.write(f.read()) 
outfile.close()
