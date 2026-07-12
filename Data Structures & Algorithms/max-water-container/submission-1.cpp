class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l {0};
        int r = heights.size() - 1;
        int output {0};

        while (l < r) {
            int area = min(heights[l], heights[r]) * (r - l);
            output = max(output, area);

            if (heights[l] <= heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return output;
    }
};
