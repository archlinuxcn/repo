# Maintainer: Pavan Rikhi <pavan.rikhi@gmail.com>
# Maintainer: BrLi <brli at chakralinux dot org>

pkgname=pencil
pkgver=3.1.0
pkgrel=7
pkgdesc="Sketching and GUI prototyping/wireframing tool"
arch=('any')
license=('GPL2')
url="https://github.com/evolus/pencil"
depends=(electron)
makedepends=(yarn)
source=("https://github.com/evolus/pencil/archive/v$pkgver.tar.gz"
        'fix-package-json.patch'
        'upstream.patch')
sha256sums=('e14eddd0aad28919cfdf8d47b726f9c75a3a0d2042605e8da96309c23a995f44'
            '7094d33707a1fa27b79f296b3083584643150935ac4e464ebd44a82ed04ad036'
            '78c28950a497495f3efef0b915283c10fd834c83996471291ae6ac18e3256997')
conflicts=('evolus-pencil-bin' 'pencil-v2')

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    
    patch -Np1 -i "${srcdir}/upstream.patch"

    # We don't build electron and friends, and don't depends on postinstall script
    patch -Np1 -i "${srcdir}/fix-package-json.patch"
    sed '/^\s*\"electron.*$/d;/postinstall/d' -i app/package.json
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
exec electron /${_destdir} "\$@"
END

    cd "${srcdir}/${pkgname}-${pkgver}"

    cp -r --no-preserve=ownership --preserve=mode app/* "${pkgdir}/${_destdir}/"

    # install icons of vary sizes to hi-color theme
    for px in 16 24 32 48 64 96 128 256; do
        install -Dm644 "build/icons/${px}x${px}.png" \
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
