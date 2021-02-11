import os
from pathlib import Path

from flask import Flask
from osgeo import gdal

app = Flask(__name__)

root = Path(os.path.abspath(__file__)).parent


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/name/<path:filename>')
def file_name(filename):
    srcfile = root / filename
    return str(srcfile)


@app.route('/info/<path:filename>')
def download_file(filename):
    srcfile = root / filename
    srcds = gdal.Open(str(srcfile), gdal.GA_ReadOnly)
    if srcds is None:
        return f'Could not open {srcds}'
    output = f'file {srcfile} has {srcds.RasterCount} bands'
    return output


if __name__ == "__main__":
    app.run()
