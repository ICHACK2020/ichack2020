"use strict";

var uid;
var first = true;

var redR = 192;
var redG = 57;
var redB = 43;

var greenR = 0;
var greenG = 230;
var greenB = 64;

function interpolate(troll) {
    var input = troll <= 0.5 ? troll * 2.0 : 1.0;
    var red = input * redR + (1.0 - input) * greenR;
    var green = input * redG + (1.0 - input) * greenG;
    var blue = input * redB + (1.0 - input) * greenB;
    return "rgb(" + Math.floor(red) + ", " + Math.floor(green) + ", " + Math.floor(blue) + ")"
}
//var socket = new WebSocket("ws://146.169.207.172:8080/talk/");

//let socket = new WebSocket("ws://146.169.207.172:8080/talk/")
var url = document.URL.split("/")
var convId = url.pop().slice(0, url.length - 1)
var topic = url.pop()
let socket = new WebSocket("ws://146.169.207.172:8080/ws/" + topic + "/" +convId)

socket.onopen = function(e) {
    console.log("Success!");
}
socket.onmessage = function(e) {
  if (first) {
    uid = parseInt(e.data);
    console.log(e);
    first = false;
    //Stop waiting for users
    document.getElementById("loadingBox").style.visibility = "hidden";
  } else {
    var obj = JSON.parse(e.data);
    if (uid == obj.UID) {
      addMyMessage(obj.Msg, obj.Troll);
    } else {
      addOtherMessage(obj.Msg, obj.Troll);
    }
    handleResize();
    console.log(JSON.parse(e.data));
  }
}

socket.onclose = function(e) {
  console.log("closing");
  document.getElementById("modalBtn").click();
}

socket.onerror = function(e) {
  console.log(e);
}

class incomingMsg {
  constructor(Msg) {
    this.UID = uid;
    this.ConvID = convId;
    this.Msg = Msg;
  }
}

function sendMessage() {
  let chatArea = document.getElementById("chatArea");
  if (chatArea.value == "") {
      alert("Enter a message");
      return;
  }
  socket.send(JSON.stringify(new incomingMsg(chatArea.value)));
  chatArea.value = "";
}

function addMyMessage(message, troll) {
  let messageBox = document.getElementById("messageBox");
  messageBox.insertAdjacentHTML("beforeend", '<div class="panel message myMessage"><div class="panel-body"></div></div>');
  printMessage(message);
  messageBox.lastChild.style.borderColor = interpolate(troll);
}

function addOtherMessage(message, troll) {
  let messageBox = document.getElementById("messageBox");
  messageBox.insertAdjacentHTML("beforeend", '<div class="panel message otherMessage"><div class="panel-body"></div></div>');
  printMessage(message);
  messageBox.lastChild.style.borderColor = interpolate(troll);
}

function printMessage(message) {
  var node = document.createTextNode(message);
  document.getElementById("messageBox").lastChild.firstChild.appendChild(node);
  handleResize();
  window.scrollTo(0, document.body.scrollHeight);
}


document.onkeydown = function (event) {
  if (event.key === "Enter") {
    sendMessage();
    return false;
  }
};

function handleResize() {
  $(".myMessage").css("left", (window.innerWidth >= 390 ? window.innerWidth - 390 : 0) + "px");
}

window.onresize = function (event) {
  handleResize();
};

function onMessageInput() {
  let chatArea = document.getElementById("chatArea");
  let sendButton = document.getElementById("sendButton");
  if (chatArea.value == "") {
    sendButton.classList.add("disabled");
  } else {
    sendButton.classList.remove("disabled");
  }
}

function toHomePage() {
  window.location.replace("http://146.169.207.172:8080");
}

onMessageInput();
handleResize();
