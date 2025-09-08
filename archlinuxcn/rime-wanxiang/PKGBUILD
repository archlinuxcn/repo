# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang
pkgname=(rime-wanxiang-dict rime-wanxiang-pro-dict rime-wanxiang-data rime-wanxiang-pro-data)
pkgver=12.1.0
pkgrel=1
pkgdesc="万象拼音：词库基于AI筛选和语料辅助筛选精干高效，配合全新语法模型，输入不再纠结。"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz"
        build.sh)
b2sums=('ab524ebff75868e7eb21a5d34cdce8044ded548b542a6ff7e0fbb7f43b9c52bf341d40de3846d0ffe598e86b026ea155d178bcb76c6e073b8a28600ffe7a55d8'
        'ffbab0a401f81e8f520304ec8016dfb5188b84b5a948582409d25b890c75f65ad738379a01999f8315b9b73a58163f1c44feb09d51c25ef300a53bd55456395d')

makedepends=("librime" "rime-prelude" "rime-essay" "sed" "python" "zip")

# 拼写方案
declare -A _schemas=(
    [pinyin]="全拼"
    [zrm]="自然码"
    [flypy]="小鹤双拼"
    [mspy]="微软双拼"
    [sogou]="搜狗双拼"
    [abc]="智能ABC"
    [ziguang]="紫光双拼"
    # 以下方案支持不完善
    # [pyjj]="拼音加加"
    # [gbpy]="国标双拼"
    # [lxsq]="乱序17"
    # [hanxin]="汉心龙"
    # [zrlong]="自然龙"
)

# 辅助码类型
declare -A _fuzhus=(
  [zrm]="自然码"
  [moqi]="墨奇"
  [flypy]="小鹤"
  [hanxin]="汉心"
  [wubi]="五笔前2"
  [tiger]="虎码首末"
)

build() {
    cd "${srcdir}/rime_wanxiang-${pkgver}" || exit 1

    msg2 "release building..."
    bash .github/workflows/scripts/release-build.sh >/dev/null

    msg2 "schema building..."
    bash "${srcdir}"/build.sh
}

_package() {
    cd "${srcdir}"/dist/"${1//rime-wanxiang-/}" || exit 1
    find . -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;
}

package_rime-wanxiang-dict() {
    pkgdesc="万象拼音词库基础数据"
    replaces=("${pkgbase}-dict-zh")
    # shellcheck disable=SC2128
    _package "$pkgname"
}
package_rime-wanxiang-pro-dict() {
    pkgdesc="万象拼音双拼辅助码版词库基础数据"
    replaces=("${pkgbase}-dict-zh")
    conflicts=("$pkgbase-dict")
    # shellcheck disable=SC2128
    _package "$pkgname"
}

package_rime-wanxiang-data() {
    pkgdesc="万象拼音基础数据"
    depends=(lua librime rime-wanxiang-gram-zh-hans)
    optdepends=('libnotify: notification support in lua scripts')
    # shellcheck disable=SC2128
    _package "$pkgname"
}
package_rime-wanxiang-pro-data() {
    pkgdesc="万象拼音双拼辅助码版基础数据"
    depends=(lua librime rime-wanxiang-gram-zh-hans)
    optdepends=('libnotify: notification support in lua scripts')
    conflicts=("$pkgbase-data")
    # shellcheck disable=SC2128
    _package "$pkgname"
}

#
# ${pkgbase}-<schema>
# - ${pkgbase}-data
# - ${pkgbase}-dict-<schema>
#   - ${pkgbase}-dict
# 
# ${pkgbase}-pro-<schema>
# - ${pkgbase}-pro-data
# - [${pkgbase}-pro-data-fuzhu]
#   - ${pkgbase}-pro-data-<fuzhu>-fuzhu
#     - ${pkgbase}-pro-dict-<fuzhu>-fuzhu
#       - ${pkgbase}-pro-dict
# 
for _schema in "${!_schemas[@]}"; do
    _schema_name=${_schemas[$_schema]}

    # 基础版词库
    _pkgname=${pkgbase}-dict-${_schema} && pkgname+=("${_pkgname}")
    _conflicts=()
    for _schema_c in "${!_schemas[@]}"; do
        [[ "${_schema_c}" == "${_schema}" ]] && continue
        _conflicts+=("${pkgbase}-dict-${_schema_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音标准版词库（${_schema_name}方案）'
        depends=('${pkgbase}-dict=${pkgver}')
        conflicts=(${_conflicts[*]})
        _package ${_pkgname}
    }"

    # 基础版方案
    _pkgname=${pkgbase}-${_schema} && pkgname+=("${_pkgname}")
    _conflicts=()
    for _schema_c in "${!_schemas[@]}"; do
        [[ "${_schema_c}" == "${_schema}" ]] && continue
        _conflicts+=("${pkgbase}-${_schema_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音标准版（${_schema_name}方案）'
        depends=(${pkgbase}-data '${pkgbase}-dict-${_schema}=${pkgver}')
        conflicts=(${_conflicts[*]})
        install='post.install'
        _package ${_pkgname}
    }"

    if [[ $_schema != "pinyin" ]]; then
        # PRO 版方案
        _pkgname=${pkgbase}-pro-${_schema} && pkgname+=("${_pkgname}")
        _conflicts=()
        for _schema_c in "${!_schemas[@]}"; do
            [[ "${_schema_c}" == "${_schema}" ]] && continue
            _conflicts+=("${pkgbase}-pro-${_schema_c}")
        done
        eval "package_${_pkgname}() {
            pkgdesc='万象拼音双拼辅助码版（${_schema_name}方案）'
            depends=(${pkgbase}-pro-data '${pkgbase}-pro-data-fuzhu=${pkgver}')
            conflicts=(${_conflicts[*]})
            install='post.install'
            _package ${_pkgname}-zrm-fuzhu
        }"
    fi
done

for _fuzhu in "${!_fuzhus[@]}"; do
    _fuzhu_name=${_fuzhus[$_fuzhu]}

    # PRO 版词库
    _pkgname=${pkgbase}-pro-dict-${_fuzhu}-fuzhu && pkgname+=("${_pkgname}")
    _conflicts=()
    for _fuzhu_c in "${!_fuzhus[@]}"; do
        [[ "${_fuzhu_c}" == "${_schema}" ]] && continue
        _conflicts+=("${pkgbase}-dict-${_fuzhu_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音双拼辅助码词库（${_fuzhu_name}辅助）'
        depends=('${pkgbase}-pro-dict=${pkgver}')
        conflicts=(${_conflicts[*]})
        _package ${_pkgname}
    }"

    # PRO 版数据
    _pkgname=${pkgbase}-pro-data-${_fuzhu}-fuzhu && pkgname+=("${_pkgname}")
    _conflicts=()
    for _fuzhu_c in "${!_fuzhus[@]}"; do
        [[ "${_fuzhu_c}" == "${_schema}" ]] && continue
        _conflicts+=("${pkgbase}-pro-data-${_fuzhu_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音双拼辅助码版基础数据（${_fuzhu_name}辅助）'
        depends=('${pkgbase}-pro-dict-${_fuzhu}-fuzhu=${pkgver}')
        conflicts=(${_conflicts[*]})
        provides=('${pkgbase}-pro-data-fuzhu=${pkgver}')
        _package ${_pkgname}
    }"
done
