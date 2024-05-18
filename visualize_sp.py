import carla
import random

def main():
    # Connect to the CARLA server
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    
    # Get the world object
    world = client.get_world()

    # Get the map
    carla_map = world.get_map()
    
    # Retrieve all the spawn points
    spawn_points = carla_map.get_spawn_points()
    
    # Get the spectator object
    spectator = world.get_spectator()
    
    # Display each spawn point
    for i, spawn_point in enumerate(spawn_points):
        # Draw a box at each spawn point location
        world.debug.draw_box(carla.BoundingBox(spawn_point.location, carla.Vector3D(1, 1, 0.5)),
                             spawn_point.rotation,
                             0.1,  # thickness of the box lines
                             carla.Color(255, 0, 0, 0),  # red color with no alpha transparency
                             life_time=10.0)
        
        # Draw an arrow indicating the spawn point orientation
        world.debug.draw_arrow(spawn_point.location,
                               spawn_point.location + spawn_point.rotation.get_forward_vector() * 2,
                               thickness=0.1,
                               arrow_size=0.2,
                               color=carla.Color(0, 255, 0, 0),  # green color with no alpha transparency
                               life_time=10.0)
        
        # Draw the spawn point number
        world.debug.draw_string(spawn_point.location + carla.Location(z=2),
                                f'#{i}',
                                draw_shadow=False,
                                color=carla.Color(255, 255, 255, 0),  # white color with no alpha transparency
                                life_time=10.0,
                                persistent_lines=True)
    
    # Move the spectator to a suitable position to view all the spawn points
    if spawn_points:
        first_spawn_point = spawn_points[0]
        spectator.set_transform(carla.Transform(first_spawn_point.location + carla.Location(z=50),
                                                carla.Rotation(pitch=-90)))
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Cancelled by user. Bye!')


