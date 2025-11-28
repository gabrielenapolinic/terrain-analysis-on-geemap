# Terrain Analysis with Google Earth Engine

This repository contains a Python script for terrain analysis using Google Earth Engine (GEE). It computes various terrain metrics over a specified FeatureCollection using a smoothed Digital Elevation Model (DEM).

## Overview

The script calculates morphometric factors such as elevation, slope, aspect, and curvature, essential for understanding landforms, hydrology, and ecological dynamics.

## Key Features

1. **Initialization of Google Earth Engine**
   The script initializes the GEE API for geospatial processing.

2. **Smoothing the DEM**
   A Gaussian filter is applied to the DEM (NASADEM) to reduce noise and enhance terrain data quality.

3. **Loading FeatureCollection**
   The script loads a FeatureCollection (SU2) for terrain metric calculations.

4. **Calculating Terrain Metrics**
   The script computes the following terrain metrics:
   - **Elevation (El)**
   - **Slope (S)**
   - **Aspect (As)**
   - **Hillshade (Hill)**
   - **Northness (Nor)**
   - **Eastness (Eas)**
   - **Horizontal Curvature (HCv)**
   - **Vertical Curvature (VCv)**
   - **Mean Curvature (MeCur)**
   - **Minimal Curvature (MinCur)**
   - **Maximal Curvature (MaxCur)**
   - **Gaussian Curvature (Gauss)**
   - **Shape Index (Sh)**

5. **High-Resolution Zonal Statistics**
   The script uses a mapped `reduceRegion` function to calculate the **Mean** and **Standard Deviation** for each metric. This approach supports high-resolution analysis (e.g., 10m scale) and complex geometries by processing features individually.

6. **Renaming Metrics**
   Terrain metric bands are renamed for easier handling.

7. **Exporting Results**
   The summarized data is exported as a GeoJSON file to Google Drive for further analysis in GIS software.

## Output

The output is a GeoJSON file containing the summarized terrain metrics for each feature in the FeatureCollection, with mean and standard deviation values for each metric.

## Usage

To use this script, ensure you have the following:

- Python 3.x installed.
- Google Earth Engine Python API set up.
- Access to Google Drive for exporting results.

## Screenshots

<table class="tg">
  <thead>
    <tr>
      <th class="tg-0pky">Torto River's Watershed</th>
      <th class="tg-0pky">Slope, Aspect, and Shape Index</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="tg-0pky" rowspan="3"><img src="TORTO.png" alt="Torto River's Watershed" width="400"/></td>
      <td class="tg-0pky"><img src="Slope.png" alt="Slope" width="300"/></td>
    </tr>
    <tr>
      <td class="tg-0pky"><img src="Aspect.png" alt="Aspect" width="300"/></td>
    </tr>
    <tr>
      <td class="tg-0pky"><img src="Shape_Index.png" alt="Shape Index" width="300"/></td>
    </tr>
  </tbody>
</table>

## License

This project is licensed under the GNU General Public License v3.0.

<img src="GPLv3_Logo.svg.png" alt="GPLv3 License" width="200"/>
