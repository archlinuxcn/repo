from types import SimpleNamespace
import re

from ast_grep_py import SgRoot

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('wine')
  edit_it()

def post_build():
  git_add_files(g.files)
  git_commit()

def edit_it():
  sh = open('PKGBUILD').read()
  sh = sh.replace('$pkgname', '$_pkgname')
  lib32_re = re.compile(r'\s+lib32-[\S]+')
  sh = lib32_re.sub('', sh)

  doc = SgRoot(sh, 'bash')
  r = doc.root()
  edits = []

  node = r.find(pattern='pkgname=$A')
  edits.append(node.replace('_pkgname=wine\npkgname=wine-for-wechat'))

  node = r.find(pattern='pkgdesc=$A')
  text = 'pkgdesc="A patched version of Wine for running Wechat and Netease Music without persistent shadow windows"'
  edits.append(node.replace(text))

  node = r.find(pattern='source=($$$A)')
  arr = node.child(2)
  elems = arr.children()
  indent = elems[-2].range().start.column
  e = elems[-1].replace('\n%swine-wechat.patch)' % (' ' * indent))
  edits.append(e)

  text = "'646dfd6ec62fb9ddbfb27aac0ac80d87926fbc3360bb53cca942622e95d1ec380f0b5efdfd45bbe1cdce72661b7b36b15ffb7874b1b4269e3bd56a14ec0d2166')"
  node = r.find(pattern='sha512sums=($$$A)')
  arr = node.child(2)
  elems = arr.children()
  indent = elems[-2].range().start.column
  e = elems[-1].replace('\n%s' % (' ' * indent) + text)
  edits.append(e)

  node = r.find(kind='function_definition').prev()
  e = node.replace('''%s
provides=(wine=$pkgver)
conflicts=(wine)''' % node.text())
  edits.append(e)

  node = r.find(pattern='prepare')
  if node:
    body = node.parent().children()[-1]
    elems = body.children()
    indent = elems[-2].range().start.column
    text = 'patch -p1 < "$srcdir"/wine-wechat.patch\n}'
    e = elems[-1].replace(' ' * indent + text)
    edits.append(e)
  else:
    node = r.find(kind='function_definition')
    e = node.replace('''prepare() {
  cd $_pkgname
  patch -p1 < ../wine-wechat.patch
}\n\n''' + node.text())
    edits.append(e)

  node = r.find(pattern='--enable-win64')
  indent = node.range().start.column
  e = node.replace('--enable-win64 \\\n%s--enable-archs=x86_64,i386' % (' ' * indent))
  edits.append(e)
  comm = node.parent().next()
  for c in comm.next_all():
    edits.append(c.replace(''))
  del edits[-1] # keep last '}'

  node = r.find(pattern='package').parent()
  body = node.children()[-1]
  for c in body.child(0).next_all():
    if c.find(pattern='"Packaging Wine-64..."'):
      break
    edits.append(c.replace(''))

  new = r.commit_edits(edits)
  with open('PKGBUILD', 'w') as f:
    f.write(new)

