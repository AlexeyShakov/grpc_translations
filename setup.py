from setuptools import setup, find_packages

setup(
    name="grpc_translations",
    version="0.0.1",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    install_requires=["grpcio==1.59.0", "grpcio-tools==1.59.0"],
    python_requires=">=3.8"
)
