from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

_PATCH = '0001-calendar-event-location.patch'
_PATCH_SHA256 = '67d42d95af431cd63c2de82b9c75c9015ccc0d67f9e9377f59ff868b8cd9ec6f'

_EXPECTED = {'pkgbase', 'pkgname', 'provides', 'source', 'sha256sums', 'prepare',
             'mainpkg', 'drop-x11', 'renamed'}


def pre_build():
  g.files = download_official_pkgbuild('plasma-workspace')

  checks = set()
  state = 'out'
  prepare_seen = False
  for line in edit_file('PKGBUILD'):
    if state == 'skip-pkgfn':
      # Drop package_plasma-x11-session() entirely: plasmax11.desktop stays with
      # the separate official plasma-x11-session package.
      if line == '}':
        state = 'out'
      continue

    if line.startswith('pkgbase='):
      # Fold the split package into a single one.
      checks.add('pkgbase')
      continue

    if line.startswith('pkgname=('):
      line = 'pkgname=plasma-workspace-calendar-event-location'
      checks.add('pkgname')

    elif line.startswith('groups=('):
      # The official package is in the plasma group; the renamed package must not
      # join it, it replaces the official package through provides/conflicts.
      line = "provides=(\"plasma-workspace=$pkgver\")\nconflicts=('plasma-workspace')"
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
      line = '  cd "$srcdir"/plasma-workspace-$pkgver\n  patch -Np1 -i "$srcdir"/%s\n' % _PATCH + line
      state = 'out'
      checks.add('prepare')

    elif line.startswith('build()') and not prepare_seen:
      # The official PKGBUILD has no prepare(), so add one for the local patch.
      line = ('prepare() {\n'
              '  cd "$srcdir"/plasma-workspace-$pkgver\n'
              '  patch -Np1 -i "$srcdir"/%s\n'
              '}\n\n%s' % (_PATCH, line))
      checks.add('prepare')

    elif line.startswith('package_plasma-workspace()'):
      line = 'package() {'
      checks.add('mainpkg')

    elif line.startswith('package_plasma-x11-session()'):
      state = 'skip-pkgfn'
      checks.add('drop-x11')
      continue

    elif line.strip().startswith('conflicts=('):
      # Keep the provides/conflicts set at the top level above.
      line = line.replace('conflicts=(', 'conflicts+=(', 1)

    if '$pkgname' in line:
      # The upstream tarball is named plasma-workspace-<ver>, independently of pkgname.
      line = line.replace('${pkgname}', 'plasma-workspace').replace('$pkgname', 'plasma-workspace')
      checks.add('renamed')

    print(line)

  if checks != _EXPECTED:
    raise ValueError('official plasma-workspace PKGBUILD layout changed, checks=%r' % sorted(checks))


def post_build():
  git_add_files(g.files)
  git_commit()
