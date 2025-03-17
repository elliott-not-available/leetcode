# remove_sub-folders_from_the_filesystem_1233
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution_og:
    # timelimit exceeded
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        base_folders = [folder[0]]

        for f in folder:
            sub = False
            for i, b in enumerate(base_folders):
                if b.startswith(f):
                    # print(f"replace base: {b} starts with {f}")
                    if b == f:
                        duplicate = True
                        # print("duplicate ignored")
                    elif "/" in b.split(f)[1]:
                        # print(f"{b} starts with {f}")
                        base_folders[i] = f
                        sub = True
                        continue

                if f.startswith(b):
                    # print(f"sub_fodler: {f} starts with {b}")
                    if f == b:
                        duplicate = True
                        # print("duplicate ignored")
                    elif "/" in f.split(b)[1]:
                        # print(f"{f} starts with {b}")
                        sub = True
                        continue

            if not sub:
                base_folders.append(f)
            
        return list(set(base_folders))
    


class Solution:
    # neeted
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder_set = set(folder)
        result = []

        for f in folder:
            result.append(f)
            for i in range(len(f)):
                if f[i] == "/" and f[:i] in folder_set:
                    result.pop()
                    break

        return result
    


class Trie:
    def __init__(self):
        self.children = {} # string -> Trie
        self.end_of_folder = False

    def add(self, path):
        cur = self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end_of_folder = True
    
    def prefix_search(self, path):
        cur = self
        folders = path.split("/")

        for i in range(len(folders)-1):
            cur = cur.children[folders[i]]
            if cur.end_of_folder:
                return True
        return False


class Solution_prefix:
    def removeSubfolders(self, folder: list[str]) -> list[str]:

        trie = Trie()

        for f in folder:
            trie.add(f)

        result = []
        for f in folder:
            if not trie.prefix_search(f):
                result.append(f)

        return result