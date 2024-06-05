from lilaclib import *

def pre_build():
  depends_nginx_re = re.compile(
    r'''^(depends=.*?)['"]?nginx[^'") ]*['"]?''')

  nginx_ver = _G.newvers[1]
  update_pkgver_and_pkgrel(_G.newver)
  for line in edit_file('PKGBUILD'):
    if line.startswith('depends='):
      line = depends_nginx_re.sub(
        r'\1"nginx=%s"' % nginx_ver, line)
    print(line)

def post_build():
  git_pkgbuild_commit()
