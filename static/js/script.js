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
    for (var i = 0; i < fileInput.files.length; i++){
        var file = event.target.files[i];
        // the_return.innerHTML = this.value;  
        // create new p
        var new_p = document.createElement('p');
        new_p.innerText = String(file.name);

        //create new img
        var new_img = document.createElement('img');
        new_img.setAttribute("style","height:200px");
        new_img.setAttribute("id","image"+i);

        //add new tag to return DIV
        the_return.appendChild(new_p);
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
