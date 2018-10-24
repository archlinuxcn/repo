# Maintainer: jtmb <packaging at technologicalwizardry dot com>
pkgname=msbuild-stable
_pkgver=15.8+xamarinxplat.2018.07.31.22.43-0xamarin5+ubuntu1404b1
pkgver=${_pkgver//[+-]/_}
pkgrel=3
pkgdesc="Xamarin implementation of the Microsoft build system"
arch=('x86_64')
depends=('mono>=5.0.0')
provides=('msbuild')
conflicts=('msbuild')
url="https://github.com/mono/msbuild"
license=('MIT')
source=("msbuild-amd64-v${_pkgver}.deb::http://download.mono-project.com/repo/ubuntu/pool/main/m/msbuild/msbuild_${_pkgver}_all.deb")
sha256sums=('93e71f85c16c896ce6f459fb1d61e16d90db725d288bc6635332ac50e9886ced')

package() {
    cd "${srcdir}"

    bsdtar xf data.tar.xz
    chmod -R g-w usr
    mv usr "${pkgdir}"
}
