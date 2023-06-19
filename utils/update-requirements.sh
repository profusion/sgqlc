#!/bin/sh

# we must keep dev-requirements.txt so we can test on other Python versions
pipenv requirements --dev > dev-requirements.txt
