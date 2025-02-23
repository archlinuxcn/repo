# Maintainer: taotieren <admin@taotieren.com>

pkgbase=mfgtools-git
pkgname=(mfgtools{,-doc}-git)
pkgver=1.5.109.r9.gd669525
pkgrel=1
epoch=
pkgdesc="uuu (Universal Update Utility), mfgtools 3.0. Freescale/NXP I.MX Chip image deploy tools."
arch=('x86_64' 'aarch64')
url="https://github.com/nxp-imx/mfgtools"
license=('BSD')
groups=()
depends=('bzip2' 'zlib' 'libusb' 'libzip' 'openssl')
makedepends=('cmake' 'git' 'ninja')
checkdepends=()
optdepends=()
replaces=()
backup=()
options=('!strip')
install=
changelog=
source=("${pkgbase%-git}::git+${url}.git"
        "${pkgbase%-git}-doc::git+${url}.wiki.git"
		"uuu-complete.bash")
noextract=()
sha256sums=('SKIP'
            'SKIP'
            'ffc8e32655ce574a4719c85c5c9a3530a5ec619e933fc801a291df8ec506a442')
#validpgpkeys=()

pkgver() {
    cd "${srcdir}/${pkgbase%-git}"
    git describe --long --tags |  sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/uuu_//g' | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

# prepare() {
#     cd "${srcdir}/${pkgbase%-git}"
#     git submodule update --init --recursive
# }

build() {
    cd "${srcdir}/${pkgbase%-git}"
    cmake -Bbuild -DCMAKE_INSTALL_PREFIX=/usr \
          -DCMAKE_BUILD_TYPE=None \
          -GNinja

    ninja -C build
}

package_mfgtools-git() {
    provides=('uuu' 'mfgtool')
    conflicts=(${pkgname%-git})

    cd "${srcdir}/${pkgname%-git}/build"
     DESTDIR="$pkgdir/" ninja -C "${srcdir}/${pkgname%-git}/build" install
    install -Dm0644 "${srcdir}/uuu-complete.bash" "${pkgdir}/etc/bash_completion.d/uuu-complete.bash"
    install -Dm0644 "${srcdir}/${pkgname%-git}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname%-git}/LICENSE"
    install -dm0755  "${pkgdir}/etc/udev/rules.d/"
    ./uuu/uuu -udev > "${pkgdir}/etc/udev/rules.d/70-uuu.rules"
}

package_mfgtools-doc-git() {
    pkgdesc+=" (doc)"
    depends=(asciidoc
            dblatex
            findutils
            coreutils)
    provides=(${pkgname%-git})
    conflicts=(${pkgname%-git})

    cd "${srcdir}/${pkgname%-git}/"
    find . -type f -name "*.asciidoc" -exec sh -c 'mv "$0" "${0%.asciidoc}"' {} \;
    sed -i 's|=====|====|g' Release-Notes
    echo "<revhistory>" > UUU-docinfo.xml
    git log -n25 --reverse --format="format:<revision><revnumber>%h</revnumber><date>%cd</date><authorinitials>%an</authorinitials><revremark>%s</revremark></revision>" >> UUU-docinfo.xml
    echo "</revhistory>" >> UUU-docinfo.xml
    a2x -L -a docinfo UUU

    install -Dm0644 "${srcdir}/${pkgname%-git}/UUU.pdf" -t "${pkgdir}/usr/doc/${pkgname%-git}/"
}
