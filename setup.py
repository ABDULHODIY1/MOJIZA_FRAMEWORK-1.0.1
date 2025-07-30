from setuptools import setup, find_packages

setup(
    name="mojiza",
    version="0.0.1",
    description="A lightweight Python HTML rendering engine",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Abdulhodiy Muhiddinov",
    author_email="muhiddinovabdulhodiy2@gmail.com",
    url="https://github.com/ABDULHODIY1/MOJIZA_FRAMEWORK-1.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Jinja2>=3.1.4",
        "loguru>=0.7.3",
        "watchdog>=6.0.0",
        "aiohttp>=3.11.10",
        "qrcode>=8.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Mojiza",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires='>=3.7',
    license="MIT",
)
