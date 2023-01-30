##
from spatialdata_io import xenium
import spatialdata as sd

##
from pathlib import Path
import shutil

##
path = Path().resolve()
# luca's workaround for pycharm
if not str(path).endswith("xenium"):
    path /= "xenium"
    assert path.exists()
path_read = path / "data/xenium/outs"
path_write = path / "data.zarr"
##
print('parsing the data... ', end='')
sdata = xenium(
    path=str(path_read),
    n_jobs=8,
)
print("done")
##
print('writing the data... ', end='')
if path_write.exists():
    shutil.rmtree(path_write)
sdata.write(path_write)
print("done")
##
print(f'view with "python -m spatialdata view data.zarr"')
sdata = sd.SpatialData.read("./data.zarr/")
print("read")
print(sdata)
##

