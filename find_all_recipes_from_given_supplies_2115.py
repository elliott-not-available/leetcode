class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:

        # # brute force:
        # # go through recipe, if ingredient in recipe list, add to check later
        # # if not check supplies contain ingredients
        # # if all ingredients exist, add recipe to supplies

        # THIS DOES NOT WORK FOR DOUBLE+ nested recipies

        # res = []
        # check_later = []

        # for i in range(len(recipes)):
        #     r = recipes[i]
            
        #     ing_exist = True

        #     for ing in ingredients[i]:
        #         if ing in recipes:
        #             ing_exist = False
        #             check_later.append(i)
        #             break

        #         if ing not in supplies:
        #             ing_exist = False
        #             break
        #         ing_exist = True

        #     if ing_exist:
        #         res.append(r)
        #         supplies.append(r)

        # for l in check_later:
        #     r = recipes[l]

        #     ing_exist = True

        #     for ing in ingredients[l]:
        #         if ing not in supplies:
        #             ing_exist = False
        #             break
        #         ing_exist = True

        #     if ing_exist:
        #         res.append(r)
        # return res



        # ## working brute force, memory limit exceeded
        # res = []
        # rec_map = {}
        # for i in range(len(recipes)):
        #     rec_map[recipes[i]] = ingredients[i]

        # recs = rec_map.keys()

        # for k, v in rec_map.items():

        #     new_vs = []

        #     for j in range(len(v)):
        #         if v[j] not in recs:
        #             new_vs.append(v[j])
        #         else:
        #             new_vs += rec_map[v[j]]

        #     rec_map[k] = new_vs

        # set_sup = set(supplies)

        # for r in recipes:
        #     if set(rec_map[r]).issubset(set_sup):
        #         res.append(r)
        #     # if rec_map[r] in supplies:
        #     #     res.append(r)
        # return res




        # graph dfs neet
        
        can_cook = {s:True for s in supplies}
        re_index = {r:i for i, r in enumerate(recipes)}

        def dfs(re):

            if re in can_cook:
                return can_cook[re]
            
            if re not in recipes:
                return False

            i = re_index[re]
            can_cook[re] = False
            
            for nei in ingredients[i]:
                if not dfs(nei):
                    return False
            can_cook[re] = True
            return can_cook[re]

        return [r for r in recipes if dfs(r)]
        