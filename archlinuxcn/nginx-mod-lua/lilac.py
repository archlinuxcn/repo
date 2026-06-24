from lilaclib import *

def pre_build():
  depends_nginx_re = re.compile(
    r'''^(depends=.*?)['"]?nginx[^'") ]*['"]?''')
  # lua-resty-core has strict version requirement on nginx-mod-lua
  depends_restycore_re = re.compile( r"'lua-resty-core[^']+'")

  nginx_ver = _G.newvers[1]
  newver = _G.newver.lower()
  restycore_ver = _G.newvers[2].lower()
  update_pkgver_and_pkgrel(newver)
  for line in edit_file('PKGBUILD'):
    if line.startswith('depends='):
      line = depends_nginx_re.sub(
        r'\1"nginx=%s"' % nginx_ver, line)
      line = depends_restycore_re.sub(f"'lua-resty-core={restycore_ver}'", line)
    print(line)

def post_build():
  git_pkgbuild_commit()
