import sys
import subprocess



puzzle = sys.argv[1]
p = subprocess.run(["bash", "./fetch.sh", puzzle],
        capture_output=True)

print(p)