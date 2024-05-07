import apache_beam
import weatherbench2
import xarray as xr
import numpy as np

#find model name from cloud
#very tailored to weatherbench2
def find_model_name(path):
    return path.split('/')[4]

#list of paths
fns = ['gs://weatherbench2/datasets/era5/1959-2022-6h-64x32_equiangular_conservative.zarr',
       'gs://weatherbench2/datasets/hres/2016-2022-0012-64x32_equiangular_conservative.zarr',
       'gs://weatherbench2/datasets/pangu/2018-2022_0012_64x32_equiangular_conservative.zarr',
       'gs://weatherbench2/datasets/keisler/2020-64x32_equiangular_conservative.zarr',
       'gs://weatherbench2/datasets/graphcast/2020/date_range_2019-11-16_2021-02-01_12_hours-64x32_equiangular_conservative.zarr',
       'gs://weatherbench2/datasets/sphericalcnn/2020-64x32_equiangular_conservative.zarr',
       'gs://weatherbench2/datasets/fuxi/2020-64x32_equiangular_conservative.zarr',
       'gs://weatherbench2/datasets/neuralgcm_deterministic/2020-64x32_equiangular_conservative.zarr']

#Time period
itime = np.datetime64('2020-01-01T00')
ftime = np.datetime64('2020-12-31T23')

for fn in fns:
    ds = xr.open_zarr(fn)
    ds = ds.sel(time=slice(itime, ftime))
    
    newds = xr.Dataset()
    newds['u850'] = ds['u_component_of_wind'].sel(level=850).load()
    newds['v850'] = ds['v_component_of_wind'].sel(level=850).load()
    newds['geopot'] = ds['geopotential'].sel(level=850).load()

    sname = find_model_name(fn)
    newds.to_netcdf('data/%s/dynamics_850.nc' % sname)