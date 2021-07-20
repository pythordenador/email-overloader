import requests
import sys

url = sys.argv[1]
filer = sys.argv[2]

r = requests.get(url, allow_redirects=True)
open(filer, "wb").write(r.content)

