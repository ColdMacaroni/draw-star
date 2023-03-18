import pygame
from math import pi, cos, sin

size = 600, 600

def create_star(centre, len_to_spike = 100, rot = 0, sides = 5, spike_angle = None):
    pts = []
    # We have a small regular shape on the inside, and then a bigger one going out
    # interior angles = (n-2) * 180
    
    # I couldnt tell you why, but it's gotta be like this
    len_to_spike /= 1.5

    # If the shape is split into triangles, what's the angle at the centre.
    half_centre_angle = 2 * pi / (sides * 2)

    # If the shape is split into rectangle triangles, what's the angle at the corners?
    half_inner_angle = ((sides - 2) * pi/2)/ sides

    # This is the angle between the centre, a corner, and the spike tip.
    suplementary_corner_angle = pi - (half_inner_angle if spike_angle is None else spike_angle/2)

    # half the angle at the end of a star spike
    spike_angle = half_inner_angle - half_centre_angle

    # Radius of circle in which the spikes will touch
    outer_radius_ratio = (sin(suplementary_corner_angle)/sin(spike_angle))

    # Calculate based on values given.
    inner_radius = len_to_spike / outer_radius_ratio
    outer_radius = len_to_spike

    # We want the star to be "standing up" so the first inner corner needs to be pointing down
    threequarters_offset = 3 * pi / 2

    # Do some trig to get each pt as a coordinate, alternate between the inner and outer points.
    for idx, i in enumerate(range(sides * 2)):
        if idx % 2:
            radius = inner_radius
        else:
            radius = outer_radius
        
        pts.append(
            (centre[0] + radius * cos(rot + threequarters_offset + half_centre_angle * i),
             centre[1] + radius * sin(rot + threequarters_offset + half_centre_angle * i)))

    return pts

def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Pos, dist between centre and spike, rotation, spikes, angle between spikes
    pts = create_star((300, 300), 100, 0, 5, None)

    running = True
    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = False

        screen.fill((0xffffff))

        pygame.draw.lines(screen, (0x000000), True, pts, 3)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()