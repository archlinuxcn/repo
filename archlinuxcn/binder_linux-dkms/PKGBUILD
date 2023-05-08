# Maintainer: Sick Codes <info at sick dot codes>
# Maintainer: Christian Hoff <https://github.com/choff>
# Contributor: Tobias Martin <tm-x at gmx dot net>

_commit=44dc351409c6e1665c0dd3c7a32c8e79a2950a4e

pkgname=binder_linux-dkms
pkgver=6.3
pkgrel=1
arch=("x86_64")
url='https://github.com/choff/anbox-modules'
pkgdesc='Android kernel driver fork by @choff in DKMS format, binder only.'
license=("GPL3")
conflicts=("anbox-modules-dkms")
depends=("dkms")
makedepends=("git")
source=(
    "git+${url}.git#commit=${_commit}"
    # Fix build on 6.3 kernel
    # See https://github.com/choff/anbox-modules/pull/10
    "10-6.3.diff::https://github.com/choff/anbox-modules/pull/10.diff")
sha256sums=('SKIP'
            '7bfae09412b8ed3835c2b91a775f5e1dff46ce2e05824cc203a14a52491cecec')
prepare(){
    cd "${srcdir}/anbox-modules"
    for diff_file in "${srcdir}/"*.diff
    do
        git apply "$diff_file"
    done
}
package(){
    install -dm755 "${pkgdir}/usr/src/binder-1"
    cp -r "${srcdir}/anbox-modules/binder/"* "${pkgdir}/usr/src/binder-1/"
}
