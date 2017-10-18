import clr
import os

# This would be an ideal solution to the problem
# See: reflection-workaround.py
if __name__ == '__main__':
    # Load charp_library.dll
    clr.AddReference("csharp_library")
    import MyNamespace

    # Call charp_library.dll
    print(MyNamespace.MyClass().MyFunction())

    # Release charp_library.dll
    clr.ClearProfilerData() # Not yet supported by Pythonnet
     
    # Confirm that dll has been released
    os.remove("charp_library.dll")