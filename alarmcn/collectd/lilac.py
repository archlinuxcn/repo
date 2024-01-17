from lxml import html

from lilaclib import *

def pre_build():
  page = s.get('https://www.collectd.org/download.html')
  doc = html.fromstring(page.text)
  ul = doc.xpath('//h2[@id="source"]/following::ul[1]//ul')[0]
  sha256sum = ul.xpath('.//code')[0].text

  update_pkgver_and_pkgrel(_G.newver, updpkgsums=False)

  for line in edit_file('PKGBUILD'):
    if line.startswith('sha256sums='):
      line = f"sha256sums=('{sha256sum}'"
    print(line)

def post_build():
  git_add_files("PKGBUILD")
  git_commit()
