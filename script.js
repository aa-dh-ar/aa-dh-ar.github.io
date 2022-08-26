var container = document.getElementById('container');
var container2 = document.getElementById('container2');
var container3 = document.getElementById('container3');
var text = document.getElementById('text');
var back = document.getElementById('back');
var back2 = document.getElementById('back2');
var about = document.getElementById('About')

text.onclick = function(){
		container.className = "vanish";
		container3.className = "vanish";
		container2.className = "open";
}

back.onclick = function(){
	container2.className = "vanish";
	container3.className = "vanish";
	container.className = "open";
}

about.onclick = function(){
		container.className = "vanish";
		container2.className = "vanish";
		container3.className = "open";
}

back2.onclick = function(){
	container3.className = "vanish";
	container2.className = "vanish";
	container.className = "open";
}