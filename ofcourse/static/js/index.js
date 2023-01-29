// * 가로 스크롤 구현 =====================================
console.log('index.js loaded')

//* 요소, 사이즈
// const list = document.querySelector(".list-card > .skill-list ul");
const lists = document.querySelectorAll(".list-card > .skill-list ul");

for (i = 0; i < lists.length; i++) {
    let list = lists[i];

    const listScrollWidth = list.scrollWidth;
    const listClientlWidth = list.clientWidth;

    //* 이벤트마다 갱신할 값
    let startX = 0;
    let nowX = 0;
    let endX = 0;
    let listX = 0;

    console.log(list, listScrollWidth, listClientlWidth);

    //* 이벤트 헨들러 선언
    // 스크롤 시작 이벤트
    const onScrollStart = (e) => {
        console.log("scroll start");
        startX = getClientX(e);
        window.addEventListener("mousemove", onScrollMove);
        window.addEventListener("mouseup", onScrollEnd);
        window.addEventListener("touchmove", onScrollMove);
        window.addEventListener("touchend", onScrollEnd);
    };
    // 스크롤 진행 이벤트
    const onScrollMove = (e) => {
        nowX = getClientX(e);
        setTranslateX(listX + nowX - startX);
    };
    const onScrollEnd = (e) => {
        endX = getClientX(e);
        listX = getTranslateX();

        if (listX > 0) {
            setTranslateX(0);
            list.style.transition = "all 0.3s ease";
            listX = 0;
        } else if (listX < listClientlWidth - listScrollWidth) {
            setTranslateX(listClientlWidth - listScrollWidth);
            list.style.transition = "all 0.3s ease";
            listX = listClientlWidth - listScrollWidth;
        }

        window.removeEventListener("mousedown", onScrollStart);
        window.removeEventListener("touchstart", onScrollStart);
        window.removeEventListener("mousemove", onScrollMove);
        window.removeEventListener("touchmove", onScrollMove);
        window.removeEventListener("mouseup", onScrollEnd);
        window.removeEventListener("touchend", onScrollEnd);
        window.removeEventListener("click", onClick);

        setTimeout(() => {
            bindEvents();
            list.style.transition = "";
        }, 300);
    };
    const onClick = (e) => {
        if (startX - endX !== 0) {
            e.preventDefault();
        }
    };

    //* 유틸 함수 정의 - 코드에서 재사용되는 부분
    const getClientX = (e) => {
        const isTouches = e.touches ? true : false;
        return isTouches ? e.touches[0].clientX : e.clientX;
    };
    const getTranslateX = () => {
        return parseInt(
            getComputedStyle(list).transform.split(/[^\-0-9]+/g)[5]
        );
    };
    const setTranslateX = (x) => {
        console.log("setTranslate");
        list.style.transform = `translateX(${x}px)`;
    };

    // 이벤트 바인딩
    const bindEvents = () => {
        list.addEventListener("mousedown", onScrollStart);
        list.addEventListener("touchstart", onScrollStart);
        list.addEventListener("click", onClick);
    };
    bindEvents();
}


//* filter에 따른 버튼 css 추가 =====================================
// 1. url에서 filter 값 가져오기
let filter = window.location.search.split('=')[1]

// 2. 필터에서 url filter 값과 동일한 필터 버튼을 찾기
let filterBtns = document.querySelectorAll('.btn-r-wrap .btn')
filterBtns.forEach(filterBtn => {
    filterBtnName = filterBtn.href.split('=')[1]
    // console.log(filterBtnName)
    if (filter === filterBtnName){
        filterBtn.classList.add('on')
    }
});