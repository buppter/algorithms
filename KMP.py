"""
author: buppter
datetime: 2019/8/25 14:32
"""


class KMP:

    def gen_pnext(self, p):
        """
        生成 pnext 表
        :param p: str 需要匹配的字符串
        :return: list pnext 表
        """
        if not p:
            return []
        lens = len(p)
        pnext = [float('inf')] * lens
        pnext[0] = 0
        k = 0
        i = 1
        while i < lens:
            if p[i] == p[k]:
                k += 1
                pnext[i] = k
                i += 1
            else:
                if k > 0:
                    k = pnext[k - 1]
                else:
                    pnext[i] = k
                    i += 1
        pnext = self.move_pnext(pnext)
        return pnext

    def move_pnext(self, pnext):
        """
        将 pnext 进行移动，第 0 位表示为 -1
        :param pnext: list pnext 表
        :return: list 调整顺序后的 pnext 表
        """
        for i in range(len(pnext) - 1, 0, -1):
            pnext[i] = pnext[i - 1]
        pnext[0] = -1
        return pnext

    def kmp_search(self, text, pattern):
        """
        :param text: str 主字符串
        :param pattern: str 所需要匹配到的字符串
        :return: list(int) 主字符串的下标，如果匹配不到则返回 -1
        """
        if not text or not pattern or len(pattern) > len(text):
            return -1

        pnext = self.gen_pnext(pattern)

        t_len = len(text)
        p_len = len(pattern)
        i, j = 0, 0
        res = []
        while i < t_len:
            if j == p_len - 1 and text[i] == pattern[j]:
                res.append(i - j)
                j = pnext[j]

            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = pnext[j]
                if j == -1:
                    j += 1
                    i += 1

        return res if res else -1


if __name__ == '__main__':
    k = KMP()
    res = k.kmp_search("ABABABABCABAABABCABAA", "ABABCABAA")
    print(res)
