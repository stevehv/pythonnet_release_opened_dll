import clr
import os
from os import path
from System.Reflection import Assembly

# Tried loading csharp_library using reflection as recommended as a workaround 
# https://github.com/pythonnet/pythonnet/issues/513#issuecomment-316180382
if __name__ == '__main__':
    # Load charp_library.dll using reflection
    # https://stackoverflow.com/a/6365969
    dll_abs_path = path.join(path.dirname(path.abspath(__file__)), "csharp_library.dll")
    dll1 = Assembly.LoadFile(dll_abs_path)

    # Call charp_library.dll
    print(clr.MyNamespace.MyClass().MyFunction()) # AttributeError: module 'clr' has no attribute 'MyNamespace'

    # Release charp_library.dll
    # Don't yet know how to do this, I'd first need to get load working
     
    # Confirm that dll has been released
    os.remove("charp_library.dll")

