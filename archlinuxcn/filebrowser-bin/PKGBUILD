# Maintainer: axionl <axionl@aosc.io>
# Contributor: Sherlock Holo <sherlockya(at)gmail.com>
pkgname=filebrowser-bin
pkgver=2.24.2
pkgrel=1
pkgdesc="Web File Manager which can be used as a middleware or standalone app."
arch=('x86_64' 'aarch64')
url="https://github.com/filebrowser/filebrowser"
license=('Apache')
depends=('glibc')
provides=("filebrowser")
conflicts=("filebrowser")
backup=("etc/filebrowser/filebrowser.conf")
install="${pkgname}.install"

source=('filebrowser.service' 'filebrowser@.service' 'filebrowser-bin.install'
        'filebrowser.sysusers' 'filebrowser.tmpfiles'
        'https://raw.githubusercontent.com/hacdias/filebrowser/master/LICENSE')
source_x86_64=("linux-amd64-filebrowser-${pkgver}.tar.gz::https://github.com/filebrowser/filebrowser/releases/download/v${pkgver}/linux-amd64-filebrowser.tar.gz")
source_aarch64=("linux-aarch64-filebrowser-${pkgver}.tar.gz::https://github.com/filebrowser/filebrowser/releases/download/v${pkgver}/linux-arm64-filebrowser.tar.gz")

sha256sums=('1d85acca4ca9bcdb6767ff60891d6e0a4e9c324fc50bed1231e8c891eb9c4420'
            '29031d87f8294889ea33658570422406ca8c13367ae20cbcc1f98132df83ea14'
            '3495234f011491a1d448af24bfe8af8018bb4c5b1a4c4ef53651fb068d9801c4'
            '6246fbeac57750e146216892ed6eb1d43a995f987bb89ef12bcbfb3963f5aa2d'
            'fd3da1de58e98185e0043070f55b46a86a78b9ebcdda949d0cd8a83e9b0b230c'
            '1fc20cab3a7d67d7997126a98dd151a362dc4600201ca37fd608b959d25985db')
sha256sums_x86_64=('03dc6636673116e50c5fd59e2798f9791d55984f373d965a3a8573fbe1e0411e')
sha256sums_aarch64=('8c0ca7c5c2a5f0cdd631631d0edb775aa9a7dd918f27e97eaa804a1a3f778749')

package() {
    install -Dm644 "${srcdir}/filebrowser.sysusers" "${pkgdir}/usr/lib/sysusers.d/filebrowser.conf"
    install -Dm644 "${srcdir}/filebrowser.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/filebrowser.conf"
    install -Dm644 "filebrowser.servic"e -t "${pkgdir}/usr/lib/systemd/system/"
    install -Dm644 "filebrowser@.service" -t "${pkgdir}/usr/lib/systemd/system/"
    install -Dm755 "LICENSE" -t "${pkgdir}/usr/share/licenses/filebrowser-bin/"
    install -Dm755 "${srcdir}/filebrowser" -t "${pkgdir}/usr/bin/"
}

# vim set: ts=4 sw=4 et:
