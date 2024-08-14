import webbrowser

def website_opener(domain):
    try:
        if not domain.startswith("www."):
            domain = "www." + domain
        if not domain.endswith(".com"):
            domain += ".com"
        if not domain.startswith("http://") and not domain.startswith("https://"):
            domain = "https://" + domain
        webbrowser.open(domain)
        return True
    except Exception as e:
        print(e)
        return False
