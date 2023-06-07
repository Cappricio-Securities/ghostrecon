#!/usr/bin/env node
/**
 * gh0str3con
 * gh0str3con is a All in one cloud based web Recon tool.
 *
 * @author karthikeyan V (karthithehacker) <https://karthithehacker.com>
 */
const lowdb = require('lowdb');
const FileSync = require('lowdb/adapters/FileSync');

class targetdb {
    constructor(targetname,scopes,reportpath) {
        let cdb = lowdb(new FileSync('database/db/' + targetname + '.json'))
        cdb.defaults({
            recondb:{
            targetname,
            status: "none",
            scope: scopes,
            infos: []
            }
        }).write()
        return cdb;
    }
}
class targetdbload {
    constructor(targetname,scopes,live,openport,recinfo) {
        let rec = lowdb(new FileSync('database/db/' + targetname + '.json'))
        rec.set('recondb.recOn' , 'completed').write();
        rec.get('recondb.infos').push({subs:scopes,live:live,openport:openport}).write();
    }
}
class initializ {
    constructor(targetname) {
        let cdb = lowdb(new FileSync('database/db/' + targetname + '.json'))
        let data_scope = cdb.get('recondb.scope').value(); 
        return data_scope
        
    }
}
class retrive {
    constructor(targetname) {
        let cdb = lowdb(new FileSync('database/db/' + targetname + '.json'))
        let data_scope = cdb.get('recondb.infos').value(); 
        return data_scope
        
    }
}

module.exports = {
    initializ: initializ,
    targetdb: targetdb,
    targetdbload: targetdbload,
    retrive: retrive

};


