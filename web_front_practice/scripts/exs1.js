
function change_data(){
  let valueElement=document.getElementById("date_time_button");
  let  buttonElement=document.getElementById("myButton");
  if (valueElement.style.display === "none") { 
     valueElement.innerHTML=Date();
     valueElement.style.display = "block" ;
     buttonElement.textContent = "Hide Date";
  } else { 
    valueElement.style.display = "none";
    buttonElement.textContent = "Show Date";
  }
}

