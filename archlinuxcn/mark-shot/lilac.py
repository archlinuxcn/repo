from types import SimpleNamespace
from urllib.request import urlopen

from lilaclib import *

g = SimpleNamespace()

# 使用 lilac 检测到的 release tag 对应的 PKGBUILD (而非固定 master),
# 保证打包内容与版本代码一致
def pre_build():
    version = _G.newver  # github 源返回 tag 名, 如 v0.1.45
    url = f'https://raw.githubusercontent.com/jswysnemc/mark-shot/{version}/packaging/aur/PKGBUILD'
    with urlopen(url) as r:
        pkgbuild = r.read().decode('utf-8')
    with open('PKGBUILD', 'w') as f:
        f.write(pkgbuild)

    # 仅当 tag 内 PKGBUILD 版本滞后于 release 时强制同步, 否则保持其 pkgrel=1
    pkgver, _ = get_pkgver_and_pkgrel()
    if pkgver != version.lstrip('v'):
        update_pkgver_and_pkgrel(version.lstrip('v'))

def post_build():
    git_add_files(['PKGBUILD'])
    git_commit()
