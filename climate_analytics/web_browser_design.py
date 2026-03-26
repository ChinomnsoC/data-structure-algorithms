# **Web Browser Design (IDB)** = Design Browser History (LC 1472)

# Next on your evening list. Here's the question:

# **Part 1:**
# Implement a browser with:
# - `add_to_history(url)` — add URL to history
# - `print_history()` — return all visited URLs in reverse chronological order of **most recent visit**. 
# Deduplicate — if a URL is visited twice, only show it once at its most recent position.

# ```
# add("a.com")
# add("b.com")
# print() → ["b.com", "a.com"]

# add("a.com")
# add("b.com")
# add("a.com")
# print() → ["a.com", "b.com"]
# ```

# **Part 2:** Discuss how you'd implement autocomplete for URLs (no coding needed).
from collections import OrderedDict

class WebBrowserDesign:
    def __init__(self):
        self.url_ordered_dict = OrderedDict()
        
    def add(self, url):
        if not url:
            return
        url = url.lower()
        
        if url not in self.url_ordered_dict:
            self.url_ordered_dict[url] = True
        
        self.url_ordered_dict.move_to_end(url)
    
    def print_history(self):
        return list(reversed(self.url_ordered_dict.keys()))



web_browser_design = WebBrowserDesign()

web_browser_design.add("a.com")
web_browser_design.add("b.com")  
web_browser_design.add("c.com")
web_browser_design.add("a.com")
print(web_browser_design.print_history())