## nroonga

nroonga is a library for building groonga powered node.
You can write your custom full-text search backend on the top of node.js and groonga.

### To build and run tests:

    % npm install
    % npm test

### To run examples:

Super simple test script:

    % node examples/test.js

A CLI example (like groonga stand-alone mode):

    % coffee examples/prompt.coffee

A http daemon example (like groonga server mode):

    % coffee examples/server.coffee

### Examples

    var nroonga = require('nroonga');
    var db = new nroonga.Database('database');
    
    // Synchronous
    console.log(db.commandSync('status'));
    
    // Asynchronous
    db.command('status', function(error, data) {
      console.log(data);
    });

### new nroonga.Database([[path], openOnly])

Open a groonga database.

If [path] is given, create a persistent db. Otherwise, create a temporary db.

If [openOnly] is set to `true`, do not attempt to create even if open failed. Otherwise, try to create a new database.

### database.commandSync(command)

Send `command` to groonga. Block until results returned.

### database.command(command, [options], callback)

Asynchronously send `command` to groonga. Callback will be given two arguments `(error, data)`.
