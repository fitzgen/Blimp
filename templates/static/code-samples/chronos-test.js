function getNumTimers () {
    return Number(document.querySelector("#num-timers").value);
}

function getTaskLength () {
    return Number(document.querySelector("#task-length").value);
}

var ids = [];

function stop () {
    ids.forEach(function (id) {
        chronos.clearInterval(id);
        window.clearInterval(id);
    });
    ids = [];
}

var incrementCounter = (function () {
    var counter = 0;
    var counterEl = document.querySelector("#counter");
    return function () {
        counterEl.innerHTML = counter++;
    };
}());

function makeTest (hostObj) {
    return function () {
        var numTimers = getNumTimers();
        var taskLen = getTaskLength();
        for ( var i = 0; i < numTimers; i++ ) {
            ids.push(hostObj.setInterval(function () {
                var start = +new Date();
                while ( +new Date() - start < taskLen ) {
                    incrementCounter();
                }
            }, 50));
        }
    };
}

var withChronos = makeTest(chronos);
var withoutChronos = makeTest(window);

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