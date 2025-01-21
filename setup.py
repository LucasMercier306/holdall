from setuptools import setup, find_packages

setup(
    name='rbk-ctl',
    version='0.1.0',
    packages=find_packages(where="src"),  # Rechercher les packages dans le dossier 'src'
    package_dir={'': 'src'},  # Définir 'src' comme racine des packages
    install_requires=[
        'fire',  # Dépendance pour le CLI
    ],
    entry_points={
        'console_scripts': [
            'rbk_ctl=rbk_ctl.main:main',  # Lier la commande 'rbk-ctl' au point d'entrée
        ],
    },
    author="Votre Nom",
    description="Un outil CLI basé sur Fire pour rbk-ctl",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
