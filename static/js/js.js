function redirect()
{
  var checkBox = document.getElementById("defaultCheck1");
   if (checkBox.checked == true){
        window.location.href = '/PreTest';
    }
   else {
       alert("נא סמן כי אתה מסכים לתנאים");

        }
}

function endPage(){
    window.location.href = '/end';
}