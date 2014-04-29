from ConfigParser import SafeConfigParser

parser = SafeConfigParser()

parser.read('simple.ini')

print parser.get('bug_tracker', 'username')
print parser.get('bug_tracker', 'password')
print parser.get('bug_tracker', 'url')
