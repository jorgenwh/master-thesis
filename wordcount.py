import os

filenames = [os.path.join(dp, f) for dp, dn, fns in os.walk("sections") for f in fns if os.path.splitext(f)[1] == '.tex']
filenames.append("main.tex")

word_count = 0
for fn in filenames:
    with open(fn) as f:
        inside_fig = False
        for line in f:
            if line.startswith("\\begin{figure}"):
                inside_fig = True
            if line.startswith("\\end{figure}"):
                inside_fig = False
            if not inside_fig:
                word_count += len(line.split())
print(f"Estimated thesis word count: {word_count}")
