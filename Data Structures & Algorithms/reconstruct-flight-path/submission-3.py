class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)

        itinerary = ["JFK"]

        def dfs(src):
            if len(itinerary) == len(tickets) + 1:
                return True

            for i in range(len(graph[src])):
                dst = graph[src].pop(i)
                itinerary.append(dst)

                if dfs(dst):
                    return True

                itinerary.pop()
                graph[src].insert(i, dst)

            return False

        dfs("JFK")
        return itinerary