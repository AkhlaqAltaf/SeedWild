def map_soil_to_number(soil):
    soil_types = [
        'Loamy', 'Sandy', 'Clay', 'Silt', 'Peaty', 'Muddy', 'Loam', 'Clayey', 'Rocky',
        'Sandy loam', 'Well-drained', 'Moist', 'Silty', 'Clay loam', 'Silt loam',
        'Swampy', 'Well-draining', 'Sandy Loam', 'Wet', 'Marshy', 'Boggy', 'Damp',
        'Acidic', 'Silty loam', 'Epiphytic', 'Silty Loam', 'Loamy sand', 'Silty clay',
        'Dry', 'Epiphyte', 'Clay Loam', 'Alluvial', 'Humus', 'Peat', 'Slightly Acidic',
        'Neutral', 'Humus-rich', 'Slightly acidic', 'Chalky', 'Volcanic loam',
        'Laterite soil', 'Red soil', 'Alluvial soil', 'Silt Loam', 'Sandy Clay',
        'Organic', 'Sedge', 'Sandy clay loam', 'Rich', 'Rich loamy soil',
        'Sandy Clay Loam', 'Volcanic', 'Loamy soil'
    ]

    soil_categories = {soil: index for index, soil in enumerate(sorted(set(soil_types)))}
    return soil_categories.get(soil)


def scale_to_tens_rounded(value):
    return round(value / 10)


def categorize_season(temp):
    if temp < -25:
        return 0  # 'Extremely Cold'
    elif -25 <= temp < -20:
        return 1  # 'Severely Cold'
    elif -20 <= temp < -15:
        return 2  # 'Intensely Cold'
    elif -15 <= temp < -10:
        return 3  # 'Very Cold'
    elif -10 <= temp < -5:
        return 4  # 'Cold'
    elif -5 <= temp < 0:
        return 5  # 'Chilly'
    elif 0 <= temp < 5:
        return 6  # 'Cool'
    elif 5 <= temp < 10:
        return 7  # 'Mild Cool'
    elif 10 <= temp < 15:
        return 8  # 'Mild'
    elif 15 <= temp < 20:
        return 9  # 'Mild Warm'
    elif 20 <= temp < 25:
        return 10  # 'Warm'
    elif 25 <= temp < 30:
        return 11  # 'Moderate Hot'
    elif 30 <= temp < 35:
        return 12  # 'Hot'
    elif 35 <= temp < 40:
        return 13  # 'Very Hot'
    elif 40 <= temp < 45:
        return 14  # 'Extremely Hot'
    elif 45 <= temp < 50:
        return 15  # 'Scorching'
    elif 50 <= temp < 55:
        return 16  # 'Inferno'
    elif 55 <= temp < 60:
        return 17  # 'Blazing'
    elif 60 <= temp < 65:
        return 18  # 'Burning'
    elif 65 <= temp < 70:
        return 19  # 'Melting'


def get_processed_data(data):
    print("Data Before ... ", data)
    data['temperature'] = data['temperature']
    data['humidity_rate_tens'] = scale_to_tens_rounded(data['humidity_rate_tens'])
    data['hydrometry_rate_tens'] = scale_to_tens_rounded(data['hydrometry_rate_tens'])
    data['sunshine_rate_tens'] = scale_to_tens_rounded(data['sunshine_rate_tens'])
    data['rainfall_tens'] = scale_to_tens_rounded(data['rainfall_tens'])
    # data['soil_num'] = map_soil_to_number(data['soil_num'])

    return data
