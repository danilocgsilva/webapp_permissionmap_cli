from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="WebApp Permission Map CLI",
    version=VERSION,
    description="Access webapp permission map from command line",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="api dev cli webapp",
    url="https://github.com/danilocgsilva/webapp_permissionmap_cli",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["webapp_permission_map_cli"],
    entry_points={"console_scripts": ["wapmap=webapp_permission_map_cli.__main__:main"],},
    include_package_data=True
)

