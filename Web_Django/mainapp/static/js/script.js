// 미디어사이즈에 따른 메뉴 바 모양 변경 관련 함수
let navBar = document.getElementById("navBar");
function togglebtn(){
    navBar.classList.toggle("hidemenu");
}

// 게시글에서 카테고리 선택 js코드  selectBox
function oneSelect() {
    fm = document.getElementById("fm");
    alert(fm.category.value);
}