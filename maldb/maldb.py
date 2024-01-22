import sqlite3
import uuid
import fileid

from hashes import md5sum, sha1sum, sha256sum, sha512sum, hash_is_md5, hash_is_sha1, hash_is_sha256, hash_is_sha512

con = sqlite3.connect('test.db')
cur = con.cursor()

def create_db():
    cur.execute('CREATE TABLE files(fileid, file, md5sum, sha1sum, sha256sum, sha512sum, file_size, file_type)')
    cur.execute('CREATE TABLE FileSystem(fileid, parent_id, child_id)')
    
    #cur.execute('CREATE TABLE geneology(gen_id, directory, parent_id, child_id)')

    cur.execute('CREATE TABLE events(eventid, event_type, tlp_cond, timestamp, event_description, gen_id))')
    
    #cur.execute('CREATE TABLE rules(ruleid, rule_type, rule_name, rule_description, rule_author, rule_version, rule_status, rule_tags, rule_events, rule_actions, rule_conditions )')
    
    con.commit()

def insert_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        filename = f.name

    cur.execute('INSERT INTO files VALUES(?, ?, ?, ?, ?, ?)', (uuid.uuid4().hex, data, md5sum(data), sha1sum(data), sha256sum(data), sha512sum(data), len(data),fileid.file_on_buffer(data)))
    cur.execute('INSERT INTO events VALUES(?, ?, ?)', (uuid.uuid4().hex, 'file_added', datetime.datetime.now(), filename, file_extension)))
    con.commit()
    
def insert_event(eventid, event_type, timestamp):
    cur.execute('INSERT INTO events VALUES(?, ?, ?)', (eventid, event_type, timestamp))
    con.commit()

def query_hash(qhash):
    if hash_is_md5(qhash):
        cur.execute('SELECT uuid FROM files WHERE md5sum=?', (qhash,))
        print("Searching for MD5 hash: " + qhash)
        result = cur.fetchone()

    elif hash_is_sha1(qhash):
        cur.execute('SELECT uuid FROM files WHERE sha1sum=?', (qhash,))
        print("Searching for SHA1 hash: " + qhash)
        result = cur.fetchone()

    elif hash_is_sha256(qhash):
        cur.execute('SELECT uuid FROM files WHERE sha256sum=?', (qhash,))
        print("Searching for SHA256 hash: " + qhash)
        result = cur.fetchone()

    elif hash_is_sha512(qhash):
        cur.execute('SELECT uuid FROM files WHERE sha512sum=?', (qhash,))
        print("Searching for SHA512 hash: " + qhash)
        result = cur.fetchone()

    else:
        return None

    return uuid.UUID(result[0])
