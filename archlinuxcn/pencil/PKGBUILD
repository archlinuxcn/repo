# Maintainer: Pavan Rikhi <pavan.rikhi@gmail.com>
# Maintainer: BrLi <brli at chakralinux dot org>

pkgname=pencil
pkgver=3.1.1
pkgrel=1
pkgdesc="Sketching and GUI prototyping/wireframing tool"
arch=('any')
license=('GPL2')
url="https://github.com/evolus/pencil"
_electron=electron21
depends=($_electron)
makedepends=(yarn)
options=('!strip')
source=("https://github.com/evolus/pencil/archive/v$pkgver.tar.gz"
        '0001-do-not-download-electron.patch')
sha256sums=('84675567281ccdd0d5e273e628cf99a9b76d15245794ef4d38c5bfb2d64c0468'
            '273aa85290169ac313d0990c41d9d697a1266dbca885fc389d9ef8f415d37720')
conflicts=('evolus-pencil-bin' 'pencil-v2')

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    # We don't build electron and friends, and don't depends on postinstall script
    patch -Np1 -i "${srcdir}/0001-do-not-download-electron.patch"

    rm -rfv {./,app/}{yarn.lock,package-lock.json}
}

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    yarn install --pure-lockfile \
                 --no-bin-links \
                 --cache-folder "${srcdir}/cache" \
                 --link-folder "${srcdir}/link" \
                 --ignore-scripts

    cd "${srcdir}/${pkgname}-${pkgver}/app"
    yarn install --pure-lockfile \
                 --no-bin-links \
                 --cache-folder "${srcdir}/cache" \
                 --link-folder "${srcdir}/link" \
                 --ignore-scripts


    # Aggressively remove binary and useless files in node_modules
    cd "${srcdir}/${pkgname}-${pkgver}/app/node_modules"
    find . -iname "CHANGELOG*" -exec rm -rfv {} +
    find . -iname "README*" -exec rm -rfv {} +
    find . -iname "*.md" -exec rm -rfv {} +
    find . -iname "*test*" -exec rm -rfv {} +
    find . -iname "license*" -exec rm -rfv {} +
    find . -iname ".*" -exec rm -rfv {} + || true
    find . -name "yarn.lock" -exec rm -rfv {} +
}

package() {
    local _destdir=usr/lib/"${pkgname}"
    install -dm755 "${pkgdir}/${_destdir}"

    install -Dm755 /dev/stdin "${pkgdir}/usr/bin/${pkgname}" <<END
#!/bin/sh
exec $_electron /${_destdir} "\$@"
END

    cd "${srcdir}/${pkgname}-${pkgver}"

    cp -r --no-preserve=ownership --preserve=mode app/* "${pkgdir}/${_destdir}/"

    # install icons of vary sizes to hi-color theme
    for px in 16 24 32 48 64 96 128 256; do
        install -Dm644 "app/build/icons/${px}x${px}.png" \
            "${pkgdir}/usr/share/icons/hicolor/${px}x${px}/apps/${pkgname}.png"
    done

    install -Dm644 /dev/stdin  "$pkgdir/usr/share/applications/pencil.desktop" <<END
[Desktop Entry]
Encoding=UTF-8
Name=Pencil
Comment=Sketching and GUI prototyping tool
Comment[cs]=Nástroj na kreslení a prototypování GUI
Comment[el]=Εργαλείο σχεδιασμού και κατασκευής πρωτοτύπων γραφικού περιβάλλοντος διεπαφής χρήστη
Comment[es]=Herramienta de esbozado y prototipado de interfaces gráficas de usuario
Comment[vi_VN]=Công cụ phát thảo giao diện Pencil
Exec=/usr/bin/pencil %u
Terminal=false
Type=Application
StartupNotify=true
Icon=pencil
Categories=Graphics;2DGraphics;Development;
MimeType=application/x-evolus-pencil;
END

    install -Dm644 /dev/stdin  "${pkgdir}/usr/share/mime/application/pencil.xml" <<END
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
    <mime-type type="application/x-evolus-pencil">
        <comment>Evolus Pencil Document</comment>
        <icon name="image-x-generic"/>
        <glob pattern="*.ep"/>
        <glob pattern="*.epz"/>
        <glob pattern="*.epgz"/>
        <sub-class-of type="text/xml"/>
    </mime-type>
</mime-info>
END
}
