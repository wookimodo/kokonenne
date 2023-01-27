
$(document).ready(function(){
    $("input[type='checkbox']").on("click",function(){
        let count = $("input:checked[type='checkbox']").length;
        console.log(count)
        if (count>5){
            //$(this).prop("checked",false);
            this.checked=false;
            alert("5개까지만 선택이 가능합니다.")
        }
    });
});