import subprocess
import sys
from importlib.metadata import version, PackageNotFoundError

def checkRequirements(requirementfile='requirements.txt'):
    try:
        with open(requirementfile, 'r') as file:
            requirements = file.readlines()
            for requirement in requirements:
                package = requirement.strip().split('>=')[0]
                try:
                    version(package)
                except PackageNotFoundError:
                    print(f"{package} n'est pas installé. Installation...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", requirement.strip()])

    except FileNotFoundError:
        print(f"Le fichier {requirementfile} est introuvable.")
        sys.exit(1)


if __name__ == '__main__':
    checkRequirements()
    
    from app import createApp
    app = createApp()
    
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])