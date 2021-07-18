from lxml import html

from lilaclib import *

def pre_build():
  page = s.get('https://collectd.org/download.shtml')
  doc = html.fromstring(page.text)
  ul = doc.xpath('//h2[@id="source"]/following::ul[1]//ul')[0]
  sha256sum = ul.xpath('.//div')[0].text_content().split()[-1]

  update_pkgver_and_pkgrel(_G.newver)

  for line in edit_file('PKGBUILD'):
    if line.startswith('sha256sums='):
      line = f"sha256sums=('{sha256sum}'"
    print(line)

def post_build():
  git_add_files("PKGBUILD")
  git_commit()
  update_aur_repo()
