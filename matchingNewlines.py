import re

new_line = re.compile(".*", re.DOTALL)
mo1 = new_line.search("Serve the public trust.\nProtect the innocent.\nUphold the law.")
print(mo1.group())