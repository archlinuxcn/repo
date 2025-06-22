# Maintainer: Kimiblock Moe
# Contributor: Giovanni Harting <anonfunc@archlinux.org>
# Contributor: Sefa Eyeoglu <contact@scrumplex.net>
# Contributor: txtsd <aur.archlinux@ihavea.quest>
# Contributor: seth <getchoo at tuta dot io>
# Contributor: Lenny McLennington <lennymclennington@protonmail.com>
# Contributor: Elijah Gregg <lovetocode999@tilde.team>
# Contributor: Miko <mikoxyzzz@gmail.com>
# Contributor: Cheru Berhanu <aur attt cheru doot dev>
# Contributor: dada513 <dada513@protonmail.com>

pkgname=prismlauncher-bwrap
pkgver=9.4
pkgrel=3
provides=(prismlauncher prismlauncher-portable)
conflicts=(prismlauncher)
pkgdesc="Minecraft launcher with ability to manage multiple instances. Sandboxed by portable."
arch=(x86_64)
url='https://prismlauncher.org'
license=('GPL-3.0-only AND LGPL-3.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND MIT AND LicenseRef-Batch AND OFL-1.1')
depends=(
  glibc
  gcc-libs
  java-runtime
  libgl
  qt6-base
  qt6-5compat
  qt6-svg
  qt6-imageformats
  qt6-networkauth
  quazip-qt6
  zlib
  hicolor-icon-theme
  tomlplusplus
  cmark
  glfw
  portable
  xorg-xrandr
  openal
  flite
)
makedepends=(cmake3 extra-cmake-modules git jdk17-openjdk scdoc ghc-filesystem gamemode desktop-file-utils)
optdepends=('visualvm: Profiling support')
source=("git+https://github.com/PrismLauncher/PrismLauncher#tag=${pkgver}"
        {lionshead,batch,mdi}.license
        portable-config
        start.sh)
b2sums=('30988cbda54c393e25589d898418d0c468a9cab765a3dc108cae1ceea97d91603e8358c245eae44ff23b155289ec4fede95ca888793dd6de58874d2de817b7cd'
        'e7427b8289a8b524da96f884c327bce0fce25df6643b49bcca11cb7b38ab44bee8ad7418d159279074ff205ddd5d7beb922b32c743fd1504928dbd1cceada586'
        '093912695909a4d78c0d3e1faef3f393c1f2183ce0728d9faed65fcd3eac55da160b91bd95be9e935a738a4fdad7b592e73a9a09d5ed5e904b03a810e53e4942'
        '6bec000f725457b2d559a610b8b6a7c4c77b3b60510d089243463b32797254549ed1def83df562294664b7ddbc2b5b6edaae432c66b49cb7dd35aaaf174acec9'
        'd7fbe68f3f6963cd30296496f10cc808da06d942abbeca6e7c9095b4f7cc7da891b157b1ae578d2daa8def9c2fe25fb455285f749f2414acde0bb8e833c3bdae'
        '417edca8819febc409431dee12ccb1d9466a274ce28d8bde554e6f28bfe352372ee0d88c5b53ebf95c9d13d0f91e9ff3b363980687fb04d0adf010fa0f8a4e26')

function prepare() {
	cd PrismLauncher
	git submodule init
	git submodule update --init --recursive --depth 1
}

function build() {
	cd PrismLauncher
	export PATH="/usr/lib/jvm/java-17-openjdk/bin/:$PATH"

	cmake3 -DCMAKE_BUILD_TYPE= \
		-DCMAKE_INSTALL_PREFIX="/usr" \
		-DLauncher_BUILD_PLATFORM="archlinux" \
		-DLauncher_QT_VERSION_MAJOR="6" \
		-DLauncher_ENABLE_JAVA_DOWNLOADER=OFF \
		-Bbuild -S.
	cmake3 --build build
}

check() {
	cd PrismLauncher/build
	ctest .
}

package() {
	# licenses
	install -Dm644 lionshead.license -t "$pkgdir"/usr/share/licenses/$pkgname/
	install -Dm644 batch.license -t "$pkgdir"/usr/share/licenses/$pkgname/
	install -Dm644 mdi.license -t "$pkgdir"/usr/share/licenses/$pkgname/
	cd PrismLauncher/build
	DESTDIR="$pkgdir" cmake3 --install .
	install -Dm755 \
		"${srcdir}/start.sh" \
		"${pkgdir}/usr/bin/prismlauncher-bwrap"
	install -Dm755 \
		"${srcdir}/portable-config" \
		"${pkgdir}/usr/lib/portable/info/org.prismlauncher.PrismLauncher/config"
	desktop-file-edit \
		--set-key=Exec \
		--set-value='env _portableConfig=org.prismlauncher.PrismLauncher portable -- %U' \
		"${pkgdir}/usr/share/applications/org.prismlauncher.PrismLauncher.desktop"
	install -d "${pkgdir}/usr/lib/prismlauncher-bwrap/prismlauncher"
	mv "${pkgdir}/usr/bin/prismlauncher" "${pkgdir}/usr/lib/prismlauncher-bwrap/prismlauncher"
	ln -srf "${pkgdir}/usr/bin/prismlauncher-bwrap" "${pkgdir}/usr/bin/prismlauncher"
}
