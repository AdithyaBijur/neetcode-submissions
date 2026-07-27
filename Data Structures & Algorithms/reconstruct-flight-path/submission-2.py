class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort()

        graph = collections.defaultdict(list)

        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])


        def dfs(node, res):
            print(node, res)
            if len(res) == len(tickets) + 1:
                print("here")
                return True
            
            neis = graph[node]
            for i in range(len(neis)):
                graph[node] = neis[:i] + neis[i+1:]
                res.append(neis[i])
                if dfs(neis[i], res):
                    return True
                res.pop()
                graph[node] = neis
             
            return False

        res = ["JFK"]
        dfs("JFK", res)
        return res


            
        