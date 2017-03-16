# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Simon Legner <Simon.Legner@gmail.com>

pkgname=bazel
pkgver=0.4.5
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
sha512sums=('bc70e379a9f6f962440d05d4a706959461690e28a943833e17d6e2b7e3cd7dd2344f329f72d833ec5104334a71764fde195e50b09a582ae7c1b89bd62822943b'
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
