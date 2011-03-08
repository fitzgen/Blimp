var ids = [];

function getNumTimers () {
    return Number(document.querySelector("#num-timers").value);
}

function getTaskLength () {
    return Number(document.querySelector("#task-length").value);
}

function stop () {
    ids.forEach(function (id) {
        chronos.clearInterval(id);
        window.clearInterval(id);
    });
    ids = [];
}

function withChronos () {
    var numTimers = getNumTimers();
    var taskLen = getTaskLength();
    for ( var i = 0; i < numTimers; i++ ) {
        ids.push(chronos.setInterval(function () {
            var start = +new Date();
            while ( +new Date() - start < taskLen ) ;
        }, 50));
    }
}

function withoutChronos () {
    var numTimers = getNumTimers();
    var taskLen = getTaskLength();
    for ( var i = 0; i < numTimers; i++ ) {
        ids.push(window.setInterval(function () {
            var start = +new Date();
            while ( +new Date() - start < taskLen ) ;
        }, 50));
    }
}

document
    .querySelector("#with-chronos")
    .addEventListener("click", function (event) {
        event.preventDefault();
        stop();
        withChronos();
    }, false);

document
    .querySelector("#without-chronos")
    .addEventListener("click", function (event) {
        event.preventDefault();
        stop();
        withoutChronos();
    }, false);

document
    .querySelector("#stop")
    .addEventListener("click", function (event) {
        event.preventDefault();
        stop();
    }, false);