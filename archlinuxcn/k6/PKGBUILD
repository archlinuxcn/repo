# Maintainer: Jeff Henson <jeff@henson.io>
# Old Maintainer: Andy Nicholson <andrew@anicholson.net>
# Contributors: teutat3s

pkgname=k6
pkgver=0.40.0
pkgrel=1
pkgdesc="A modern load testing tool, using Go and JavaScript"
arch=('x86_64' 'i686')
url="https://github.com/loadimpact/k6"
license=('AGPL3')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/grafana/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('d3e00387c6dda4e53b3816175b8772db53124198d8ceb499c9a1f6b76092df83')

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
	install -vDm 644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"

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
