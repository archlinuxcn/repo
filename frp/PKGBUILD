# Maintainer: Vimsucks <dev@vimsucks.com>

pkgname=frp
pkgver=0.19.1
pkgrel=1
pkgdesc="A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet."
license=('Apache')
url="https://github.com/fatedier/frp"
arch=('x86_64' 'i686' 'arm')
source=(frps.service frpc.service frps@.service frpc@.service)
source_x86_64=("https://github.com/fatedier/frp/releases/download/v${pkgver}/frp_${pkgver}_linux_amd64.tar.gz")
source_i686=("https://github.com/fatedier/frp/releases/download/v${pkgver}/frp_${pkgver}_linux_386.tar.gz")
source_arm=("https://github.com/fatedier/frp/releases/download/v${pkgver}/frp_${pkgver}_linux_arm.tar.gz")
md5sums=('6f9c6681357f3f984983457151d7f0c5'
         'e3bfa7c428433fa6cbb5aa64515d8899'
         '50364b050ca08f47b7afe305f528eaa2'
         '7aaf36865c656232b441e7bbaf2993dd')
md5sums_x86_64=('0a323dc60d2c93fd5956ac0218929f4e')
md5sums_i686=('a5c1f33b6afd3453369a5677c49ae9df')
md5sums_arm=('1f50d2cbd5436a05cc9a6c2b66ece05c')
install=$pkgname.install

package() {
    case $CARCH in
        x86_64)ARCH=amd64
            ;;
        i686)ARCH=386
            ;;
        arm)ARCH=arm
            ;;
    esac
    frpdir=$srcdir/frp_${pkgver}_linux_${ARCH}

    mkdir -p $pkgdir/usr/bin
    install -m755  $frpdir/frpc $pkgdir/usr/bin/frpc
    install -m755  $frpdir/frps $pkgdir/usr/bin/frps

    mkdir -p $pkgdir/etc/frp
    install -Dm644 $frpdir/frpc.ini $pkgdir/etc/frp/frpc.ini
    install -Dm644 $frpdir/frpc_full.ini $pkgdir/etc/frp/frpc_full.ini
    install -Dm644 $frpdir/frps.ini $pkgdir/etc/frp/frps.ini
    install -Dm644 $frpdir/frps_full.ini $pkgdir/etc/frp/frps_full.ini

    install -Dm644 $frpdir/LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE

    install -Dm644 frps.service  $pkgdir/usr/lib/systemd/system/frps.service
    install -Dm644 frpc.service  $pkgdir/usr/lib/systemd/system/frpc.service
    install -Dm644 frps@.service  $pkgdir/usr/lib/systemd/system/frps@.service
    install -Dm644 frpc@.service  $pkgdir/usr/lib/systemd/system/frpc@.service
}
