from cx_Freeze import setup, Executable

base = None
version = "0.0.1"

executables = [Executable("update-no-ip", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
        'optimize':2,
        'include_msvcr':True,
        'include_files':[]
    },    
}

setup(
    name = "update-no-ip",
    options = options,
    version = version,
    description = 'Update ip for host on no-ip.com',
    executables = executables
)