import subprocess
import os

def build_executable():
    # Define the path to the main script
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
    build_executable()