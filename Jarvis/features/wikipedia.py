import wikipedia
import re

def tell_me_about(topic):
    try:
        res = wikipedia.summary(topic, sentences=3)
        return res
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]  # Limiting to first 5 options
        return f"Multiple options found. Did you mean one of these? {', '.join(options)}"
    except Exception as e:
        print(e)
        return False