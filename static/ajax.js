var campaignNameBox = document.getElementById('campaignName');
//TODO: create a dropdown element in the template
var dropdown;
campaignNameBox.addEventListener('input', getXHR);

function getXHR(){
  var xhr = new XMLHttpRequest();
  var urlPath = "/get/?query=" + encodeURI(campaignNameBox.value) + "/";
  xhr.open("GET", urlPath, true);
  //clear contents before replacing with new contents
  dropdown.innerHTML = "";
  xhr.onload = function(e) {
    if (xhr.readyState == 4) {
      if (xhr.status == 200) {
        var suggestions = JSON.parse(xhr.responseText);
        if (suggestions){
          suggestions.forEach(function(val){
          //TODO: Add in the found results here
          //TODO: add event listeners to the results so they are clickable

        }
      } else {

        console.log(xhr.statusText);
        console.log(xhr.status);
      }
    }
  };
  xhr.onerror = function (e) {
    console.log("error!");
    console.error(e);
  };
  xhr.send(null);
}
