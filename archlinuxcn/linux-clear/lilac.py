from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('_subarch='):
            print('_subarch=26')
        elif line.strip() == "### Copying i915 firmware and intel-ucode":
            print('### Disable modle sig force')
            print('	    sed -i "s|CONFIG_MODULE_SIG_FORCE=y|CONFIG_MODULE_SIG_FORCE=n|g" ./.config ')
            print(line)
        else:
            print(line)


