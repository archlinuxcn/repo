# Maintainer: Joffrey Darcq <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile-server
pkgver=6.2.5
pkgrel=3
pkgdesc="Seafile is an online file storage and collaboration tool"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/${pkgname}"
license=('AGPL3')
makedepends=("vala" "intltool")
depends=("ccnet-server" "libevhtp-seafile" "libarchive"
         "wget" "sqlite" "fuse" "git" "ffmpeg")
optdepends=("python2-wsgidav-seafile: webdav-support")
conflicts=('seafile')
changelog="ChangeLog"
source=("${pkgname}-${pkgver}-server.tar.gz::${url}/archive/v${pkgver}-server.tar.gz"
        "fix_seafile-admin.diff"
        "fix_mysql_support.diff"
        "seafile-server@.service"
        "0001-Revert-server-put-pids-folder-out-of-seafile-data.patch"
        "libseafile.in.patch"
        "openssl-1.1.diff"
)
sha256sums=('8cc17303b3b3949cfb4e914264f6446057bb2eee0b5e6e3a3399294ab566c0e0'
            '91f56d852cb4670ce052f1539ebe51c3ec74189150dc24ed34245ca3397d29a7'
            'c144d93638dfb44d1474c46e427977f4c314def3ca6a31bf495b6b4ce523741f'    
            'da31d1b61031cbacc42e1ab708c67c83dba933ff391b07677dabab7ab79729f4'
            '114920836eec03ac152a88cdfb55de5cd554240ca246dd69d3d9b52b74ec8809'
            'a2d7f7cf0c59aba97650af62b3cefd0ceb71a1007c34d9369a88e5769c7f6076'
            'ffa351b22e89a66f80139888e4e7a2c2bde41fd648d57c71dcf10884dc03bbc3')

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}-server"

    # Remove scripts for tests and others OS
    rm -rf "./scripts/"{build,upgrade/win32,*.bat,*.md} "./integration-tests"

    patch -p1 -i "${srcdir}/fix_seafile-admin.diff"
    patch -p1 -i "${srcdir}/fix_mysql_support.diff" 
    patch -p1 -i "${srcdir}/0001-Revert-server-put-pids-folder-out-of-seafile-data.patch"
    patch -p1 -i "${srcdir}/libseafile.in.patch"
    patch -p1 -i "${srcdir}/openssl-1.1.diff"

    # Use python lib seahub interpreter for all scripts
    grep -s -l -r '#!/usr/bin/env python' "./" \
    | xargs sed -i -e '1 s|#!/usr/bin/env python|#!/usr/lib/seahub/bin/python2|'
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
    cd "${srcdir}/${pkgname}-${pkgver}-server"

    make DESTDIR="${pkgdir}" install

    # Prepare directories layout for an easy deploying
    # https://manual.seafile.com/deploy/using_mysql.html
    mkdir -p "${pkgdir}/usr/share/${pkgname}/runtime"
    cp -r -p "./scripts" "${pkgdir}/usr/share/${pkgname}/scripts"

    mv "${pkgdir}/usr/share/${pkgname}/scripts/seahub.conf" \
       "${pkgdir}/usr/share/${pkgname}/runtime/"
    mv "${pkgdir}/usr/share/${pkgname}/scripts/upgrade" \
       "${pkgdir}/usr/share/${pkgname}/"

    # Install systemd service
    install -Dm644 "${srcdir}/seafile-server@.service" \
                   "${pkgdir}/usr/lib/systemd/system/seafile-server@.service"
}
