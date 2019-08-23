from lilaclib import *

def pre_build():
  depends_lily_re = re.compile(
    r'''^(depends=.*?)['"]?linux-lily[^'") ]*['"]?''')

  kernel = _G.newvers[1]
  update_pkgver_and_pkgrel(_G.newver)
  for line in edit_file('PKGBUILD'):
    m = depends_lily_re.match(line)
    if m:
      line = depends_lily_re.sub(
        r'\1"linux-lily=%s"' % kernel, line)
    print(line)

def post_build():
  git_pkgbuild_commit()
