#!/usr/bin/node
var k = new Array(176,214,205,246,264,255,227,237,242,244,265,270,283);
var u = "administrator";
let p = "";

for(i = 0; i < u.length; i++) {
p += String.fromCharCode(k[i] - (u.charCodeAt(i) + i * 10))
}
console.log(p);
