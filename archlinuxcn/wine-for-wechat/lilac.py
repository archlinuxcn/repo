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

  text = "'acb6f1a0db48872994d0829a40f7be239d7114bc2ca0964cbbfe44af3d02dec03cb63528c52990d22ac3b926de510faf8ad5a9f88b98b2e9914836531023684f')"
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
    text = 'cd wine && patch -p1 < "$srcdir"/wine-wechat.patch\n}'
    e = elems[-1].replace(' ' * indent + text)
    edits.append(e)
  else:
    node = r.find(kind='function_definition')
    e = node.replace('''prepare() {
  cd $_pkgname
  patch -p1 < ../wine-wechat.patch
}\n\n''' + node.text())
    edits.append(e)

  new = r.commit_edits(edits)
  with open('PKGBUILD', 'w') as f:
    f.write(new)

