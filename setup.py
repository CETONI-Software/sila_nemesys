from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sila_nemesys",
    version="0.0.1",
    author="Florian Meinicke",
    author_email="florian.meinicke@cetoni.com",
    description="The official SiLA 2 driver for the neMESYS High Precision Syringe Pumps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CETONI-Software/sila_nemesys",
    packages=find_packages(),
    install_requires=[
        "sila2lib",
        # "cetoni-qmixsdk"
    ],
    # dependency_links=[
    #     "link to QmixSDK"
    # ],
    scripts=[
        "qmixsdk-py_wrapper.sh"
    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires='>=3.6',
)
