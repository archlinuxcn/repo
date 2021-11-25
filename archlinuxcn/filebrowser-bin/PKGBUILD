# Maintainer: axionl <axionl@aosc.io>
# Contributor: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=filebrowser-bin
pkgver=2.19.0
pkgrel=1
pkgdesc="Web File Manager which can be used as a middleware or standalone app."
arch=('x86_64' 'aarch64')
url="https://github.com/filebrowser/filebrowser"
license=('Apache')
#depends=('glibc')
provides=("filebrowser")
conflicts=("filebrowser")
install="${pkgname}.install"

source=('filebrowser@.service' 'filebrowser-bin.install'
        'https://raw.githubusercontent.com/hacdias/filebrowser/master/LICENSE')
source_x86_64=("linux-amd64-filebrowser-${pkgver}.tar.gz::https://github.com/filebrowser/filebrowser/releases/download/v${pkgver}/linux-amd64-filebrowser.tar.gz")
source_aarch64=("linux-aarch64-filebrowser-${pkgver}.tar.gz::https://github.com/filebrowser/filebrowser/releases/download/v${pkgver}/linux-arm64-filebrowser.tar.gz")

sha256sums=('79a1fdb1f0b26f211242f1fdb6f3478a56890a721fe324ea7ade2e8f9a351b38'
            '8a423af0707ac37b15ca425ec097b3d98aecd08238f7599ae9dfcce31c8cbb32'
            '1fc20cab3a7d67d7997126a98dd151a362dc4600201ca37fd608b959d25985db')
sha256sums_x86_64=('549bf4f03c0de9ef27b0527900fafdd412e3fbaecb9fcdc8a1dbe357a06e05a8')
sha256sums_aarch64=('67be1fd9c313521da359462ddf92d14d5b084d94d20ec0dc7942648d97705f00')




package() {
    install -Dm644 filebrowser@.service "${pkgdir}/usr/lib/systemd/system/filebrowser@.service"
    install -Dm755 LICENSE "${pkgdir}/usr/share/licenses/filebrowser-bin/LICENSE"
    install -Dm755 "${srcdir}/filebrowser" "${pkgdir}/usr/bin/filebrowser"
}

# vim set: ts=4 sw=4 et:
