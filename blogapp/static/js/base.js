// navbar-nav li:last-child 클릭시 logoutForm 보내기
document
  .querySelector(".navbar-nav li:last-child")
  .addEventListener("click", (e) => {
    document.querySelector("#logoutForm").submit();
  });
