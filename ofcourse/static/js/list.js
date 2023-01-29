filterSelection("all");

function filterSelection(c) {
    var x, i, filterBtnList;
    x = document.getElementsByClassName("filterDiv");

    if (c == "all") c = "";
    for (i = 0; i < x.length; i++) {
        w3RemoveClass(x[i], "show");
        if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
    }
}

function w3AddClass(element, name) {
    filterBtnList = document.querySelectorAll(".btn-wrap .btn-l-wrap .btn");
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
        
    filterBtnList.forEach((filterBtn) => {
        filterBtn.classList = filterBtn.classList[0];
    });

    filterBtnList.forEach((filterBtn) => {
        // console.log(arr1, arr2, filterBtn.innerHTML);
        if (arr1[1] === filterBtn.innerHTML.trim()) {
            filterBtn.classList.add("on");
        }
    });
}

function w3RemoveClass(element, name) {
    filterBtnList = document.querySelectorAll(".btn-wrap .btn-l-wrap .btn");
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}

// Add active class to the current button (highlight it)
// var btnContainer = document.getElementById("myBtnContainer");
// var btns = btnContainer.getElementsByClassName("btn");
// for (var i = 0; i < btns.length; i++) {
//     btns[i].addEventListener("click", function () {
//         var current = document.getElementsByClassName("active");
//         current[0].className = current[0].className.replace(" active", "");
//         this.className += " active";
//     });
// }
