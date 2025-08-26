db = db.getSiblingDB('admin');
db.auth('root','root');
db = db.getSiblingDB('TestDB');
db.createCollection('TestCollection');