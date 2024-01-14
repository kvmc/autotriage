from lief import PE

binary32 = PE.Binary("pe_from_scratch", PE.PE_TYPE.PE32)

section_text                 = PE.Section(".text")
#section_text.content         = code
section_text.virtual_address = 0x1000

section_data                 = PE.Section(".data")
#section_data.content         = data
section_data.virtual_address = 0x2000


title   = "LIEF is awesome\0"
message = "Hello World\0"

data =  list(map(ord, title))
data += list(map(ord, message))


user32 = binary32.add_library("user32.dll")
user32.add_entry("MessageBoxA")

kernel32 = binary32.add_library("kernel32.dll")
kernel32.add_entry("ExitProcess")

ExitProcess_addr = binary32.predict_function_rva("kernel32.dll", "ExitProcess")
MessageBoxA_addr = binary32.predict_function_rva("user32.dll", "MessageBoxA")
print("Address of 'ExitProcess': 0x{:06x} ".format(ExitProcess_addr))
print("Address of 'MessageBoxA': 0x{:06x} ".format(MessageBoxA_addr))

builder = PE.Builder(binary32)
builder.build_imports(True)
builder.build()
builder.write("pe_from_scratch.exe")
