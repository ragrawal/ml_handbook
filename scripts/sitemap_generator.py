import yaml
from glob import glob
from os import path
from urllib.parse import urljoin

if __name__ == '__main__':
	with open('_config.yml', 'r') as fp:
		config = yaml.safe_load(fp)

	base_url = config['url']

	with open('_site/sitemap.txt', 'w') as fp:
		for file in glob('_site/*.html'):
			fp.write(urljoin(base_url, path.basename(file)) + '\n')
