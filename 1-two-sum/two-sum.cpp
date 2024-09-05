class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        //keep the cheked numbers and indexes
        map<int, int> checkednum;
        
        // loop through every element in nums
        for (int i = 0; i<nums.size(); ++i) {
            //find needed num for each
            int num2 = target - nums[i];
            // check the sum of num and num2 to meet target
            if (checkednum.find(num2) != checkednum.end()) {
                return {checkednum[num2], i};
                }
            checkednum[nums[i]] = i;
            }
        return {};
        };
    };
