from typing import List


class Solution:
    s: str = ''
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        all_partitions = []
        self.dfs(0, "", [], all_partitions)
        return all_partitions

    def dfs(self, curr_pos, curr_string, substring_list: list[str], all_partitions):
        if curr_pos == len(self.s):
            if curr_string and curr_string[::-1] == curr_string:
                substring_list.append(curr_string)
                all_partitions.append(substring_list)
            return

        ch = self.s[curr_pos]

        potential_string = curr_string + ch
        if potential_string == potential_string[::-1]:
            self.dfs(curr_pos + 1, "", substring_list + [potential_string], all_partitions)

        self.dfs(curr_pos + 1, potential_string, substring_list, all_partitions)






if __name__ == '__main__':
    s = 'aabaac'
    sol = Solution()
    print(sol.partition(s))
