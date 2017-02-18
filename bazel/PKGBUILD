# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Simon Legner <Simon.Legner@gmail.com>

pkgname=bazel
pkgver=0.4.4
pkgrel=1
pkgdesc='Correct, reproducible, and fast builds for everyone'
arch=('i686' 'x86_64')
license=('Apache')
url='https://bazel.io/'
depends=('java-environment>=8' 'libarchive' 'zip' 'unzip')
makedepends=('git' 'protobuf')
options=('!distcc' '!strip')
source=(https://github.com/bazelbuild/bazel/releases/download/${pkgver}/bazel-${pkgver}-dist.zip
        https://github.com/bazelbuild/bazel/releases/download/${pkgver}/bazel-${pkgver}-dist.zip.sig)
sha512sums=('0ca24cbd3894f7db657e50b63ccd2613530eca5df607acb71642f9d33196ee3b1b21244541880cd27ff87050bc189f1b65b22f89aad73c6b25efbe9a5c86d114'
            'SKIP')
validpgpkeys=('71A1D0EFCFEB6281FD0437C93D5919B448457EE0')

build() {
  ./compile.sh
  ./output/bazel build scripts:bazel-complete.bash
  cd output
  ./bazel shutdown
}

package() {
  pwd
  install -Dm755 ${srcdir}/output/bazel ${pkgdir}/usr/bin/bazel
  install -Dm755 ${srcdir}/bazel-bin/scripts/bazel-complete.bash ${pkgdir}/etc/bash_completion.d/bazel-complete.bash
  mkdir -p ${pkgdir}/opt/bazel/
  for d in examples third_party tools; do
    cp -r ${srcdir}/${d} ${pkgdir}/opt/bazel/
  done
}
