class StringIterator:

    from collections import deque

    def __init__(self, compressedString: str):
        self.comp_str = deque(compressedString)
        self.uncomp_str_chars = deque([])
        self.uncomp_str_nums = deque([])
        while len(self.comp_str) > 0:
            char = self.comp_str.popleft()
            _num = ''
            while self.comp_str and self.comp_str[0] in '0123456789':
                _num += self.comp_str.popleft()
            num = int(_num)
            self.uncomp_str_chars.append(char)
            self.uncomp_str_nums.append(num)

    def next(self) -> str:
        if len(self.uncomp_str_chars) > 0:
            char = self.uncomp_str_chars[0]
            self.uncomp_str_nums[0] -= 1
            if self.uncomp_str_nums[0] == 0:
                self.uncomp_str_nums.popleft()
                self.uncomp_str_chars.popleft()
            return char
        return ' '

    def hasNext(self) -> bool:
        return len(self.uncomp_str_chars) > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
