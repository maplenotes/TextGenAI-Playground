
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById("generate").addEventListener("click", () => generate_onclick())
})

function generate_onclick() {
  (async () => {
    const input = document.getElementById("input").value;

    const response = await fetch('/inference', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "prompt":input }),
    }).then(response => response.json());
    
    const output = response.answer;

    const div = document.createElement("div");
    div.innerHTML = `<p><b>Input:</b> ${input}</p><p><b>Output:</b> ${output}</p>`;
    document.getElementById("history").appendChild(div);
  })();
};
