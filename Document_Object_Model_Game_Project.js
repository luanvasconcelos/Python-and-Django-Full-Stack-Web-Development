
var cells = document.querySelectorAll("td"); // Selecting every cell with 'td'

function change(){
    if(this.textContent === ''){
      this.textContent = 'X';
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = '';
    }
};

for (var i = 0; i < cells.length; i++) {
    cells[i].addEventListener('click', change); //Adding an event for each cell with cells[i]
}

var clear = document.querySelector("#button");//Selecting the button with '#id'

function clean(){
  for (var i = 0; i < cells.length; i++) {
    cells[i].textContent = '';//Adding nothing '' to every cell
  }
}

clear.addEventListener('click',clean);
