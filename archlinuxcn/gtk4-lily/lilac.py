from types import SimpleNamespace

from lilaclib import (
  download_official_pkgbuild, edit_file,
  git_commit, git_add_files,
)

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('gtk4')

  state = ''
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      state = 'pkgname'
    elif state == 'pkgname':
      if line.strip() == ')':
        state = ''
      elif line.strip() == 'gtk4':
        line = line.replace('gtk4', 'gtk4-lily')
      else:
        line = line.replace('gtk', '# gtk')

    elif line.startswith('pkgdesc='):
      line = line[:-1] + ', with lilydjwg\'s patches"'

    elif line.startswith('source=('):
      state = 'source'
    elif state == 'source' and line.endswith(')'):
      line = line.replace(')', '  0001-wayland-im-notify-wayland-after-set_cursor_location.patch\n  0001-inhibit-hex-check.patch)')
      state = ''

    elif line.startswith('b2sums='):
      state = 'b2sums'
    elif state == 'b2sums' and line.endswith(')'):
      line = line.replace(')', "\n        '025d7e58d415526b4478f19a9b145bd173f6f37cc11a8d6b902f7fb1deabdd606588f949f9d2b0a3ec24efe1e90b200b74b80b5fcce359b349044ded6e16bd6f'\n        'f5a4f9db6b527ae13a60074a2bbaa5e4401a52625531e97a21b2d5f44845ab869512083063d4fee9b50e536d5448e43eeab63700fb39a293a71d424f8fb0eea6')")
      state = ''

    elif line.startswith('prepare('):
      state = 'prepare'
    elif state == 'prepare' and line.startswith('}'):
      line = ('  patch -Np1 -i ../0001-wayland-im-notify-wayland-after-set_cursor_location.patch\n'
              '  patch -Np1 -i ../0001-inhibit-hex-check.patch\n'
              + line)
      state = ''

    elif line.startswith('package_gtk4'):
      state = 'package'
      line = line.replace('gtk4', 'gtk4-lily')
    elif state == 'package':
      if line.strip().startswith('provides='):
        line += '\n    gtk4=$pkgver'
      elif line.strip().startswith('conflicts='):
        line = line.replace(')', ' gtk4)')

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
