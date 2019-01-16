# Maintainer: MadPhysicist <jfoxrabinovitz at gmail dot com>
pkgname=panoply
pkgver=4.10.3
pkgrel=1
pkgdesc='NetCDF, HDF and GRIB Data Viewer by NASA GISS'
arch=('any')
url='http://www.giss.nasa.gov/tools/panoply/'
license=('custom')
groups=('nasa-tools')
depends=('java-runtime>=8'
         'hicolor-icon-theme'
         'desktop-file-utils')
makedepends=('unzip')
optdepends=()
provides=()
conflicts=(panoply-nodesktop)
replaces=()
backup=()
options=()
install=panoply.install
changelog=
source=("http://www.giss.nasa.gov/tools/panoply/download/PanoplyJ-${pkgver}.zip"
        'LICENSES'
        'panoply-script.patch'
        'panoply16.png'
        'panoply32.png'
        'panoply48.png'
        'panoply64.png'
        'panoply128.png'
        'panoply.desktop')
noextract=()
_sha1="$(curl https://www.giss.nasa.gov/tools/panoply/download/Panoply-${pkgver}.sha1.txt 2>/dev/null | grep 'PanoplyJ.*.zip' | grep -o '^[^ ]*')"
sha1sums=("${_sha1}"
          'a83855747414873269e21aaff1a53d13ab5de304'
          '707208d062922b5426303238870e0dd269257697'
          '97c70755c7d87217556de5b2f1012b3be0d375fb'
          'c36f0b5d423d626255be0f2d2cbf3eba72618a36'
          '7becea40d14b5d89a8c4662b84ebe0578a53b1a4'
          '2347bd0a4644781a86950fa740d8621437049b69'
          '6151a1fe4a0a19e7b0145f1f58724b72bc38e8e6'
          '39c9a58c25d8f764c928e9dfe75f4f73bb9198f0')

prepare() {
    cd ${srcdir}/PanoplyJ
    patch -uN -i ../panoply-script.patch || return 1
    unzip -px jars/Panoply.jar gov/nasa/giss/panoply/about/panoply4.png > ../panoply192.png
}

package() {
    install -Dm644 ${srcdir}/LICENSES ${pkgdir}/usr/share/licenses/${pkgname}/LICENSES
    install -d -m755 ${pkgdir}/usr/share/java/panoply
    install -Dm644 ${srcdir}/PanoplyJ/jars/*.jar ${pkgdir}/usr/share/java/panoply
    install -Dm755 ${srcdir}/PanoplyJ/panoply.sh ${pkgdir}/usr/bin/panoply
    install -Dm644 ${srcdir}/panoply16.png ${pkgdir}/usr/share/icons/hicolor/16x16/apps/panoply.png
    install -Dm644 ${srcdir}/panoply32.png ${pkgdir}/usr/share/icons/hicolor/32x32/apps/panoply.png
    install -Dm644 ${srcdir}/panoply48.png ${pkgdir}/usr/share/icons/hicolor/48x48/apps/panoply.png
    install -Dm644 ${srcdir}/panoply64.png ${pkgdir}/usr/share/icons/hicolor/64x64/apps/panoply.png
    install -Dm644 ${srcdir}/panoply128.png ${pkgdir}/usr/share/icons/hicolor/128x128/apps/panoply.png
    install -Dm644 ${srcdir}/panoply192.png ${pkgdir}/usr/share/icons/hicolor/192x192/apps/panoply.png
    install -Dm644 ${srcdir}/panoply.desktop ${pkgdir}/usr/share/applications/panoply.desktop
}
