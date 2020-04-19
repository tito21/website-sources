import pathlib
from sitemap_generator import Sitemap

site_root = 'https://site.com'
path_site = pathlib.Path('../public')
sitemap = Sitemap(path_site, site_root)
sitemap.make_sitemap(path_site/'sitemap.xml')

with open(path_site/'robots.txt', 'w') as f:
    f.write("Sitemap: {}/sitemap.xml\n".format(site_root))
