import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()

#cur.execute('CREATE TABLE files(uuid, md5sum, sha1sum, sha256sum, sha512sum)')

#cur.execute('CREATE TABLE events(eventid, event_type, timestamp)')

#cur.execute('CREATE TABLE rules(ruleid, rule_type, rule_name, rule_description, rule_author, rule_version, rule_status, rule_tags, rule_events, rule_actions, rule_conditions )')

def ingestFile(file):
    cur.execute('INSERT INTO files(blob) VALUES(readfile(file))')


