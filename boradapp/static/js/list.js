const actionForm = document.querySelector("#actionForm");

// .page-link 클릭시
// page 번호 가져온 후 actionForm 안의 페이지 값 변경
// actionForm 보내기
document.querySelector(".pagination").addEventListener("click", (e) => {
  e.preventDefault();
  actionForm.page.value = e.target.getAttribute("href");
  actionForm.action = "/board";
  actionForm.submit();
});

// 제목 클릭 시 a태그 중지
// actionForm 의 action 수정 후 acrtionForm 보내기
document.querySelector("tbody").addEventListener("click", (e) => {
  e.preventDefault();
  actionForm.action = e.target.getAttribute("href");
  actionForm.submit();
});

document.querySelector(".so").addEventListener("change", (e) => {
  actionForm.so.value = e.target.value;

  actionForm.submit();
});

// 찾기버튼 클릭시 (검색)
// actionForm 보내기
// 상요자가 입력한 keyword를 actionForm 의 keyword값으로 변경
// page =1 변경

document
  .querySelector(".btn-outline-secondary")
  .addEventListener("click", () => {
    actionForm.keyword.value = document.querySelector("[name='keyword']").value;
    actionForm.page.value = 1;
    actionForm.submit();
  });
