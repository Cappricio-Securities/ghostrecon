#!/usr/bin/env node
/**
 * gh0str3con
 * gh0str3con is a All in one cloud based web Recon tool.
 *
 * @author karthikeyan V (karthithehacker) <https://karthithehacker.com>
 */

const express = require("express");
const routes = express.Router();
const dbs = require('./dbgateway');
const engine = require('./engine');
const lowdb = require('lowdb');
const FileSync = require('lowdb/adapters/FileSync'),
    path = require('path'),
    adapter = new FileSync('database/gh0str3con.json'),
    db = lowdb(adapter);

let data;

var currentTime = new Date();
var currentOffset = currentTime.getTimezoneOffset();
var ISTOffset = 330;
var date_time = new Date(currentTime.getTime() + (ISTOffset + currentOffset)*60000);
var hoursIST = date_time.getHours()



routes.get('/',(req,res)=>{    
    adapters = new FileSync('database/gh0str3con.json'),
    dbl = lowdb(adapters);
    data = dbl.get('admin.reconinfo').value();
    res.render('index.ejs',{cred:data});
})

routes.get('/new',(req,res)=>{
    res.render('bughunting.ejs',{sucess:'0'});
})

routes.post('/newrecon',(req,res)=>{
    data = req.body;
    targetname = req.body.name;
    report = req.body.reportpath;
    scopes = req.body.subs;
    db.get('admin.reconinfo').push({
        targetname:targetname,
        report:report,
        scope:scopes,
        recOn:"pending",
        createdat:date_time.toISOString()
    }).write();
    res.render('bughunting.ejs',{sucess:'2'});
    d = new dbs.targetdb(targetname,scopes,report);
    a  = new engine.initializ(targetname);
})

routes.post('/update',(req,res)=>{
    data = req.body;
    targetname = req.body.name;
    scopes = req.body.subs;
    live = req.body.live;
    ports = req.body.ports;
    statu = req.body.status;
    db.get('admin.reconinfo').find({targetname: targetname}).assign({ recOn: 'completed' }).write();
    d = new dbs.targetdbload(targetname,scopes,live,ports,statu);
    res.send('ok');
})


routes.get('/:target',(req,res)=>{
    
    dat = req.params.target
    d = new dbs.retrive(dat);
    a = db.get('admin.reconinfo').find({"targetname": dat}).value().report;
    re = db.get('admin.reconinfo').find({"targetname": dat}).value().recOn;
    if(re == "pending"){
        res.render('index.ejs',{cred:data,reinfo:d});
    }
    res.render('targetpage.ejs',{cred:d,comp:dat,repo:a});
})

module.exports = routes;