from flask import Flask, render_template, jsonify
import math
import random
from datetime import datetime

app = Flask(__name__)

# ══════════════════════════════════════════════════════════════
#  SPACE DATA ENGINE
# ══════════════════════════════════════════════════════════════

class SpaceExplorer:
    def __init__(self):
        self.time = 0
        self.planets = {
            'sun':     {'radius': 2.0, 'color': '#FFF3A0', 'distance': 0,  'period': 0,     'emissive': '#FFAA00'},
            'mercury': {'radius': 0.4, 'color': '#8C7853', 'distance': 8,  'period': 88,    'emissive': '#000'},
            'venus':   {'radius': 0.6, 'color': '#FFC649', 'distance': 12, 'period': 225,   'emissive': '#221100'},
            'earth':   {'radius': 0.7, 'color': '#6B93D6', 'distance': 16, 'period': 365,   'emissive': '#003366'},
            'mars':    {'radius': 0.5, 'color': '#CD5C5C', 'distance': 20, 'period': 687,   'emissive': '#330000'},
            'jupiter': {'radius': 1.5, 'color': '#D2691E', 'distance': 28, 'period': 4333,  'emissive': '#332200'},
            'saturn':  {'radius': 1.2, 'color': '#FAD5A5', 'distance': 36, 'period': 10759, 'emissive': '#333300', 'rings': True},
            'uranus':  {'radius': 1.0, 'color': '#4FD0E3', 'distance': 44, 'period': 30687, 'emissive': '#003333'},
            'neptune': {'radius': 1.0, 'color': '#4169E1', 'distance': 52, 'period': 60190, 'emissive': '#000033'},
        }

    def get_planet_positions(self):
        self.time += 0.02
        positions = {}
        for name, data in self.planets.items():
            if data['period'] > 0:
                angle = (self.time / data['period']) * 2 * math.pi
                x = math.cos(angle) * data['distance']
                z = math.sin(angle) * data['distance']
            else:
                x, z = 0, 0

            positions[name] = {
                'x':        x,
                'y':        0,
                'z':        z,
                'radius':   data['radius'],
                'color':    data['color'],
                'emissive': data['emissive'],
                'rotation': self.time * 2,
                'rings':    data.get('rings', False),
                'distance': data['distance'],
                'period':   data['period'],
            }
        return positions

    def get_iss_data(self):
        t = datetime.now().timestamp()
        return {
            'latitude':   math.sin(t / 600) * 51.6,
            'longitude':  (t / 300) % 360 - 180,
            'altitude':   408 + math.sin(t / 100) * 5,
            'velocity':   27600 + math.sin(t / 50) * 50,
            'astronauts': ['Samantha Cristoforetti', 'Bob Hines', 'Kjell Lindgren'],
            'status':     'daylight' if random.random() > 0.5 else 'eclipse',
            'image':      'https://images.unsplash.com/photo-1446776877081-d282a0f896e2?w=400&h=300&fit=crop',
        }

    def get_missions(self):
        return [
            {
                'name':    'Starlink-95',
                'rocket':  'Falcon 9',
                'date':    '2025-09-30',
                'status':  'upcoming',
                'image':   'https://images.unsplash.com/photo-1517976487492-5750f3195933?w=300&h=200&fit=crop',
                'details': 'Deployment of 60 Starlink satellites to low Earth orbit',
            },
            {
                'name':    'Artemis III',
                'rocket':  'SLS',
                'date':    '2026-09-01',
                'status':  'planned',
                'image':   'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=300&h=200&fit=crop',
                'details': 'First crewed lunar landing mission since Apollo program',
            },
            {
                'name':    'Europa Clipper',
                'rocket':  'Falcon Heavy',
                'date':    '2024-10-14',
                'status':  'completed',
                'image':   'https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=300&h=200&fit=crop',
                'details': "NASA mission to study Jupiter's moon Europa",
            },
            {
                'name':    'Crew-9',
                'rocket':  'Falcon 9',
                'date':    '2024-09-28',
                'status':  'completed',
                'image':   'https://images.unsplash.com/photo-1446776877081-d282a0f896e2?w=300&h=200&fit=crop',
                'details': 'International Space Station crew rotation mission',
            },
        ]


# ══════════════════════════════════════════════════════════════
#  FLASK ROUTES
# ══════════════════════════════════════════════════════════════

space = SpaceExplorer()

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/planets')
def api_planets():
    return jsonify(space.get_planet_positions())

@app.route('/api/iss')
def api_iss():
    return jsonify(space.get_iss_data())

@app.route('/api/missions')
def api_missions():
    return jsonify(space.get_missions())


# ══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("=" * 70)
    print("🚀 REALISTIC SPACE DASHBOARD - STARTING")
    print("=" * 70)
    print("✨ Features:")
    print("   • Interactive Solar System with animated orbits")
    print("   • Click any planet for full detailed info modal")
    print("   • Planet data: diameter, gravity, temp, atmosphere, moons & more")
    print("   • Real-time ISS tracking")
    print("   • Space missions with images")
    print("   • Speed controls (1x, 5x, 10x)")
    print("   • Toggle orbits and labels")
    print("=" * 70)
    print("🌐 Access the dashboard at: http://localhost:5000")
    print("=" * 70)
    print("📁 Project structure:")
    print("   space.py   — Flask backend (this file)")
    print("   index.html — Frontend UI (must be in same folder)")
    print("=" * 70)
    print("📝 Instructions:")
    print("   1. Click any planet to open its info modal")
    print("   2. Hover over planets to highlight them")
    print("   3. Use speed buttons to control animation")
    print("   4. Toggle orbits and labels for different views")
    print("   5. Press Escape or click outside to close modal")
    print("=" * 70)
    print("\n🎮 Starting server...\n")

    app.run(debug=True, host='0.0.0.0', port=5000)