# 🌿 NDVI and Precipitation Graphic Analysis – Serra do Japi, Jundiaí (SP), Brazil (2013–2023)

This repository contains the source code, data processing pipeline, and visualization scripts developed for the scientific study on the conservation of the **Serra do Japi Environmental Conservation, Preservation and Restoration Zone**, located in **Jundiaí, São Paulo, Brazil**.  
The analysis covers the **temporal behavior of the Normalized Difference Vegetation Index (NDVI)** and **annual precipitation** between **2013 and 2023**, as well as statistical and spatial assessments used in the article submitted to the *Revista Brasileira de Cartografia (RBC)*.


## 📄 About the study
The study applies **remote sensing** and **geospatial analysis techniques** to evaluate the conservation effectiveness of Serra do Japi, one of the best-preserved remnants of the **Atlantic Forest biome** in southeastern Brazil.  

NDVI values were extracted from **Landsat-8 imagery** (Collection 2 Level-2 surface reflectance products), while precipitation data were obtained from the **CHIRPS** dataset via **Climate Engine**.  
Administrative boundaries were provided by **IBGE** (Brazilian Institute of Geography and Statistics) and **GeoJundiaí** (Municipal Geoinformation Platform).

The visualizations generated in this notebook supported the analysis of long-term vegetation stability, the relationship between vegetation cover and precipitation, and the identification of local spatial dynamics within the municipality.


## 🧮 Analytical steps
1. **Data Acquisition**  
   - Downloaded NDVI composites (dry season) from *Landsat-8 (USGS Earth Explorer)*.  
   - Retrieved annual accumulated precipitation data from *CHIRPS* through *Climate Engine*.  
   - Obtained administrative and conservation boundaries from *IBGE* and *GeoJundiaí* shapefiles.

2. **Preprocessing and ΔNDVI Calculation**  
   - Computed per-pixel difference: **ΔNDVI = NDVI₍₂₀₂₃₎ − NDVI₍₂₀₁₃₎**.  
   - Reclassified pixels into three conservative classes:  
     - **Possible vegetation loss:** ΔNDVI ≤ −0.125  
     - **No significant change:** −0.125 < ΔNDVI < 0.125  
     - **Possible vegetation gain:** ΔNDVI ≥ 0.125  

3. **Zonal Extraction and CSV Export**  
   - Masked rasters by study zones (Serra do Japi and urban Jundiaí).  
   - Extracted per-pixel reclassified values to `.csv` for statistical visualization.

4. **Histogram Generation for Article Inclusion**  
   - Created a **percentage-based histogram** of reclassified pixels using **Python (Matplotlib)** in **VS Code**.  
   - The histogram compares the **Serra do Japi zone** and the **urban portion of Jundiaí**, visually representing the proportion of pixels classified as loss, no significant change, and gain.  
   - This figure was **included as part of Figure 7** in the manuscript submitted to the *Revista Brasileira de Cartografia*.

## 📊 Data sources
| Dataset | Source | Time span | Resolution | Access |
|----------|---------|------------|-------------|---------|
| **NDVI (2013–2023)** | Landsat-8 (USGS Earth Explorer) | 2013–2023 | 30 m | [https://earthexplorer.usgs.gov](https://earthexplorer.usgs.gov) |
| **Precipitation** | CHIRPS via Climate Engine | 2013–2023 | ~4.8 km | [https://climateengine.org](https://climateengine.org) |
| **Fire occurrences** | MapBiomas Fire Collection 3.0 | 2013–2023 | Annual | [https://mapbiomas.org](https://mapbiomas.org) |
| **Administrative boundaries** | IBGE | Static | Vector (Shapefile) | [https://ibge.gov.br](https://ibge.gov.br) |
| **Conservation zone boundaries** | GeoJundiaí (Municipal Geoinformation System) | Static | Vector (Shapefile) | [https://geojundiai.jundiai.sp.gov.br](https://geojundiai.jundiai.sp.gov.br) |


## 📌 Citation
If you use or refer to this code or dataset structure in your own work, please cite the corresponding paper (currently under review at *Revista Brasileira de Cartografia*) or credit the authorship of this repository.


## 🧑‍💻 Author
**Bruno Zomignani Perciani**  
Undergraduate Student at the Federal University of ABC (UFABC)  
📧 bruno.perciani@aluno.ufabc.edu.br  

**Supervised by:**  
Prof. Dr. Victor Fernandez Nascimento  
Prof. Dr. Vitor Vieira Vasconcelos  
Prof. Dr. Márcio de Souza Werneck  
