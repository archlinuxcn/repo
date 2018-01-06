# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile-server
pkgver=6.2.3
pkgrel=1
pkgdesc="Seafile is an online file storage and collaboration tool"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/${pkgname}"
license=('AGPL3')
makedepends=("vala" "intltool")
depends=("seafile" "wget" "sqlite" "fuse" "ccnet-server" "libarchive"
         "libevhtp-seafile" "git" "ffmpeg"
         "python2-requests" "python2-flup")
optdepends=("python2-setuptools: MySQL deploying"
            "python2-pillow: MySQL deploying"
            "mysql-python: MySQL deploying"
            "python2-wsgidav-seafile: webdav-support")
source=("${pkgname}-${pkgver}-server.tar.gz::${url}/archive/v${pkgver}-server.tar.gz"
        "seafile-admin_virtualenv.patch"
        "seafile-server@.service"
        "create-default-conf-dir.patch"
        "0001-Revert-server-put-pids-folder-out-of-seafile-data.patch"
        "libseafile.in.patch"
        "openssl-1.1.diff"
        "mysql-setup.patch")
sha256sums=('77bfc8a0037d37588edf96e46b3975453ff6e48a06b4343ce97d9381618cc111'
            '52fb29858f6424052cf01630ad72b5687a4fb259f23f9efc97f08be04a883218'
            'da31d1b61031cbacc42e1ab708c67c83dba933ff391b07677dabab7ab79729f4'
            '6bd632f8741b039bad961af3d6850b651e25b7e7a3018d6e2789f350ff93bb78'
            'b1748e826d8e7cccdd825b99864b74dfb5795312f8878d63e9a87105f4382e29'
            'a2d7f7cf0c59aba97650af62b3cefd0ceb71a1007c34d9369a88e5769c7f6076'
            'ffa351b22e89a66f80139888e4e7a2c2bde41fd648d57c71dcf10884dc03bbc3'
            '67da9dff7e1620041eb5a5e3dbb5c61457c2106e5fbb57db06e6f061a0d63c7d')

prepare () {
  cd "${srcdir}/${pkgname}-${pkgver}-server"

  patch -p1 -i "${srcdir}/seafile-admin_virtualenv.patch"
  patch -p1 -i "${srcdir}/0001-Revert-server-put-pids-folder-out-of-seafile-data.patch"
  patch -p1 -i "${srcdir}/create-default-conf-dir.patch"
  patch -p1 -i "${srcdir}/libseafile.in.patch"
  patch -p1 -i "${srcdir}/openssl-1.1.diff"
  patch -p1 -i "${srcdir}/mysql-setup.patch"

  # Fix all script's python 2 requirement
  grep -s -l -r '#!/usr/bin/env python\b' "${srcdir}/${pkgname}-${pkgver}-server" \
    | xargs sed -i -e '1 s|env python\b|env python2|'
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
  rm -rf "${pkgdir}/usr/share/${pkgname}/build"
  rm -rf "${pkgdir}/usr/share/${pkgname}/upgrade/win32"

  # Install systemd service
  install -D -m644 "${srcdir}/seafile-server@.service" \
    "${pkgdir}/usr/lib/systemd/system/seafile-server@.service"
}
