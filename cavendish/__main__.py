from universe import Universe
from entity import Entity
from r2 import R2
from random import randrange


def main() -> None:
    mass1 = Entity(10, R2(0, randrange(-150, 150)))
    mass1.velocity = R2(-5e-2, -1e-1)

    mass2 = Entity(10, R2(randrange(-150, 150), randrange(-150, 150)))
    mass2.velocity = R2(1e-1, 0)

    mass3 = Entity(10, R2(randrange(-150, 150), randrange(-150, 150)))
    mass3.velocity = R2(-5e-2, 1e-1)

    my_universe = Universe(mass1, mass2, mass3)
    my_universe.execute()

if __name__ == '__main__':
    main()