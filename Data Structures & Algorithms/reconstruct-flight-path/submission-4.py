class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)

        itinerary = []

        def dfs(src):
            while graph[src]:
                nei = graph[src].pop()
                dfs(nei)
            itinerary.append(src)

        dfs("JFK")
        return itinerary[::-1]