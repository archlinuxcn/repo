# Maintainer: MadPhysicist <jfoxrabinovitz at gmail dot com>
pkgname=panoply
pkgver=5.7.0
pkgrel=1
pkgdesc='NetCDF, HDF and GRIB Data Viewer by NASA GISS'
arch=('any')
url='http://www.giss.nasa.gov/tools/panoply/'
license=('custom')
groups=('nasa-tools')
depends=('java-runtime>=11'
         'hicolor-icon-theme')
makedepends=('unzip' 'imagemagick')
optdepends=()
provides=()
conflicts=(panoply-nodesktop)
replaces=()
backup=()
options=()
install=panoply.install
changelog=
source=("http://www.giss.nasa.gov/tools/panoply/download/PanoplyJ-${pkgver}.zip"
        "https://www.giss.nasa.gov/tools/panoply/download/Panoply-${pkgver}.sha1.txt"
        'LICENSES'
        'panoply-script.patch'
        'panoply.desktop')
noextract=()
sha1sums=('32460f396631c49e03c3ce896eace243d8ad89d4'
          '1f9738d87eae2368fe960b3923aa9ec3e6c03a2e'
          'a83855747414873269e21aaff1a53d13ab5de304'
          '241ee69031c69598483c27b8580731aa7a468eca'
          '39c9a58c25d8f764c928e9dfe75f4f73bb9198f0')

prepare() {
    _sha1="$(cat Panoply-${pkgver}.sha1.txt 2>/dev/null | grep 'PanoplyJ.*.zip' | grep -o '^[^ ]*')"
    if [ "${sha1sums[0]}" = "$_sha1" ]; then
        echo "Checksum correct. Proceed to build"
    else
        echo "Checksum fail. Please check download!"
        exit 1
    fi
    cd ${srcdir}/PanoplyJ
    patch -uN -i ../panoply-script.patch || return 1
    unzip -px jars/Panoply.jar gov/nasa/giss/panoply/about/panoply_320x320.png > ../panoply320.png
    declare -a StringArray=("16" "32" "48" "64" "128" "192")
    for i in "${StringArray[@]}"; do
        echo "Resizing icon to ${i}x${i}"
        convert ../panoply320.png -resize ${i}x${i} ../panoply${i}.png
    done
}

package() {
    install -Dm644 ${srcdir}/LICENSES ${pkgdir}/usr/share/licenses/${pkgname}/LICENSES
    install -d -m755 ${pkgdir}/usr/share/java/panoply
    install -Dm644 ${srcdir}/PanoplyJ/jars/*.jar ${pkgdir}/usr/share/java/panoply
    install -Dm755 ${srcdir}/PanoplyJ/panoply.sh ${pkgdir}/usr/bin/panoply
    for i in "${StringArray[@]}"; do
        install -Dm644 ${srcdir}/panoply${i}.png ${pkgdir}/usr/share/icons/hicolor/${i}x${i}/apps/panoply.png
    done
    install -Dm644 ${srcdir}/panoply.desktop ${pkgdir}/usr/share/applications/panoply.desktop
}
