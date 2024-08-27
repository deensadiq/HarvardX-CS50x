import re

p = re.compile('[a-z]+')

print(p.match(""))

match = p.match("tempo")
print(f"Start: {match.start()}, end: {match.end()}, group: {match.group()}, span: {match.span()}")