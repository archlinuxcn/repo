# Maintainer: Kimiblock Moe

pkgname=ntfysh
pkgver=2.14.0
pkgrel=2
pkgdesc="Send push notifications to your phone or desktop using PUT/POST "
arch=("x86_64")
url="https://ntfy.sh"
license=('GPL2')
makedepends=('go' 'git' 'npm' 'nodejs')
conflicts=(
	ntfysh-bin
	ntfy
	)
backup=('etc/ntfy/server.yml' 'etc/ntfy/client.yml')
source=(
	"$pkgname::git+https://github.com/binwiederhier/ntfy.git#tag=v$pkgver"
	"ntfy.sysusers"
        )
b2sums=('410ee1098943de738300f2e0f119c7de218c8ae356244f9b1bd26451fcfb61610b2d58b402f4d98ecee80baf0864968c7877976ace312e9a459161efe0e1bf5f'
        '958bdfc80eeb8ed62508593a94b379d7c099373a4ed2af3eaeedebdca05519378e2bc20940950db4f848be0575cebe16bcb79b794133e8f4467418f8e34278ca')

build() {
	cd "${pkgname}"

    mkdir -p "$srcdir/fakehome"
    OLD_HOME=$HOME
    HOME="$srcdir/fakehome"

    # web-deps target
    (
        set -e
        cd web
        npm install

        # web-build target
        npm run build
        mv build/index.html build/app.html
        rm -rf ../server/site
        mv build ../server/site
        rm ../server/site/config.js
    )

	# # cli-deps-static-sites target
	# mkdir -p server/docs server/site
	# touch server/docs/index.html server/site/app.html

	# cli-linux-server target
	mkdir -p dist/ntfy_linux_server server/docs

	touch server/docs/index.html

	export GOPATH="$HOME/go"
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"

	export CGO_ENABLED=1
	go build \
		-trimpath \
		-buildmode=pie \
		-mod=readonly \
		-modcacherw \
		-o dist/ntfy_linux_server/ntfy \
		-tags sqlite_omit_load_extension,osusergo,netgo \
		-ldflags \
		"-linkmode=external -extldflags=-static -s -w -X main.version=${pkgver} -X main.commit=$(git rev-parse --short HEAD) -X main.date=$(date +%s)"

    HOME=$OLD_HOME
}

package() {
	cd "${pkgname}"

	install -Dm755 "dist/ntfy_linux_server/ntfy" 	"${pkgdir}/usr/bin/ntfy"
	install -Dm644 "client/ntfy-client.service" 	"${pkgdir}/usr/lib/systemd/system/ntfy-client.service"
	install -Dm644 "client/client.yml" 		"${pkgdir}/etc/ntfy/client.yml"
	install -Dm644 "server/ntfy.service" 		"${pkgdir}/usr/lib/systemd/system/ntfy.service"
	install -Dm644 "server/server.yml" 		"${pkgdir}/etc/ntfy/server.yml"
	install -Dm644 "README.md" 			"${pkgdir}/usr/share/doc/${pkgname}/README.md"
	install -Dm644 "LICENSE" 			"${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	install -Dm644 "${srcdir}/ntfy.sysusers" 	"${pkgdir}/usr/lib/sysusers.d/ntfy.conf"
}
