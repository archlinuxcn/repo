# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile
pkgver=6.0.4
pkgrel=1
pkgdesc="Seafile is an online file storage and collaboration tool"
arch=('i686' 'x86_64' 'armv7h' 'armv6h')
url="https://github.com/haiwen/${pkgname}"
license=('GPL2')
depends=("ccnet" "fuse" "python2" "sqlite")
makedepends=("vala" "intltool")
source=("seafile-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "libseafile.in.patch")
sha256sums=('b3919bff1e0f974483df129e500868332e752dec6380556839e006bf9d5b425e'
            'a2d7f7cf0c59aba97650af62b3cefd0ceb71a1007c34d9369a88e5769c7f6076')
provides=('seafile-client-cli')

prepare () {
  cd "${srcdir}/seafile-${pkgver}"

  patch -p1 -i "${srcdir}/libseafile.in.patch"

  # Fix all script's python 2 requirement
  grep -s -l -r '#!/usr/bin/env python' "${srcdir}/seafile-${pkgver}" \
    | xargs sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/env python2|g'
}

build() {
  cd "$srcdir/seafile-${pkgver}"

  ./autogen.sh

  ./configure \
    --enable-console \
    --prefix=/usr \
    PYTHON=/usr/bin/python2

  make
}

package() {
  cd "${srcdir}/seafile-${pkgver}"

  make DESTDIR="${pkgdir}" install
}
