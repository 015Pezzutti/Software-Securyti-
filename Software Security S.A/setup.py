from turtle import setup

from distutils.command import install # type: ignore


python setup.py install # type: ignore

from setuptools import setup, find_packages # type: ignore

setup(
    name='ProjetoSeguranca',
    version='1.0.0',
    description='Software para gerenciamento de câmeras, alarmes, cerca elétrica e controle de acesso facial.',
    author='Seu Nome',
    author_email='seu_email@dominio.com',
    packages=find_packages(),
    install_requires=[
        'PyQt5==5.15.4',
        'bcrypt==3.2.0',
        'cryptography==3.4.7',
        'opencv-python==4.5.1.48',
    ],
    entry_points={
        'console_scripts': [
            'projeto_seguranca=main:main',
        ],
    },
)

