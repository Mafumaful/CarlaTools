import carla

def print_spectator_location(world):
    # Get the spectator object
    spectator = world.get_spectator()
    
    # Get the transform of the spectator
    transform = spectator.get_transform()
    
    # Print the location and rotation of the spectator
    location = transform.location
    rotation = transform.rotation
    print(f'Spectator Location: (x: {location.x}, y: {location.y}, z: {location.z})')
    print(f'Spectator Rotation: (pitch: {rotation.pitch}, yaw: {rotation.yaw}, roll: {rotation.roll})')

def main():
    # Connect to the CARLA server
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    
    # Get the world object
    world = client.get_world()
    
    # Print the spectator's current location
    print_spectator_location(world)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Cancelled by user. Bye!')
