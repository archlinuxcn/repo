# Maintainer: Jeff Henson <jeff@henson.io>
# Old Maintainer: Andy Nicholson <andrew@anicholson.net>
# Contributors: teutat3s

pkgname=k6
pkgver=0.46.0
pkgrel=1
pkgdesc="A modern load testing tool, using Go and JavaScript"
arch=('x86_64' 'i686')
url="https://github.com/grafana/k6"
license=('AGPL3')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('8f3c7ddc9e4df1c6df745be9ca0dcc81188783afac76c8bb45c16a2079299c63')

build() {
	cd "${pkgname}-${pkgver}"
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
	go build -o ${pkgname}
}

package() {
	cd "${pkgname}-${pkgver}"
	install -vDm 755 ${pkgname} -t "${pkgdir}/usr/bin/"
	install -vDm 644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
	install -vDm 644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}/"

	# build bash completions
	mkdir -p "${pkgdir}/usr/share/bash-completion/completions"
	./${pkgname} completion bash > "${pkgdir}/usr/share/bash-completion/completions/k6"

	# build zsh completions
	mkdir -p "${pkgdir}/usr/share/zsh/site-functions"
	./${pkgname} completion zsh > "${pkgdir}/usr/share/zsh/site-functions/_k6"

	# build fish completions
	mkdir -p "${pkgdir}/usr/share/fish/vendor_completions.d/"
	./${pkgname} completion fish > "${pkgdir}/usr/share/fish/vendor_completions.d/k6.fish"
}
