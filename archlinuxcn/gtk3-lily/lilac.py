from types import SimpleNamespace

from lilaclib import (
  download_official_pkgbuild, edit_file,
  git_commit, git_add_files,
)

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('gtk3')

  state = ''
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      state = 'pkgname'
    elif state == 'pkgname':
      if line.strip() == ')':
        state = ''
      elif line.strip() == 'gtk3':
        line = line.replace('gtk3', 'gtk3-lily')
      else:
        line = line.replace('gtk3', '# gtk3')

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
      line = line.replace(')', "\n        '2718db7adc07ee2df86b6dacbfb7638217b2cb76c5f5acde4ce9bd7a4617989744326069670b6cc4e5aff59fac410db9b60db7f07dd2a2e36a40b7a3b0d2d8b9'\n        '805b43b9be928362fc9e5ec1738bc9c069d2f3fc32c6d740aefdbab1f8cbd43a5d11aea8113cf9df613f203f6dd77ac250a1e3a6f2399848de58642f08ac0aac')")
      state = ''

    elif line.startswith('prepare('):
      state = 'prepare'
    elif state == 'prepare' and line.startswith('}'):
      line = ('  patch -Np1 -i ../0001-wayland-im-notify-wayland-after-set_cursor_location.patch\n'
              '  patch -Np1 -i ../0001-inhibit-hex-check.patch\n'
              + line)
      state = ''

    elif line.startswith('package_gtk3'):
      state = 'package'
      line = line.replace('gtk3', 'gtk3-lily')
    elif state == 'package':
      if line.strip().startswith('provides='):
        line += '\n    gtk3=$pkgver'
      elif line.strip().startswith('conflicts='):
        line = line.replace(')', ' gtk3)')

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
