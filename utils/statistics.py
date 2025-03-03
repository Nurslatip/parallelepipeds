import json
from utils.functions import process 

def stats(parallelepipeds: dict) -> dict:
    len_ = len(parallelepipeds)
    if len_ == 0:
        return {}  
    

    char_values = [process(float(val['a']), float(val['b']), float(val['c'])) for val in parallelepipeds.values()]

  
    statistics = {
        'avg_diag': str(round(sum(float(k['diag']) for k in char_values) / len_, 2)),
        'avg_volume': str(round(sum(float(k['volume']) for k in char_values) / len_, 2)),
        'avg_surface_area': str(round(sum(float(k['surface_area']) for k in char_values) / len_, 2)),
        'avg_alpha': str(round(sum(float(k['alpha']) for k in char_values) / len_, 2)),
        'avg_beta': str(round(sum(float(k['beta']) for k in char_values) / len_, 2)),
        'avg_gamma': str(round(sum(float(k['gamma']) for k in char_values) / len_, 2)),
        'avg_radius_described_sphere': str(round(sum(float(k['radius_described_sphere']) for k in char_values) / len_, 2)),
        'avg_volume_described_sphere': str(round(sum(float(k['volume_described_sphere']) for k in char_values) / len_, 2))
    }
    
    return statistics
