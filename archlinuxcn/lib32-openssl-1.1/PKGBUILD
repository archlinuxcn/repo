# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

pkgname=lib32-openssl-1.1
_ver=1.1.1w
pkgver=${_ver/[a-z]/.${_ver//[0-9.]/}}
pkgrel=5
pkgdesc='The Open Source toolkit for Secure Sockets Layer and Transport Layer Security'
arch=('x86_64')
url='https://www.openssl.org'
license=('OpenSSL')
makedepends=('lib32-gcc-libs') #Used for test binaries
depends=('lib32-glibc' 'openssl-1.1')
source=("https://www.openssl.org/source/openssl-${_ver}.tar.gz"
        'ca-dir.patch'
        CVE-2023-5678.patch
        CVE-2024-0727-1.patch
        CVE-2024-0727-2.patch
        CVE-2024-2511.patch
        CVE-2024-4741.patch
        CVE-2024-5535-1.patch
        CVE-2024-5535-2.patch
        CVE-2024-5535-3.patch
        CVE-2024-5535-4.patch
        CVE-2024-5535-5.patch
        CVE-2024-5535-6.patch
        CVE-2024-5535-7.patch
        CVE-2024-5535-8.patch
        CVE-2024-9143.patch
        CVE-2024-13176.patch
        CVE-2025-9230.patch
        CVE-2025-68160.patch
        CVE-2025-69418.patch
        CVE-2025-69420.patch
        CVE-2025-69421.patch
        CVE-2026-22795_CVE-2026-22796.patch
        # https://git.almalinux.org/rpms/openssl/src/branch/c8s
        CVE-2025-69419-1.patch
        CVE-2025-69419-2.patch
      )
b2sums=('2fdba6ca0188928ab2f74e606136afca66cfa0467170fa6298ef160b64ac6fdcad1e81e5dd14013ce0e9921d0f7417edec531cd0beaf1196fec704c2c6d48395'
        '6375a8994d95ef5e51d724e62558a25a7ec0632577f4cf99d347fc1cecc133ac2cb1dc55bb872ca6bca0449ed5c27ba72afb10c4c55aced300405b542ccbb808'
        '6eefef93c3bf6d68011dbd27523e42a6de1fbef5673f1c297d1d65a86d5f598a62ed1006af840a0d0522697ad40016bd1c302d15263b0e4c48bb634ee4167487'
        'fc8090b0e887b671cea545c1abd348de77971c505472a0f087752bbccd2204179d14bad5e8ddc700c45dcc8e27062569de7efcc1318f2b52f2aa75046b754a16'
        '3860190c5ca5dd7948e7b2e049c27bc05edba99abb3bbd839777772694f1128db9f9e7480149a2cd6cbef52e83de68a070f64af77c41f303564cbf49173f0711'
        'b113cef5639d5d0867f767097496664aaee2c41fd1ef938211a56f3485096e769bf4820be63e331df33aa6758e2fe29046069ceed24881c74212abfd8578360e'
        '50c300c3f82bf24dd497cad591bbce0c0e5c36b6ed9e98fdc7fc5d211d8dd62b962a57ab8c5cb76adb726e8383c118f256f50313be5dfa962a24b3f9218e2beb'
        'bd9df977dc175448189e14315c0684531095b2ef576be2a07675a89496eb321e811e6f761ed78038fdfb8ce11406bb010fe7130b18c1130a98abf94b4e11916a'
        '28794d83c694d657746ba9ecc00ae8595aa722cf4dc126d48adca9ca4ce8b1c5681cfcc8200821f00b86c07ee7cb4393483daa552361cdba1957566f13267b26'
        '911f9662fe3352d706ca018854e6a357a4fb281fccb0b75d4ab293df619c40e038d2a90efe7331a5abc3ba66cc5bdaf90853f9503fa947e207b9950bfbc5a41b'
        '371c83b6faaa87245c81ee200dc71c67fc8c156436854ceb3546dc82e4bb133e432235542b445b2c77041f67ceed63a8089c7b79df3562f0d641d18f38a7c68f'
        '528d272564697d50a82372615c954e8e7225f5c9015897e964607e7474855c6b7ed05464209a2c827eddcbd0fd32a5473740cf2e40f18be8ba1c554861160826'
        'f3d28a99a14477565ecb4de6b976031e96917af3e8cc5886021e29583f8bec2277a49bc5cb17b05cb9481ba060debdb0cd1ce6b4f5811a58f70e3f59ebff9205'
        'cc745d331329572cd23716883a9ff213d910ba9181497475ec8b2c11ab52eac8ab975fb412502e7ef362eddad032b7e4c3dec27341824aee8641ae55290b1bce'
        '767a38e4d0452e8ec7d80845ed63108f251f8e46a012c92da8f39cd6496d4940fbc50fe8d1755a9d3b2b32cf1e1de192eb8aca8a49c25c642150d2051f135fae'
        'a85a811288635bff48915c46e95902ca99a06e2fd9942b4a33c784b15115936be1c7308d4ecc5d7e6f58a1e29d451252d5695f18b354db76694ea81bdb7d6bf4'
        '4f54d0d0df8b34404ad479ca6288ddef0d644b8e010be7d5114c25b862d9da51dc22adece81ab8676982d412fc5f03b8fc4adacc6976247a5c53d577d0fabc09'
        '2ac51116d270fa6bd39bd923f3ed32d6ff064e2542b2cbdf631fa622e6a8106ec94b968f6c73bdafe2932e99f4ba281501a10de0a020ba6de4a2b65674409ac5'
        'ed6529089da4e2354e257d569e8c2d84808176606dca163f95286cbdcb76a2639d3d719532fe247f6f8b8192fcf3de7023a0660c3c9d137b368a6e518bbba8eb'
        '25f6dc619e9738c9b70196c8403163bb674f482075beb9ead7d5000b7335b9ed49eb11e7e7984ad7997b97f764d1f1b4bade5f47a1c5a5317bad6743cfb3c9f7'
        'd5121a34c576d403080c2820bb59561394bb878fef9ff1ed1a8e382582ace83a2ab1cd57d1c8777da8a250f96acaaf94e523dbe1956a42b7baf7e6a79b07472c'
        '8e7e30c48904d73345198a67efd8b86c9e74433a0303859ebc37f48515badac00fb3902ea498f008925bd58f744edb81a3c82eb649c3a0343c58fdd1ce981696'
        '42cc4120d706861e0d7ad6d46df6e220715ece3a2735987048abfefae08698a626ad241b9c8908d2df16d9740d751c98ca21aeeb58315dfdaa4170cb8a89e624'
        '9d1317b25b56b2d9c83187c426aecb64818a6cdaa18514dd000d05b362485cd6b13aa7eaa5f049a84c11603c6cc4b5d155a5fbb94f58055f0840bd5c1cf74970'
        '69937d4f804a27db980e56ba45775e9f308fda2f2897e0c88e021d8b802cc734aa7f6804acde6d3ea7e763986d9d3357e32bba89a41b176f01d685d13592c413')

prepare() {
  cd openssl-${_ver}
  patch -Np0 -i "${srcdir}/ca-dir.patch"
  for _patch in {2023-5678,2024-0727-1,2024-0727-2,2024-2511,2024-4741,2024-5535-1,2024-5535-2,2024-5535-3,2024-5535-4,2024-5535-5,2024-5535-6,2024-5535-7,2024-5535-8,2024-9143,2024-13176,2025-9230,2025-68160,2025-69418,2025-69420,2025-69421,2025-69419-1,2025-69419-2};
  do
    echo "DOING PATCH ${_patch}"
    patch -Np1 -i "${srcdir}/CVE-${_patch}.patch"
  done
  patch -Np1 -i "${srcdir}/CVE-2026-22795_CVE-2026-22796.patch"
}

build() {
  cd openssl-${_ver}

  export CC='gcc -m32'
  export PKG_CONFIG=i686-pc-linux-gnu-pkg-config

  ./Configure \
    --prefix='/usr' \
    --libdir='lib32/openssl-1.1' \
    --openssldir='/etc/ssl' \
    shared no-ssl3-method linux-elf

  make MAKEDEPPROG="${CC}" depend
  make
}

check() {
  cd openssl-${_ver}
  patch -p0 -R -i "$srcdir/ca-dir.patch"
  make test
  patch -p0 -i "$srcdir/ca-dir.patch"
  make apps/CA.pl
}

package() {
  cd openssl-${_ver}

  make DESTDIR="${pkgdir}" install_sw
  rm -rf "${pkgdir}"/{etc,usr/{include,bin}}

  mv "${pkgdir}"/usr/lib32/{openssl-1.1/,}libcrypto.so.1.1
  mv "${pkgdir}"/usr/lib32/{openssl-1.1/,}libssl.so.1.1
  ln -sf ../libssl.so.1.1 "${pkgdir}"/usr/lib32/openssl-1.1/libssl.so
  ln -sf ../libcrypto.so.1.1 "${pkgdir}"/usr/lib32/openssl-1.1/libcrypto.so

  sed -e 's|/include$|/include/openssl-1.1|' -i "${pkgdir}"/usr/lib32/openssl-1.1/pkgconfig/*.pc

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/${pkgname}"
}

# vim: ts=2 sw=2 et:
