from setuptools import setup, find_packages

setup(
    name="mojiza",
    version="0.1.3.b1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    license="GPL-3.0-only",  # Faqat bu yerda ko'rsatiladi
    description="MOJIZA - A minimal web framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        # License classifier NI o‘chirib tashlang!
    ],
    python_requires='>=3.6',
)
