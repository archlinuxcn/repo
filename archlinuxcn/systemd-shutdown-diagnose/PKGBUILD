# Maintainer: Jiachen Yang <farseerfc@gmail.com>
pkgname=systemd-shutdown-diagnose
pkgver=6
pkgrel=1
pkgdesc="help to diagnose shutdown sequence for systemd"
arch=(any)
url="http://github.com/farseerfc/systemd-shutdown-diagnose"
license=('GPL2')
depends=()
source=('analyze-shutdown'
    'diagnose.shutdown'
    'shutdown-diagnose.service'
    'start-diagnose-shutdown'
)
sha512sums=('feb9d7a5ab06a6d89026564041aff0524d20594befa9e4ba628340fcb34a16e6bacdb1c99425e27d5335f5019f2a1c03fc1565bd88e7115241beea49ebb800ac'
            '803db23f991b1672f9c2e05d9316eb870e261e9c5f7bc56019511b946ce6086bb52083be92070bdbc08bf23130aa87ae7af0bf3d44084c33753a3602cde76a14'
            '26faec19537be2d4dad83e16a3557d1ab20f71a3f66abbfb8725e7fd9233fef6df2c21c81f5c48c48963746d8b319483615a25ae1fb49f8b3667f30e6b1418ec'
            '2ee770dce7cbf95d07b49e24522c6be2d7dd8f3cbe88097d6b27a9ea05052525ef58ef6c2f95bf09bcbc38db46918098faf13655c0f6853b3057dac9ec10e6bb')

package() {
    install -Dm755 diagnose.shutdown "$pkgdir/usr/lib/systemd/system-shutdown/diagnose.shutdown"
    install -Dm755 start-diagnose-shutdown "$pkgdir/usr/bin/start-diagnose-shutdown"
    install -Dm755 analyze-shutdown "$pkgdir/usr/bin/analyze-shutdown"
    install -Dm644 shutdown-diagnose.service "$pkgdir/usr/lib/systemd/system/shutdown-diagnose.service"
}
