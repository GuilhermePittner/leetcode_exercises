class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        n_check = []
        n_final = []

        for x in arr:
            if not x in n_check:
                # print(f'x {x} não está lá')
                ocorrencias = arr.count(x)

                sub_lst = [x, ocorrencias]
                n_final.append(sub_lst)

                n_check.append(x)


        print(n_check)
        print(n_final)

        final_check = []
        for y in n_final:
            
            if y[1] in final_check:
                return False

            else:
                final_check.append(y[1])

        return True
