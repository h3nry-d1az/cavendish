#include <cstdio>
#include <SFML/Graphics.hpp>
#include <R2.hpp>

int main()
{
    R2 my_vec(1, 2);
    R2 my_other_vec(5, -1);
    printf("%f", my_vec*my_other_vec);
    printf("%f", abs(my_vec));
    sf::RenderWindow window(sf::VideoMode(200, 200), "SFML works!");
    sf::CircleShape shape(100.f);
    shape.setFillColor(sf::Color::Green);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(shape);
        window.display();
    }

    return 0;
}