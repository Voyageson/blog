from sanic import Sanic
import setting

app = Sanic(__name__)

# registe blueprint
app.blueprint(setting.blueprints)

if __name__ == '__main__':
    app.run(**setting.run_args)