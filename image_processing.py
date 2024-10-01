import os
import random
from PIL import Image
import numpy as np
from matplotlib import colors
import requests

main_colors = {
    'red': '#FF0000',
    'orange': '#FFA500',
    'yellow': '#FFFF00',
    'green': '#008000',
    'blue': '#0000FF',
    'indigo': '#4B0082',
    'violet': '#EE82EE'
}

def get_random_image(folder_path):
    images = [f for f in os.listdir(folder_path) if f.endswith(('jpg', 'jpeg', 'png'))]
    return os.path.join(folder_path, random.choice(images))

def get_average_color(image_path):
    image = Image.open(image_path)
    np_image = np.array(image)
    avg_color = np.mean(np_image, axis=(0, 1))  # Calculate mean for RGB values
    avg_color = avg_color[:3] / 255  # Normalize the RGB values
    return avg_color

def find_nearest_color(avg_color):
    min_dist = float('inf')
    nearest_color = None
    for color_name, hex_value in main_colors.items():
        rgb_color = np.array(colors.to_rgb(hex_value))
        dist = np.linalg.norm(rgb_color - avg_color)
        if dist < min_dist:
            min_dist = dist
            nearest_color = color_name
    return nearest_color

def upload_image_to_imgur(image_path, client_id):
    url = "https://api.imgur.com/3/upload"
    headers = {
        "Authorization": f"Client-ID {client_id}"
    }
    with open(image_path, 'rb') as img:
        data = {'image': img.read(), 'type': 'file'}
        response = requests.post(url, headers=headers, files=data)

    if response.status_code == 200:
        json_response = response.json()
        image_url = json_response['data']['link']
        return image_url
    else:
        raise Exception(f"Failed to upload image: {response.status_code} - {response.text}")
