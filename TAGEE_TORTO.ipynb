import ee
ee.Initialize()

# Safanelli, J.L.; Poppiel, R.R.; Ruiz, L.F.C.; Bonfatti, B.R.; Mello, F.A.O.; Rizzo, R.; Demattê, J.A.M. Terrain Analysis in Google Earth Engine: 
# A Method Adapted for High-Performance Global-Scale Analysis. ISPRS Int. J. Geo-Inf. 2020, 9, 400. DOI: https://doi.org/10.3390/ijgi9060400
from tagee import terrainAnalysis

# Set up a smoothed DEM
# Apply a Gaussian filter to smooth the SRTM DEM. The filter reduces noise and prepares the DEM for terrain analysis.
gaussianFilter = ee.Kernel.gaussian(
    radius=3, sigma=2, units='pixels', normalize=True
)
srtmSmooth = ee.Image("USGS/SRTMGL1_003").convolve(gaussianFilter).resample("bilinear")

# Load the FeatureCollection (SU2)
# Replace 'path_to_your_feature_collection' with the actual path to your data.
feature_collection_path = 'path_to_your_feature_collection'
SU2 = ee.FeatureCollection(feature_collection_path)

# Calculate terrain metrics
# Compute multiple terrain metrics (elevation, slope, aspect, curvature, etc.) using the smoothed DEM.
terrainMetrics = terrainAnalysis(srtmSmooth)

# Combine reducers to get mean and standard deviation
# Define a reducer that calculates both the mean and standard deviation of the terrain metrics.
reducer = ee.Reducer.mean().combine(
    reducer2=ee.Reducer.stdDev(), sharedInputs=True
)

# Rename parameters with abbreviated names
# Rename the terrain metric bands to use shorter names for easier handling.
abbreviated_metrics = terrainMetrics.select([
    'Elevation', 'Slope', 'Aspect', 'Hillshade',
    'Northness', 'Eastness', 'HorizontalCurvature',
    'VerticalCurvature', 'MeanCurvature', 'MinimalCurvature',
    'MaximalCurvature', 'GaussianCurvature', 'ShapeIndex'
], [
    'El', 'S', 'As', 'Hill', 'Nor', 'Eas', 'HCv', 'VCv',
    'MeCur', 'MinCur', 'MaxCur', 'Gauss', 'Sh'
])

# Summarize the metrics within each feature in SU2
# Use the defined reducer to calculate mean and standard deviation of the terrain metrics for each feature in the FeatureCollection.
reduction = abbreviated_metrics.reduceRegions(
    collection=SU2,
    reducer=reducer
)

# Export the results as a GeoJSON to Google Drive
# Replace 'your_folder_name' with the desired folder name in Google Drive.
task = ee.batch.Export.table.toDrive(
    collection=reduction,
    description='Torto_TAGEE',
    fileFormat='GeoJSON',
    folder='your_folder_name'
)

# Start the export task
# The task is initiated and will process in the background. Check Google Drive for the exported file.
task.start()

print("Export started. Check your Google Drive for the file.")
