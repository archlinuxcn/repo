from types import SimpleNamespace
from lilaclib import *

from ast_grep_py import SgRoot

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('qt6-wayland')
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
  edits.append(node.replace('_pkgname=qt6-wayland\npkgname=qt6-wayland-lily'))

  node = r.find(pattern='_pkgver=$A')
  pkgver = node['A'].text().replace('-', '')
  node = r.find(pattern='pkgver=$A')
  edits.append(node.replace(f'pkgver={pkgver}'))

  node = r.find(pattern='_pkgfn=$A')
  edits.append(node.replace('_pkgfn=qtwayland'))

  node = r.find(pattern='pkgdesc=$A')
  desc = node['A'].text().strip('\'"') + ', patched by lilydjwg'
  edits.append(node.replace(f'pkgdesc=\'{desc}\''))

  node = r.find(pattern='source=($$$A)')
  arr = node.child(2)
  elems = arr.children()
  indent = elems[-2].range().start.column
  patches = [
    '0005-fix-egl-compositor-shutdown.patch',
  ]
  e = elems[-1].replace(''.join(f'\n%s{s}' % (' ' * indent) for s in patches) + ')')
  edits.append(e)

  sums = [
    'fe4b74099872ba6e5071704899741597fb2b0234052e9c343d746a0db4497e95',
  ]
  node = r.find(pattern='sha256sums=($$$A)')
  arr = node.child(2)
  elems = arr.children()
  indent = elems[-2].range().start.column
  e = elems[-1].replace(''.join(f'\n%s{s}' % (' ' * indent) for s in sums) + ')')
  edits.append(e)

  node = r.find(pattern='url=$A')
  e = node.replace('''%s
provides=(qt6-wayland=$pkgver)
conflicts=(qt6-wayland)''' % node.text())
  edits.append(e)

  node = r.find(pattern='groups=($$$A)')
  edits.append(node.replace(''))

  patch_code = ''.join(f'  patch -p1 < "$srcdir"/{p}\n' for p in patches)
  node = r.find(pattern='prepare')
  if node:
    body = node.parent().children()[-1]
    elems = body.children()
    e = elems[-1].replace(patch_code + '}')
    edits.append(e)
  else:
    node = r.find(kind='function_definition')
    e = node.replace(f'''prepare() {{
  cd $_pkgfn
{patch_code}\
}}\n\n''' + node.text())
    edits.append(e)

  new = r.commit_edits(edits)
  with open('PKGBUILD', 'w') as f:
    f.write(new)

