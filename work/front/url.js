const url = new URL(window.location.href);
const parameterValue = url.searchParams.get('graph');
console.log(parameterValue);
var element = document.getElementsByClassName("fullScreenGraph");
console.log(element);
element[0].setAttribute("id", parameterValue);