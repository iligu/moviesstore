REGIONS = {
    'northeast' : {'label': 'Northeast', 'lat':43, 'lng': -76},
    'midwest' : {'label': 'Midwest', 'lat':43, 'lng': -96},
    'south' : {'label': 'South', 'lat':33, 'lng': -88},
    'west' : {'label': 'West', 'lat':42, 'lng': -115},
}
REGION_CHOICES = [(key, r['label']) for key, r in REGIONS.items()]