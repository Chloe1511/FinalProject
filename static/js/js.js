function redirect()
{
  var checkBox = document.getElementById("defaultCheck1");
   if (checkBox.checked == true){
        window.location.href = '/PreTest';
    }
   else {
          alert("Please indicate that you accept the Terms and Conditions");
        }
}

function endPage(){
    window.location.href = '/end';
}