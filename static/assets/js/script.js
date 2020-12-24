var mini = true;
var print = console.log;

function toggleSidebar() {
	if (mini) {
		document.getElementById("mySidebar").style.width = "300px";
		this.mini = false;
	} else {
		document.getElementById("mySidebar").style.width = "100px";
		this.mini = true;
	}
}
