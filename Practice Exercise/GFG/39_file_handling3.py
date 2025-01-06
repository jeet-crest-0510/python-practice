from pathlib import Path 
import os

sz = Path('Practice Exercise\GFG\dict.txt').stat().st_size 
print(sz) 

sz = os.path.getsize("Practice Exercise\GFG\dict.txt") 
print(sz)