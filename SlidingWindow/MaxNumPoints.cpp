#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using std::vector;
#define PI 3.14159265358979


class Solution {
    const double eps = 1e-8;
public:
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        // trans points to angles
        vector<double> angles;
        int cnt = 0;
        for (auto p : points) {
            double ang = to_angle(p[0] - location[0], p[1] - location[1]);
            if (ang < 0)
                cnt++;
            else
                angles.push_back(ang);
        }
        std::sort(angles.begin(), angles.end());
        const double _angle = angle * PI / 180.0 + eps;
        const double pi2 = 2 * PI;
        int size = angles.size();
        
        for (int i = 0; i < size && angles[i] <= _angle; i++)
            angles.push_back(angles[i] + pi2);
        
        int right = 0, ans = 0;
        size = angles.size();
        for (int i = 0; i < size; i++) {
            while (right+1 < size && angles[right+1] - angles[i] <= _angle)
                right++;
            ans = std::max(ans, right - i + 1);
        }

        return ans + cnt;
    }

    double to_angle(double x, double y) {
        if (x == 0 and y == 0) return -1;
        double theta = atan2(y, x);
        if (theta < 0)
            return 2*PI + theta;
        return theta;
    }
};

int main()
{
    // double x = 0, y = sqrt(3);
    // std::cout << x << ' ' << y << '\n';
    // // double theta = atan(y / x) * 180 / PI;
    // double theta2 = atan2(y, x) * 180 / PI;
    // std::cout << theta2 << '\n';
    vector<vector<int>> points{{0,0}, {0,2}};
    int angle=90;
    vector<int> location {1,1};
    Solution solu;
    int ans = solu.visiblePoints(points, angle, location);
    std::cout << ans << '\n';
    return 0;
}