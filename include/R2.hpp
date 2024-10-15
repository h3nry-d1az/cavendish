#ifndef __CAVENDISH__INCLUDE_R2_HPP__
#define __CAVENDISH__INCLUDE_R2_HPP__

/* The name R2 stands for
 * the real plane, i.e., ℝ².
 */
class R2
{
private:
    double x;
    double y;

public:
    double X() { return x; }
    double Y() { return y; }

    R2 operator+(R2& other);
    R2 operator-(R2& other);
    R2 operator*(double scalar);
    double operator*(R2& other);

    R2(double x_, double y_) : x(x_), y(y_) {};
};

double abs(R2& self);


#endif // ! __CAVENDISH_INCLUDE_R2_HPP__