function IsEmpty(){
  if(document.forms['frm'].name.value === "")
  {
    alert("Заполните все поля!");
    return false;
  }
    return true;
}
