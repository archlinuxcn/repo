# Maintainer: Cyano Hao <c@cyano.cn>

_pkgname=vkd3d-proton
pkgname=$_pkgname-bin
pkgver=2.13
pkgrel=1
pkgdesc="Direct3D 12 to Vulkan translation library (Windows DLL binary files)"
url="https://github.com/HansKristian-Work/vkd3d-proton"
license=('LGPL')
arch=('x86_64')
depends=('vulkan-icd-loader')
optdepends=('lib32-vulkan-icd-loader: 32-bit Windows application support')
# do not provide vkd3d and lib32-vkd3d intentionally: providing them may break deepin-wine apps.
provides=('vkd3d-proton')
conflicts=('vkd3d-proton')
options=(!strip)
source=("https://github.com/HansKristian-Work/$_pkgname/releases/download/v$pkgver/$_pkgname-$pkgver.tar.zst")
sha256sums=('f7163187a69e19b7c57d4e2f10ed627e75d6e93eef52d119378572d26a9ce33a')

package() {
	install -D "$_pkgname-$pkgver"/x86/* -t "$pkgdir/usr/share/vkd3d-proton/x86"
	install -D "$_pkgname-$pkgver"/x64/* -t "$pkgdir/usr/share/vkd3d-proton/x64"
	install "$_pkgname-$pkgver"/setup_vkd3d_proton.sh -t "$pkgdir/usr/share/vkd3d-proton/"
	install -d "$pkgdir/usr/bin"
	ln -s /usr/share/vkd3d-proton/setup_vkd3d_proton.sh "$pkgdir/usr/bin/setup_vkd3d_proton"
}
