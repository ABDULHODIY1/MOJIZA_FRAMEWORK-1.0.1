from setuptools import setup, find_packages

setup(
    name="mojiza",  # PyPI’dagi nomi
    version="0.0.1",  # Versiyasi
    description="A lightweight Python HTML rendering engine",  # Qisqa tavsif
    author="Abdulhodiy Muhiddinov",  # Muallif ismi
    author_email="abdul@example.com",  # (ixtiyoriy)
    packages=find_packages(),  # mojiza/ papkasi ichidagilarni topadi
    include_package_data=True,  # agar static yoki template fayllar bo‘lsa
    install_requires=[
        "Jinja2>=3.1.4",
        "loguru>=0.7.3",
        "watchdog>=6.0.0",  # agar auto-reload ishlatsang
        "aiohttp>=3.11.10",  # agar async qo‘llab-quvvatlasang
        "qrcode>=8.0",  # agar QR code yaratish funksiyang bo‘lsa
    ],  # boshqa kerakli kutubxonalar (masalan: requests)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # yoki boshqa
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Minimal Python versiyasi
)
