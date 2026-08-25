def find_itinerary(tickets: list[list[str]]) -> list[str]:
    # TODO: implement (Hierholzer's algorithm, always try the lexically smallest destination first)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", find_itinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]),
          ["JFK", "MUC", "LHR", "SFO", "SJC"])
    check("with revisit", find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]),
          ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
