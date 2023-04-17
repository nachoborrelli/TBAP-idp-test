import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


if env('USE_POSTGRES', default=False):
    import pymysql
    pymysql.install_as_MySQLdb()
