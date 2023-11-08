"""
This file is used to configure Apache Superset. The SECRET_KEY below was created randomly using this command ' openssl rand -base64 42'.
Apache Superset will not deploy without a secure secret key specified in this file. MAPBOX_API_KEY only has to be filled if you want to 
utilize the map visualizations inside Superset. Otherwise, you will just have blank maps.
 """

SECRET_KEY = 'jnDid1WMi1TrCtCwptkiiakZOFAonkKZAS47ej+scFrDKqDvPXf+eAKB'
MAPBOX_API_KEY = 'pk.eyJ1IjoiZXJuZXN0MzQ0MyIsImEiOiJjbG5tNnhiYjAyNG52Mm5wZWc2a2dtcXhqIn0.a5EsNac0sG2GS25SLl1XYA'
MAPBOX_MAP_STYLE = 'mapbox://styles/ernest3443/clo60v514008j01r7c21y1e6o'
FEATURE_FLAGS = {
    'HORIZONTAL_FILTER_BAR':True,
    "ALERT_REPORTS": True, 
    "ENABLE_JAVASCRIPT_CONTROLS":True

}