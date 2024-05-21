import carla
import argparse

argparser = argparse.ArgumentParser(description="Move the spectator to a specific spawn point")
# add index argument
argparser.add_argument(
    '-i', '--index',
    metavar='N',
    default=0,
    type=int,
    help='Index of the spawn point to move the spectator to')

def move_spectator_to_spawn_point(world, spawn_point_index):
    # Get the map
    carla_map = world.get_map()
    
    # Retrieve all the spawn points
    spawn_points = carla_map.get_spawn_points()
    
    if spawn_points and 0 <= spawn_point_index < len(spawn_points):
        spawn_point = spawn_points[spawn_point_index]
        
        # Get the spectator object
        spectator = world.get_spectator()
        
        # Move the spectator to the specified spawn point
        spectator.set_transform(carla.Transform(spawn_point.location + carla.Location(z=1.5),
                                                spawn_point.rotation))
        print(f"Moved spectator to spawn point #{spawn_point_index}")
    else:
        print(f"Invalid spawn point index: {spawn_point_index}, make sure it is between 0 and {len(spawn_points) - 1}")

def main():
    # Connect to the CARLA server
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    
    # Get the world object
    world = client.get_world()
    
    # Specify the spawn point index to move to
    spawn_point_index = argparser.parse_args().index
    
    # Move the spectator to the specified spawn point
    move_spectator_to_spawn_point(world, spawn_point_index)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Cancelled by user. Bye!')
