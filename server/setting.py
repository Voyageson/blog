# import blueprint here.
from blog import blog

run_args = {
    'host': '0.0.0.0',
    'port': 8000,
    'debug': True,
}

blueprints = [
    blog,
]