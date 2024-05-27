"""
This module builds an executable from a Python script using PyInstaller.

Imports:
subprocess: Allows you to spawn new processes, connect to their input/output/error pipes, 
and obtain their return codes.
os: Provides a way of using operating system-dependent functionality,
"""
import subprocess
import os

def build_executable():
    """ 
    Define the path to the main script
    """
    main_script_path = os.path.abspath('src/GUI/main.py')

    # Define the PyInstaller command
    build_command = [
        'pyinstaller',
        '--name', 'nutriscan_ai_app',
        '--noconsole',  
        '--onefile',
        '--add-data', os.path.abspath('src/GUI/ui/mainwindow.ui') + os.pathsep + 'GUI/ui',
        main_script_path
    ]
    # Run the build command
    result = subprocess.run(build_command, check=True)
    if result.returncode == 0:
        print("Build succeeded!")
    else:
        print("Build failed!")

if __name__ == '__main__':
    #If this module is being run as the main program, execute the build_executable function.
    build_executable()
    