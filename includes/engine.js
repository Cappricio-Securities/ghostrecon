#!/usr/bin/env node
/**
 * gh0str3con
 * gh0str3con is a All in one cloud based web Recon tool.
 *
 * @author karthikeyan V (karthithehacker) <https://karthithehacker.com>
 */

const { exec } = require("child_process");
const dbs = require('./dbgateway');
const CONST = require('./const');


savepath = CONST.savepath


function wrecking(targetname,savepath) // This function is used to update and remove unwanted attacks
{
    exec("python includes/bin/wrecking.py "+targetname +" "+savepath+ " &", (error, stdout, stderr) => {
});
}


function makedir(targetname) // This function is used to update and remove unwanted attacks
{
    exec("python includes/bin/initialization.py "+targetname+ " "+savepath, (error, stdout, stderr) => {
});
}


function write(scope,targetname) // This function is used to load data into txt file
{
    exec("echo "+scope+" >> "+savepath+targetname+"/scope.txt", (error, stdout, stderr) => {
});
}


function load(cdb,targetname){

    let i;
        for (i in cdb){
            let fetdata = cdb[i]
            write(fetdata,targetname)// calling write function
        }
        wrecking(targetname,savepath)

}


class initializ {
    constructor(targetname) {
        makedir(targetname); // calling makdir function
        let cdb = new dbs.initializ(targetname); // this function will get the data and load into txt file
        setTimeout(function(){
        load(cdb,targetname);
        },20000)
    }
}

class readbugs {
    constructor(targetname) {
        makedir(targetname); // calling makdir function
        let cdb = new dbs.initializ(targetname); // this function will get the data and load into txt file
        setTimeout(function(){
        load(cdb,targetname);
        },20000)
    }
}

module.exports = {

    initializ: initializ
};
