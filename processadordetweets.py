import re

f = open("collect_foradilma-20151216.txt")

# r = "on_data"
# r = "\[on_data\] \{\"created_at\":\".{3} .{3} \d\d \d\d:\d\d:\d\d \+\d{4} 2015\",\"id\":(\d*),\"id_str\":\"\d+\",\"text\":(\".*?\"),\"source\":"
r = "\[on_data\] \{\"created_at\":\"(.*?)\",\"id\":(\d*),\"id_str\":\"\d+\",\"text\":(\".*?\"),\"source\":.*\"screen_name\":\"(.*?)\","
for l in f:
	match = re.search(r,l)
	if match:
		print("%s,%s,%s,%s" % (match.group(1), match.group(2), match.group(3), match.group(4)))