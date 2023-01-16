// import fetch from "node-fetch"

import fetch from 'node-fetch';
// import jsdom from "jsdom"
// const { JSDOM } = jsdom;

// Github username may only contain alphanumeric characters or hyphens.
// Github username cannot have multiple consecutive hyphens.
// Github username cannot begin or end with a hyphen.
// Maximum is 39 characters.

// x(?=y),  Matches "x" only if "x" is followed by "y".
// (?:x)	Non-capturing group: Matches "x" but does not remember the match.
// start with the alphanumeric character, a hypen followed by alphanumeric characters
var re = /^[a-z\d]([a-z\d]|-(?=[a-z\d])){0,38}$/i;
var str = "hello-rs";
var result = re.test(str);
console.log(result);