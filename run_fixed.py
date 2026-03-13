import os
import sys

# Add a workaround for the WMI error - must be done BEFORE any other imports
import platform as platform_original

class FixedPlatform:
    """Fixed platform module to handle WMI errors on Windows"""
    _machine = None
    _system = None
    _version = None
    
    def machine(self):
        if FixedPlatform._machine is None:
            try:
                FixedPlatform._machine = platform_original.machine()
            except:
                FixedPlatform._machine = 'AMD64'
        return FixedPlatform._machine
    
    def system(self):
        if FixedPlatform._system is None:
            try:
                FixedPlatform._system = platform_original.system()
            except:
                FixedPlatform._system = 'Windows'
        return FixedPlatform._system
    
    def version(self):
        if FixedPlatform._version is None:
            try:
                FixedPlatform._version = platform_original.version()
            except:
                FixedPlatform._version = '10.0.26000'
        return FixedPlatform._version
    
    def __getattr__(self, name):
        # Handle the specific attributes we know might fail
        if name == 'machine':
            return self.machine
        elif name == 'system':
            return self.system
        elif name == 'version':
            return self.version
        # For all other attributes, use the original platform module
        return getattr(platform_original, name)

# Replace the platform module BEFORE any other imports
sys.modules['platform'] = FixedPlatform()

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Now run the actual app from the same directory
app_py_path = os.path.join(script_dir, 'app.py')
with open(app_py_path, 'r', encoding='utf-8') as f:
    exec(f.read())

