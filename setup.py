import setuptools
import subprocess
from setuptools.command.install import install


# Custom command to run the shell script during installation
class CustomInstallCommand(install):
    """Custom command to run a shell script during installation"""
    def run(self):
        # Run the shell script
        subprocess.check_call(['./full_install.sh'])
        install.run(self)


setuptools.setup(
    name='autogluon',
    version='0.1',
    packages=setuptools.find_packages(),
    cmdclass={
        'install': CustomInstallCommand,
    },
)
