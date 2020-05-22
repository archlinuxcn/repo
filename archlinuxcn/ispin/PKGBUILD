# Maintainer: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Ghost of Kendo <ghostofkendo at gmail dot com>

pkgname=ispin
pkgver=6.5.0
pkgrel=1
pkgdesc='New Tcl/Tk GUI for Spin replacing xSpin'
arch=('any')
url='https://spinroot.com/'
license=('custom:SPIN')
depends=('spin>=6.0' 'tk>=8.5' 'gcc')
optdepends=('graphviz: recommended, provides dot tool for automata view'
            'curl: for version check information')
source=("https://github.com/nimble-code/Spin/archive/version-${pkgver}.tar.gz"
	      LICENSE)
b2sums=('d4cd147b8d8204e9c092865e49b59426c49e225578d64818e88eed44fa3a660346dfa424315d4c55f642c00a099337aff86aea5b0cf019b9f59059b636f32250'
        '4b7b009a078a13379dbc59e3cb4297b5f9710acc94e4b4dba0169e4407991fb9db3c75c80390c69a6d22cf022fae2cd0463d46474ceb60110688ee8a4c9859fc')

build() {
  cd Spin-version-${pkgver}/Src
  make
}

package() {
  install -Dm755 Spin-version-${pkgver}/optional_gui/${pkgname}.tcl "${pkgdir}"/usr/bin/${pkgname}
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
