pkgname=nvidia-texture-tools
pkgver=2.0.8
pkgrel=4
pkgdesc="GPU-accelerated Texture Tools with support for DirectX 10 texture formats"
arch=('i686' 'x86_64')
url="http://code.google.com/p/nvidia-texture-tools/"
license=('MIT')
depends=('libpng' 'libjpeg' 'libtiff' 'openexr')
makedepends=('cmake')
source=(http://nvidia-texture-tools.googlecode.com/files/${pkgname}-${pkgver}-1.tar.gz
		nvidia-texture-tools-2.0.8-add-pthread.patch
		issue139.patch
		r1157.patch
		03-kfreebsd-bfs.patch
		04-fix-gcc4.7-build.patch
		06-fix-libpng1.5-build.patch
		07-fix-valgrind.patch
		nvidia-texture-tools-2.0.8-wordsize.patch
		)

md5sums=('7449c95ca1583b512561c83c5a5f401c'
		'55d011f08ef9c924a7fd5b2c8b9e2c85'
		'c67927632740fbea5efb02969b97b52c'
		'a044c7cae45e8c9946b4349e34793656'
		'72c8ebc16fae0c24306391973188a367'
		'd60970ba621e82a22419b3f9ce930df2'
		'd98b9dd3524b426edc0693f8220b6a8d'
		'ce7d1e7103314500563dd40f18a54a04'
		'ef1e0896247b27f482eeb8b71378a551')

build() {
	cd ${srcdir}/${pkgname}

	# add -pthread to linker, r1211
	patch -p1 -i ${srcdir}/nvidia-texture-tools-2.0.8-add-pthread.patch
	# Fix aliasing bug, r1167
	patch -p1 -i ${srcdir}/issue139.patch
	# patch for CUDA 3.0, this pkg doesn't require cuda, but be nice
	patch -p2 -i ${srcdir}/r1157.patch
	# more patches from debian
	# not needed, but makes it easier to share patches with upstream and others
	patch -p1 -i ${srcdir}/03-kfreebsd-bfs.patch 
	patch -p1 -i ${srcdir}/04-fix-gcc4.7-build.patch
	# 5th patch is identical with issue139.patch
	patch -p1 -i ${srcdir}/06-fix-libpng1.5-build.patch
	patch -p1 -i ${srcdir}/07-fix-valgrind.patch
	# patch for libtiff 4.0, from fedora
	patch -p1 -i ${srcdir}/nvidia-texture-tools-2.0.8-wordsize.patch

	./configure --prefix=/usr --release
	make
}

package() {
	cd ${srcdir}/${pkgname}
	make DESTDIR=${pkgdir} install
}
