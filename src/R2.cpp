#include <R2.hpp>
#include <cmath>


R2 R2::operator+(R2& other) { return R2(x + other.x, y + other.y); }
R2 R2::operator-(R2& other) { return R2(x - other.x, y - other.y); }
R2 R2::operator*(double scalar) { return R2(x*scalar, y*scalar); }
double R2::operator*(R2& other) { return x*other.x + y*other.y; }

double abs(R2& self)
{
    double x = self.X();
    double y = self.Y();
    return sqrt(x*x + y*y);
}