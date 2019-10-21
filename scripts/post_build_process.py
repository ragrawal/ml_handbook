import sys
from glob import glob
import re 

JS = re.compile('(<script type=\"text/javascript\".*?<\/script>)', re.DOTALL)

if __name__ == '__main__':
	for file in glob("_build/??-*.html"):
		print(file)
		with open(file, 'r') as fp:
			c = fp.read()

		nc = JS.sub('{% raw %}\n\\1\n{% endraw %}\n', c)

		# remove require statements from javascript
		output = []
		found_require = False
		for line in nc.split('\n'):
			if 'require(["plotly"]' in line:
				found_require = True
			elif found_require and '</script>' in line:
				output[-1] = line
				found_require = False
			else:
				output.append(line)

		with open(file, 'w') as fp:
			fp.write("\n".join(output))

		




