import os
import sys

pattern = sys.argv[1]

filenames = [os.path.join(dp, f) for dp, dn, fns in os.walk("sections") for f in fns if os.path.splitext(f)[1] == '.tex']
filenames.append("main.tex")

for fn in filenames:
    with open(fn) as f:
        content = f.read()
        if pattern in content:
            print(fn)
