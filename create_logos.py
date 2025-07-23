#!/usr/bin/env python3
"""
Logo creation script for Just Rewards brand logos.
Creates simple, reliable placeholder logos for brands.
"""

import os
from pathlib import Path

# Brand colors and info
BRANDS = {
    'tesco': {'color': '#00539F', 'text': 'TESCO'},
    'sainsburys': {'color': '#FF8200', 'text': 'Sainsbury\'s'},
    'waitrose': {'color': '#006747', 'text': 'Waitrose'},
    'morrisons': {'color': '#FFD100', 'text': 'Morrisons'},
    'asda': {'color': '#00A651', 'text': 'ASDA'},
    'aldi': {'color': '#003D82', 'text': 'ALDI'},
    'lidl': {'color': '#0050AA', 'text': 'Lidl'},
    'subway': {'color': '#00543C', 'text': 'SUBWAY'},
    'costa': {'color': '#E31E24', 'text': 'Costa'},
    'starbucks': {'color': '#00704A', 'text': 'Starbucks'},
    'pret': {'color': '#D32F2F', 'text': 'Pret'},
    'greggs': {'color': '#0066CC', 'text': 'Greggs'},
    'mcdonalds': {'color': '#FFC72C', 'text': 'McDonald\'s'},
    'boots': {'color': '#0033A0', 'text': 'Boots'},
    'superdrug': {'color': '#E91E63', 'text': 'Superdrug'},
    'next': {'color': '#000000', 'text': 'NEXT'},
    'primark': {'color': '#004B87', 'text': 'Primark'},
    'marks-spencer': {'color': '#006747', 'text': 'M&S'},
    'nandos': {'color': '#D2001F', 'text': 'Nando\'s'},
    'apple': {'color': '#000000', 'text': 'Apple'},
    'spotify': {'color': '#1DB954', 'text': 'Spotify'},
}

def create_svg_logo(brand_name, brand_info):
    """Create a simple SVG logo for a brand."""
    color = brand_info['color']
    text = brand_info['text']
    
    # Calculate font size based on text length
    font_size = max(16, min(32, 200 // len(text)))
    
    svg_content = f'''<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="{color}" rx="20"/>
  <text x="100" y="100" font-family="Arial, sans-serif" font-size="{font_size}" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">{text}</text>
</svg>'''
    
    return svg_content

def main():
    """Create all brand logos."""
    logos_dir = Path('logos')
    logos_dir.mkdir(exist_ok=True)
    
    for brand_name, brand_info in BRANDS.items():
        svg_content = create_svg_logo(brand_name, brand_info)
        logo_path = logos_dir / f'{brand_name}.svg'
        
        with open(logo_path, 'w') as f:
            f.write(svg_content)
        
        print(f'Created logo: {logo_path}')
    
    print(f'Successfully created {len(BRANDS)} brand logos!')

if __name__ == '__main__':
    main()
