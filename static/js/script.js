document.querySelector("html").classList.add('js');

var fileInput  = document.querySelector( ".input-file" ),  
    button     = document.querySelector( ".input-file-trigger" ),
    the_return = document.querySelector(".file-return");
        
button.addEventListener( "keydown", function( event ) {  
    if ( event.keyCode == 13 || event.keyCode == 32 ) {  
        fileInput.focus();  
    }  
});
button.addEventListener( "click", function( event ) {
    fileInput.focus();
    return false;
});  
fileInput.addEventListener( "change", function( event ) {  
    var len = fileInput.files.length;
    var text = document.createElement('p');
    if (len == 1)
        text.innerText = "Selected file: ";
    else
        text.innerText = len + " files selected";
    the_return.appendChild(text);

    the_return.style.border = "5px dashed #1FB264";
    // the_return.style["border-radius"] = "5%";

    for (var i = 0; i < len; i++){
        var file = event.target.files[i];
        // the_return.innerHTML = this.value;  

        //create new img
        var new_img = document.createElement('img');
        new_img.setAttribute("style","height:200px; padding: 0 10px 25px 10px;");
        new_img.setAttribute("id","image"+i);

        //add new tag to return DIV
        the_return.appendChild(new_img);

        var selectedFile = file;
        var reader = new FileReader();
        var imgtag = document.getElementById("image"+i);
        imgtag.title = selectedFile.name;

        var myCanvas = document.createElement("canvas");
        var ctx = myCanvas.getContext('2d');
        var img = new Image();
        img.onload = function(){
            myCanvas.width = img.width;
            myCanvas.height = img.height;
            ctx.drawImage(img, 0, 0);
            console.log(myCanvas.toDataURL('image/jpeg'));
        };

        imgtag.src = URL.createObjectURL(file);

        reader.readAsDataURL(selectedFile);
    }

});  
