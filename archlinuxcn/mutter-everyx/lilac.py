from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

# patch 清单, 元素为 source 中的完整条目(名称::URL 或本地文件名)
_PATCHES = [
    '5122.patch::https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/5122.patch',
]

def pre_build():
    g.files = download_official_pkgbuild('mutter')

    state = None
    for line in edit_file('PKGBUILD'):
        s = line.strip()

        if state == 'pkgname':              # 折叠官方 split pkgname 为单包
            if s == ')':
                state = None
            continue
        if state == 'source':               # source 末尾追加全部 patch 条目
            if s == ')':
                state = None
                for entry in _PATCHES:
                    print(f'  "{entry}"')
                print(line)
                continue
            print(line)
            continue
        if state == 'b2sums':               # b2sums 末尾追加与 patch 数量一致的 SKIP
            if line.rstrip().endswith(')'):
                state = None
                print(line[:-1])
                for _ in _PATCHES:
                    print('        SKIP')
                print(')')
                continue
            print(line)
            continue
        if state == 'mkdep':                # makedepends 末尾追加 libadwaita(devkit 硬依赖)
            if s == ')':
                state = None
                if not g.mkdep_has_adwaita:
                    print('  libadwaita')
                print(line)
                continue
            if s == 'libadwaita':
                g.mkdep_has_adwaita = True
            print(line)
            continue
        if state == 'skip':                 # 丢弃 mutter-devkit / mutter-docs 子包函数与 _pick helper
            if line == '}':
                state = None
            continue
        if state == 'pm':                   # 主包函数: 改名; _pick devkit 转 rm(不打包客户端, 与官方 mutter 文件等价)
            if line == '}':
                state = None
                print(line)
                continue
            if s.startswith('_pick devkit'):
                print(line.replace('_pick devkit ', 'rm ', 1))
                continue
            if s.startswith('_pick docs'):
                continue
            if s.startswith('provides=(') and not s.startswith('provides+=('):
                # 官方用 = 赋值会覆盖顶层 provides, 改为叠加
                print(line.replace('provides=(', 'provides+=(', 1))
                continue
            print(line)
            continue

        # ---- 普通行 anchor ----
        if line.startswith('pkgbase='):
            # 非 split 包: 删除 pkgbase 行
            continue
        if line.startswith('pkgname=('):
            print('pkgname=mutter-everyx')
            state = 'pkgname'
            continue
        if line.startswith('pkgdesc='):
            line = line[:-1] + ' (with patches picked from everyx)"'
            print(line)
            continue
        if line == 'arch=(x86_64)':         # 顶替官方 mutter: 提供/冲突(与官方 mutter-devkit 无文件重叠, 可共存)
            print(line)
            print('provides+=(mutter)')
            print('conflicts+=(mutter)')
            continue
        if line.startswith('makedepends=('):
            g.mkdep_has_adwaita = False
            state = 'mkdep'
            print(line)
            continue
        if line.startswith('source=('):
            state = 'source'
            print(line)
            continue
        if line.startswith('b2sums=('):
            state = 'b2sums'
            print(line)
            continue
        if s == 'cd mutter':                # prepare() 内逐一应用 patch
            print(line)
            for entry in _PATCHES:
                print(f'  git apply -3 ../{entry.split("::", 1)[0]}')
            continue
        if '-D docs=true' in line:          # 关 docs, 开 devkit(MDK); 单包: devkit 文件随主包
            print(line.replace('docs=true', 'docs=false'))
            print('    -D devkit=enabled')
            continue
        if line.startswith('_pick() {'):
            state = 'skip'   # 死代码: 单包不拆子包, 丢弃 _pick helper
            continue
        if line.startswith('package_mutter-devkit()') or line.startswith('package_mutter-docs()'):
            state = 'skip'
            continue
        if line.startswith('package_mutter()'):
            print('package() {')
            state = 'pm'
            continue
        print(line)

def post_build():
    git_add_files(g.files)
    git_commit()
