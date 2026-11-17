"""Intentional issues for the linting demo (fake values only)."""
import os, subprocess
import hashlib

PASSWORD = "not-a-real-secret"  # S105 hardcoded password (fake)


def run(cmd):
    subprocess.call(cmd, shell=True)  # S602 shell=True


def digest(data):
    return hashlib.md5(data).hexdigest()  # S324 weak hash


def risky(x):
    try:
        return eval(x)  # S307 eval
    except:  # E722 bare except
        pass
