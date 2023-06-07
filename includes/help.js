#!/usr/bin/env node
/**
 * gh0str3con
 * gh0str3con is a All in one cloud based web Recon tool.
 *
 * @author karthikeyan V (karthithehacker) <https://karthithehacker.com>
 */

const { boolean } = require("yargs");
//lib and includes section 
require("os").userInfo().username
module.exports = {
    helpmenu: function() {
       var argv = require('yargs/yargs')(process.argv.slice(2))
          .usage('\n\n \x1b[30;1m$\x1b[0m \x1b[32;1mGh0str3con \x1b[36;1m[option]\n\n \x1b[37;42;1mUsage:\x1b[0m $0 \x1b[33;1m[options]\x1b[30;1m')
          .version('version', '1.0.1').alias('version', 'V')
          .options({
            help: {
              alias: 'h',
              description: "Show help",
              requiresArg: true,
              required: false
            },
            
            port: {
              alias: 'p',
              description: "Provide availabe port between 0 to 65536",
              requiresArg: true,
              required: false
            }
          })
          .argv;
        console.log('Inspecting options');
        console.dir(argv);
        console.log("input:", argv.input);
        console.log("output:", argv.output);
    },
     helpintro: function() {
cyan='\e[1;36m%s\e[0m\n'
console.log("  \n\n\x1b[36;1m👋 Hey \x1b[37;1m"+require("os").userInfo().username+" \x1b[36;1m\n");
console.log(" .-----------------------------.           ");
console.log(" |  Tool   : \x1b[31mGh0str3con \x1b[36;1m       |           ");
console.log(" |  Author : \x1b[32;1m@karthithehacker🎖️\x1b[36;1m |           ");
console.log(" |        \x1b[30m1'or'1='1 \x1b[30m\x1b[36;1m           |           ");
console.log(" '-----------------------------'           ");
console.log("                 ^      (\\_/)    ");
console.log("                 '----- (O.o)    ");
console.log("                        (> <)    ");

     }
};