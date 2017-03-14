# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile-server
pkgver=6.0.8
pkgrel=2
pkgdesc="Seafile is an online file storage and collaboration tool"
arch=('i686' 'x86_64' 'armv7h' 'armv6h')
url="https://github.com/haiwen/${pkgname}"
license=('AGPL3')
makedepends=("vala" "intltool")
depends=("seafile" "wget" "sqlite" "fuse" "ccnet-server" "libarchive"
         "python2-mako" "python2-dateutil" "python2-webpy" "python2-pip"
         "python2-virtualenv" "python2-flup" "python2-six" "python2-chardet"
         "python2-simplejson" "libevhtp-seafile" "git")
source=("${pkgname}-${pkgver}-server.tar.gz::${url}/archive/v${pkgver}-server.tar.gz"
        "seafile-admin_virtualenv.patch"
        "seafile-server@.service"
        "seahub-preupgrade"
        "create-default-conf-dir.patch"
        "0001-Revert-server-put-pids-folder-out-of-seafile-data.patch"
        "libseafile.in.patch")
sha256sums=('ec744e735c64c91e58895733a264a55df119afa4e4eb17dd6845eff568bab464'
            '52fb29858f6424052cf01630ad72b5687a4fb259f23f9efc97f08be04a883218'
            'ae1ed38f94304d27e4ef1ca66e15d544f99681c1e743c510c54d4a112f050421'
            '333b78e2ac2ce03b243a70223975bfb0f8e1998edc074b4307c9a96df1b5883f'
            '6bd632f8741b039bad961af3d6850b651e25b7e7a3018d6e2789f350ff93bb78'
            'b1748e826d8e7cccdd825b99864b74dfb5795312f8878d63e9a87105f4382e29'
            'a2d7f7cf0c59aba97650af62b3cefd0ceb71a1007c34d9369a88e5769c7f6076')
optdepends=('libmariadbclient: mysql server support')
install=seafile-server.install

prepare () {
  cd "${srcdir}/${pkgname}-${pkgver}-server"

  patch -p1 -i "${srcdir}/seafile-admin_virtualenv.patch"
  patch -p1 -i "${srcdir}/0001-Revert-server-put-pids-folder-out-of-seafile-data.patch"
  patch -p1 -i "${srcdir}/create-default-conf-dir.patch"
  patch -p1 -i "${srcdir}/libseafile.in.patch"

  # Fix all script's python 2 requirement
  grep -s -l -r '#!/usr/bin/env python' "${srcdir}/${pkgname}-${pkgver}-server" \
    | xargs sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/env python2|g'
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}-server"

  ./autogen.sh

  ./configure \
    --enable-fuse \
    --enable-python \
    --prefix=/usr \
    PYTHON=/usr/bin/python2

  make
}

package() {
  # Install library and header files
  cd "${srcdir}/${pkgname}-${pkgver}-server"

  make DESTDIR="${pkgdir}" install

  # Remove files already installed by seafile
  rm -rf "${pkgdir}/usr/lib/libseafile."*
  rm -rf "${pkgdir}/usr/lib/pkgconfig"
  rm -rf "${pkgdir}/usr/lib/python2.7/site-packages/seafile"
  rm -rf "${pkgdir}/usr/include"

  # Install all scripts
  mkdir -p "${pkgdir}/usr/share/${pkgname}"
  cp -r -p "${srcdir}/${pkgname}-${pkgver}-server/scripts" \
    "${pkgdir}/usr/share/$pkgname/scripts"

  # Remove win32 and other distributions specific scripts
  rm -rf "${pkgdir}/usr/share/$pkgname/scripts/build"
  rm -rf "${pkgdir}/usr/share/$pkgname/scripts/upgrade/win32"

  # Install systemd service
  install -D -m644 "${srcdir}/seafile-server@.service" \
    "${pkgdir}/usr/lib/systemd/system/seafile-server@.service"

  # Install seahub preupgrade script
  install -D -m755 "${srcdir}/seahub-preupgrade" \
    "${pkgdir}/usr/bin/seahub-preupgrade"
}
