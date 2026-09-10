from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

_PATCH = '0001-add-setOutputDpmsMode-dbus-method.patch'
_PATCH_SHA256 = '30bf595c645cf80b5c5c8294e5fbd3604c84683f1bc1a8121adbe0733df10dab'

_EXPECTED = {'pkgname', 'provides', 'source', 'sha256sums', 'prepare', 'renamed'}


def pre_build():
  g.files = download_official_pkgbuild('kwin')

  checks = set()
  state = 'out'
  prepare_seen = False
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=kwin-dpms-per-display'
      checks.add('pkgname')

    elif line.startswith('groups=('):
      # The official package is in the plasma group; the renamed package must not
      # join it, it replaces the official package through provides/conflicts.
      line = "provides=(\"kwin=$pkgver\")\nconflicts=('kwin')"
      checks.add('provides')

    elif line.startswith('source=('):
      if line.endswith(')'):
        line = line.replace(')', ' %s)' % _PATCH)
        checks.add('source')
      else:
        state = 'source'

    elif state == 'source' and line.endswith(')'):
      line = line.replace(')', ' %s)' % _PATCH)
      state = 'out'
      checks.add('source')

    elif line.startswith('sha256sums='):
      state = 'sha256sums'

    elif state == 'sha256sums' and line.endswith(')'):
      line = line.replace(')', "\n            '%s')" % _PATCH_SHA256)
      state = 'out'
      checks.add('sha256sums')

    elif line.startswith('prepare('):
      state = 'prepare'
      prepare_seen = True

    elif state == 'prepare' and line.startswith('}'):
      line = '  cd "$srcdir"/kwin-$pkgver\n  patch -Np1 -i "$srcdir"/%s\n' % _PATCH + line
      state = 'out'
      checks.add('prepare')

    elif line.startswith('build()') and not prepare_seen:
      # The official PKGBUILD has no prepare(), so add one for the local patch.
      line = ('prepare() {\n'
              '  cd "$srcdir"/kwin-$pkgver\n'
              '  patch -Np1 -i "$srcdir"/%s\n'
              '}\n\n%s' % (_PATCH, line))
      checks.add('prepare')

    if '$pkgname' in line:
      # The upstream tarball is named kwin-<ver>, independently of pkgname.
      line = line.replace('${pkgname}', 'kwin').replace('$pkgname', 'kwin')
      checks.add('renamed')

    print(line)

  if checks != _EXPECTED:
    raise ValueError('official kwin PKGBUILD layout changed, checks=%r' % sorted(checks))


def post_build():
  git_add_files(g.files)
  git_commit()
