# Maintainer: taotieren <admin@taotieren.com>

pkgname=proxmark3gui-git
pkgver=0.2.6.r13.g2723abd
pkgrel=1
pkgdesc="A cross-platform GUI for Proxmark3 client | 为 PM3 设计的图形界面"
arch=('x86_64')
url="https://github.com/wh201906/Proxmark3GUI"
license=('LGPL-2.1')
provides=(${pkgname%-git})
conflicts=(${pkgname%-git})
depends=(qt5-serialport)
makedepends=(git
            qt5-tools)
optdepends=("proxmark3: Software for the the Proxmark3, an RFID swiss-army tool")
source=("${pkgname}::git+${url}.git")
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname}/"
    git describe --long --tags | sed 's/V//g;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${srcdir}/${pkgname}/src"
    qmake -makefile -o Makefile "CONFIG+=release"
    make
}

package() {
    cd "${srcdir}/${pkgname}/src"
    export INSTALL_ROOT="${pkgdir}"
    make install

    install -dm0755 "${pkgdir}/usr/bin"
    ln -sf /opt/Proxmark3GUI/bin/Proxmark3GUI "${pkgdir}/usr/bin/${pkgname%-git}"

    cd "${srcdir}/${pkgname}"
    cp -rv config "${pkgdir}/opt/Proxmark3GUI"

    install -Dm0644 "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname%-git}/LICENSE"

    install -Dm0644 /dev/stdin "${pkgdir}/usr/share/metainfo/io.github.wh201906.proxmark3gui.metainfo.xml" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
  <id>io.github.wh201906.proxmark3gui</id>

  <name>${pkgname%-git}</name>
  <summary>${pkgname%-git}</summary>

  <metadata_license>MIT</metadata_license>
  <project_license>LGPL-2.1</project_license>

  <description>
    <p>
      ${pkgdesc}
    </p>
  </description>

  <launchable type="desktop-id">io.github.wh201906.proxmark3gui.desktop</launchable>
</component>
EOF

    install -Dm0644 /dev/stdin "${pkgdir}/usr/share/applications/io.github.wh201906.proxmark3gui.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application

Name=${pkgname%-git}
Comment=${pkgname%-git}
Categories=Network;Qt;

Icon=${pkgname%-git}
Exec=${pkgname%-git}
Terminal=false
EOF
}
