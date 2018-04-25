from setuptools import setup, find_packages

setup(
    name='paycheck',
    version='0.0.1',
    author='Ben Kaehler',
    author_email='kaehler@gmail.com',
    description='Tools for testing q2-clawback',
    scripts=['paycheck/assets/run_traceable_dada_paired.R'],
    license='BSD-3-Clause',
    packages=find_packages(),
    package_data={'paycheck.tests': ['data/*']},
    entry_points={
        'console_scripts': 
        ['paycheck_simulate=paycheck.simulate:simulate_all_samples']
    }
)