# Maintainer: Kimiblock Moe

_npmname=vite
pkgname=nodejs-$_npmname
pkgver=8.1.1
pkgrel=1
pkgdesc="Next generation frontend tooling. It's fast!"
arch=(aarch64 x86_64)
url="https://github.com/vitejs/vite"
license=('MIT')
depends=('nodejs' libgcc)
makedepends=('npm')
source=("https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz"
        "${_npmname}-LICENSE::https://raw.githubusercontent.com/vitejs/vite/56eb869a67551a257d20cba00016ea59b1e1a2c4/LICENSE")
noextract=($_npmname-$pkgver.tgz)
sha512sums=('5ffd39fdc4fe5484f2d8078373575eafab26bc6596444b4be213db3d36956e3481bae5a498d3a347a1cfdcdcea7100369c5e951c650f685449c9fb7fd8013d2a'
            '6d9074936683997b5f01e7ca64d88b4242be94a5bb151405654d3d4845cae7c2e4286d1b546b79b26c59866f56fe68b068c68f62f1cd465019fbb6de9abc9957')

package() {
  npm install -g --prefix "${pkgdir}"/usr "${srcdir}"/$_npmname-$pkgver.tgz

  # Non-deterministic race in npm gives 777 permissions to random directories.
  # See https://github.com/npm/npm/issues/9359 for details.
  chmod -R u=rwX,go=rX "${pkgdir}"

  # npm installs package.json owned by build user
  # https://bugs.archlinux.org/task/63396
  chown -R root:root "${pkgdir}"

  install -Dm644 "${srcdir}/${_npmname}-LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
