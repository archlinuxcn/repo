import sys
import shutil

from elftools.elf.elffile import ELFFile
from capstone import *
from capstone.x86 import *

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} [path to discord_krisp.node]")
    # "Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors."
    sys.exit(2)

executable = sys.argv[1]

elf = ELFFile(open(executable, "rb"))
symtab = elf.get_section_by_name('.symtab')

krisp_initialize_address = symtab.get_symbol_by_name("_ZN7discordL17DoKrispInitializeEv")[0].entry.st_value
isSignedByDiscord_address = symtab.get_symbol_by_name("_ZN7discord4util17IsSignedByDiscordERKNSt4__Cr12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE")[0].entry.st_value

text = elf.get_section_by_name('.text')
text_start = text['sh_addr']
text_start_file = text['sh_offset']
# This seems to always be zero (.text starts at the right offset in the file). Do it just in case?
address_to_file = text_start_file - text_start

# Done with the ELF now.
# elf.close()

krisp_initialize_offset = krisp_initialize_address - address_to_file
isSignedByDiscord_offset = krisp_initialize_address - address_to_file

f = open(executable, "rb")
f.seek(krisp_initialize_offset)
krisp_initialize = f.read(96)
f.close()

# States
found_issigned_by_discord_call = False
found_issigned_by_discord_test = False
found_issigned_by_discord_je = False
found_already_patched = False
je_location = None
je_size = 0

# We are looking for a call to IsSignedByDiscord, followed by a test, followed by a je.
# Then we replace the je with nops.

md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True
for i in md.disasm(krisp_initialize, krisp_initialize_address):
    if i.id == X86_INS_CALL:
        if i.operands[0].type == X86_OP_IMM:
            if i.operands[0].imm == isSignedByDiscord_address:
                found_issigned_by_discord_call = True

    if i.id == X86_INS_TEST:
        if found_issigned_by_discord_call:
            found_issigned_by_discord_test = True

    if i.id == X86_INS_JE:
        if found_issigned_by_discord_test:
            found_issigned_by_discord_je = True
            je_location = i.address
            je_size = len(i.bytes)
            break

    if i.id == X86_INS_NOP:
        if found_issigned_by_discord_test:
            found_already_patched = True
            break

if je_location:
    print(f"Found patch location: 0x{je_location:x}")

    shutil.copyfile(executable, executable + ".orig")
    f = open(executable, 'rb+')
    f.seek(je_location - address_to_file)
    f.write(b'\x90' * je_size)   # je can be larger than 2 bytes given a large enough displacement :(
    f.close()
else:
    if found_already_patched:
        print("Couldn't find patch location - already patched.")
    else:
        print("Couldn't find patch location - review manually. Sorry.")
