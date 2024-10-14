from universe import Universe
from entity import Entity, R2


def main() -> None:
    earth = Entity(
        5.972e24,
        R2(0, -1.4960e11),
        render_params = {
            'radius': 6.38,
            'color': (0, 0, 255)
        }
    )
    earth.velocity = R2(3*2.9472e6, 0)

    sun = Entity(
        1.989e30,
        R2(0, 0),
        render_params={
            'radius': 69.6,
            'color': (255, 165, 0)
        }
    )

    my_universe = Universe(earth, sun, G=6.67430e-6)
    my_universe.execute()

if __name__ == '__main__':
    main()