#ifndef __CAVENDISH__INCLUDE_ENTITY_HPP__
#define __CAVENDISH__INCLUDE_ENTITY_HPP__

#include <R2.hpp>

class Entity
{
private:
    double mass;
    R2 position;
    R2 velocity;
    // dict render_params

public:
    R2 g(Entity& witness, double G);
};


#endif // ! __CAVENDISH_INCLUDE_ENTITY_HPP__