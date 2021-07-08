let total, auxList1, auxList2, aux; 
                        
function cart_logic(total, auxList1, auxList2, aux) {
  total = document.getElementById('total');
  auxList1 = document.getElementsByClassName('gamequantity');
  auxList2 = document.getElementsByClassName('gameprice1');
  auxList3 = document.getElementsByClassName('gameprice2');

  total.innerText = 0;

  //Amount
  for(let i=0; i < auxList1.length; i++) {
    aux = auxList3[i];
    aux.innerText = parseInt(aux.innerText, 10) * auxList1[i].value + '€';
  }

  //Total
  for(let i=0; i < auxList1.length; i++) {
    aux = auxList3[i];
    total.innerText = parseInt(total.innerText, 10) + parseInt(aux.innerText, 10) + '€'; 
  }
  
}

total.onload = cart_logic();

total.addEventListener("change", function (params) {
  cart_logic();
});