(function() {
  [].forEach.call(document.getElementsByClassName("delete"), deleteButton => {
    deleteButton.addEventListener("click", event => {
      let answer = confirm("Точно хотите удалить?", "");

      if (!answer) {
        event.preventDefault();
        return;
      }
    });
  });
})(document, window);
