# Maintainer: Evan Teitelman <teitelmanevan at gmail dot com>
# Contributor: fxbru <frxbru[at]gmail>

pkgname=sqlmap-git
pkgver=1.0dev.4164.g16f8e4c
pkgrel=1
pkgdesc='Automatic SQL injection and database takeover tool'
arch=('any')
url=('http://sqlmap.org')
license=('GPLv2')
depends=('python2')
provides=('sqlmap')
conflicts=('sqlmap' 'sqlmap-svn')
makedepends=('git')
options=('!strip')
source=('git://github.com/sqlmapproject/sqlmap.git')
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/sqlmap"
  git describe --always | sed 's|-|.|g;s|0\.9|1.0dev|'
}

package() {
  cd "$srcdir/sqlmap"

  # Base directories.
  install -dm755 "$pkgdir/usr/bin"
  install -dm755 "$pkgdir/opt/sqlmap"

  cp -R --no-preserve=ownership * "$pkgdir/opt/sqlmap"

  cat > "$pkgdir/usr/bin/sqlmap" << EOF
#!/bin/bash
cd /opt/sqlmap
python2 sqlmap.py "\$@"
EOF
  chmod 755 "$pkgdir/usr/bin/sqlmap"
}
