import os
import sys
import re
import glob
import warnings

WIDGETS = """
<head>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-1286028-10"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-1286028-10');
</script>
<script src="//www.powr.io/powr.js?external-type=html"></script> 
"""


PATTERNS = {
	# Remove Twitter
	re.compile('<style.*?(?:Twitter).*?(?:<\/style>)', re.IGNORECASE | re.DOTALL): '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.3.0/milligram.min.css" integrity="sha256-Ro/wP8uUi8LR71kwIdilf78atpu8bTEwrK5ZotZo+Zc=" crossorigin="anonymous" />'

	# Remove Input Prompt
	, re.compile('<div.*?(?:input_prompt).*?(?:<\/div>)'): ''

	# Remove Output Prompt
	, re.compile('<div.*?(?:output_prompt).*?(?:<\/div>)'): ''

	# Remove Dataframe Scope
	, re.compile('<style scoped>.*?(?:dataframe).*?(?:<\/style>)', re.DOTALL): ''

	# add google tracking
	, re.compile('<head>'): WIDGETS

	# add comment
	, re.compile('<\/body>'): '<div class="powr-comments" id="ebdcad99_1535663766"></div></body>'

}


if __name__ == '__main__':

	for infile in glob.glob("html/*.html"):
		print(infile)

		with open(infile, 'r') as fp:
			html = fp.read()

		original_length = len(html)
		for p, repl in PATTERNS.items():
			html = p.sub(repl, html)

		if original_length == len(html):
			warnings.warn("Not able to find twitter")

		with open(infile, "w") as fp:
			fp.write(html)

