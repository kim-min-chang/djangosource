const actionForm = document.querySelector("#actionForm");

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
