# Maintainer: Kimiblock Moe
# Contributor: HurricanePootis <hurricanepootis@protonmail.com>
pkgname=an-anime-game-launcher-bwrap
pkgver=3.15.6
pkgrel=1
pkgdesc="A Launcher for a specific anime game with auto-patching, discord rpc and time tracking"
arch=('x86_64')
provides=('an-anime-game-launcher' 'an-anime-game-launcher-portable')
conflicts=('an-anime-game-launcher')
url="https://github.com/an-anime-team/an-anime-game-launcher"
license=('GPL-3.0-only')
depends=('gtk4' 'libadwaita' 'glibc' 'hicolor-icon-theme' 'gcc-libs' 'glib2'
	 'pango' 'xz' 'bzip2' 'cairo' 'p7zip' 'portable' 'protobuf')
makedepends=('cargo' 'git')
optdepends=(
	 'mangohud: FPS Overlay'
	 'gamescope: Micro-Compositor'
	 'gamemode: CPU Scaling Control')
source=("git+$url.git"
	"portable-config"
	"start.sh")
sha256sums=('SKIP'
            '4acf6359feeeb0b191cdad9534f2ff8af9b5dcfc0835b65002799bc4ca919017'
            'f2bc03c3d06aac59d568381fe0babf13dc9aa4ab99a0bb04b696918475561ccd')

prepare() {
	cd "$srcdir/an-anime-game-launcher"
	export RUSTUP_TOOLCHAIN=stable
    	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "$srcdir/an-anime-game-launcher"
    	export RUSTUP_TOOLCHAIN=stable
    	export CARGO_TARGET_DIR=target
	export CFLAGS+=" -ffat-lto-objects"
    	cargo build --frozen --release --target-dir target
}

package() {
	cd "$srcdir/an-anime-game-launcher"
	install -Dm755 "target/release/anime-game-launcher" "$pkgdir/usr/bin/an-anime-game-launcher"
	install -Dm644 "assets/anime-game-launcher.desktop" "$pkgdir/usr/share/applications/an-anime-game-launcher.desktop"
	install -Dm644 "assets/images/icon.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/moe.launcher.an-anime-game-launcher.png"
	install -dm755 "$pkgdir/usr/share/pixmaps"
	ln -s "/usr/share/icons/hicolor/512x512/apps/moe.launcher.an-anime-game-launcher.png" "$pkgdir/usr/share/pixmaps/an-anime-game-launcher.png"
	sed -i 's/Exec=AppRun/Exec=an-anime-game-launcher-bwrap/g' "$pkgdir/usr/share/applications/an-anime-game-launcher.desktop"
	sed -i 's/Icon=icon/Icon=an-anime-game-launcher/g' "$pkgdir/usr/share/applications/an-anime-game-launcher.desktop"
	echo "StartupWMClass=moe.launcher.an-anime-game-launcher" >> "$pkgdir/usr/share/applications/an-anime-game-launcher.desktop"
	echo "X-Flatpak-Tags=Games;" >> "$pkgdir/usr/share/applications/an-anime-game-launcher.desktop"
	echo "X-Flatpak=moe.launcher.an-anime-game-launcher" >> "$pkgdir/usr/share/applications/an-anime-game-launcher.desktop"
	install -Dm755 "$srcdir/portable-config" "$pkgdir/usr/lib/portable/info/moe.launcher.an-anime-game-launcher/config"
	install -Dm755 "$srcdir/start.sh" "$pkgdir/usr/bin/an-anime-game-launcher-bwrap"
	mv "${pkgdir}/usr/share/applications/an-anime-game-launcher.desktop" "${pkgdir}/usr/share/applications/moe.launcher.an-anime-game-launcher.desktop"
}
