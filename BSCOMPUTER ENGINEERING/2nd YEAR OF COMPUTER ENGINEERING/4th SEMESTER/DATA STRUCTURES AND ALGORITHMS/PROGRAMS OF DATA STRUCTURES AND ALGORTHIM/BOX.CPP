#include <iostream>
using namespace std;
class AREA_VOL;
class BOX {
private:
    double length;

public:
    BOX(double len = 0) : length(len) {}
    void setLength(double len) {
        length = len;
    }
    friend void calculateAreaVolume(const BOX& box, const AREA_VOL& areaVol);
};
class AREA_VOL {
public:
    friend void calculateAreaVolume(const BOX& box, const AREA_VOL& areaVol);
};
void calculateAreaVolume(const BOX& box, const AREA_VOL& areaVol) {
    double area = 6 * box.length * box.length;
    double volume = box.length * box.length * box.length;

    cout << "Area of the box: " << area << endl;
    cout << "Volume of the box: " << volume << endl;
}
int main() {
    BOX myBox(5); 
    AREA_VOL areaVol; 
    calculateAreaVolume(myBox, areaVol);
    return 0;
}