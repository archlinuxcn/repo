# Maintainer: Tomas Kral <tomas.kral@gmail.com>
# Contributor: Sergi Jimenez <sjr@redhat.com>

pkgname=minishift-bin
_minishift_version=1.21.0
pkgver=${_minishift_version//-/_}
pkgrel=2
pkgdesc="Tool that makes it easy to run OpenShift locally."
url="https://github.com/minishift/minishift"
license=('Apache')
arch=('x86_64')
makedepends=()
provides=('minishift')

optdepends=(
  'virtualbox: to use minishift with VirtualBox virtualization'
  'docker-machine-kvm: to use minishisft with KVM virtualization'
)

source=(https://github.com/minishift/minishift/releases/download/v${_minishift_version}/minishift-${_minishift_version}-linux-amd64.tgz)
sha256sums=('21e081d971197cc8704480b0cff5ac2db2e7cea5ec74f3f94e12f43804f48f25')


prepare() {
    tar -xf minishift-${_minishift_version}-linux-amd64.tgz
}

package() {
  install -Dm755 "${srcdir}/minishift-${_minishift_version}-linux-amd64/minishift" "${pkgdir}/usr/bin/minishift"
  install -Dm644 "${srcdir}/minishift-${_minishift_version}-linux-amd64/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
