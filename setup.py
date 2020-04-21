from setuptools import setup, find_packages

setup(
    name='fee_simulator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'ortools',
        'matplotlib'
    ],
    entry_points='''
        [console_scripts]
        feesim=fee_simulator.simulator:run_auctions
    ''',
)
